from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any

import kuzu


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "Graph" / "kuzu-db"
EDGE_BLOCK_RE = re.compile(r"<!--\s*semantic-edges\s*(.*?)\s*-->", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")


def validate_edge(edge: dict[str, Any], location: str) -> dict[str, Any]:
    required = {"source", "relation", "target"}
    missing = sorted(required - set(edge))
    if missing:
        raise SystemExit(f"{location}: missing required fields: {', '.join(missing)}")
    return edge


def read_jsonl_edges(path: Path) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            edge = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
        edges.append(validate_edge(edge, f"{path}:{line_no}"))
    return edges


def read_markdown_edges(notes_root: Path) -> list[dict[str, Any]]:
    edges: list[dict[str, Any]] = []
    for path in sorted(notes_root.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if relative.parts and relative.parts[0] == "Graph":
            continue
        text = path.read_text(encoding="utf-8")
        for block_index, match in enumerate(EDGE_BLOCK_RE.finditer(text), start=1):
            for line_no, line in enumerate(match.group(1).splitlines(), start=1):
                if not line.strip():
                    continue
                location = f"{path}:semantic-edges block {block_index}, line {line_no}"
                try:
                    edge = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"{location}: invalid JSON: {exc}") from exc
                edge = validate_edge(edge, location)
                edge.setdefault("evidence_path", relative.as_posix())
                edges.append(edge)
    return edges


def iter_note_paths(notes_root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(notes_root.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if relative.parts and relative.parts[0] in {"Graph", "graphify-out"}:
            continue
        paths.append(path)
    return paths


def strip_semantic_edge_blocks(text: str) -> str:
    return EDGE_BLOCK_RE.sub("", text)


def normalize_note_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_markdown_links(notes_root: Path) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    seen: set[tuple[str, str, str, str]] = set()
    for path in iter_note_paths(notes_root):
        source_path = normalize_note_path(path)
        text = strip_semantic_edge_blocks(path.read_text(encoding="utf-8"))
        for match in MARKDOWN_LINK_RE.finditer(text):
            label = match.group(1).strip()
            raw_target = match.group(2).strip()
            if not raw_target or "://" in raw_target or raw_target.startswith("#"):
                continue
            target_without_anchor, _, anchor = raw_target.partition("#")
            target_path = target_without_anchor.replace("%20", " ")
            target = (path.parent / target_path).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                continue
            if not target.exists() or target.suffix.lower() != ".md":
                continue
            target_path_normalized = normalize_note_path(target)
            key = (source_path, target_path_normalized, label, anchor)
            if key in seen:
                continue
            seen.add(key)
            links.append(
                {
                    "source_path": source_path,
                    "target_path": target_path_normalized,
                    "label": label,
                    "anchor": anchor,
                }
            )
    return links


def ensure_concept(conn: kuzu.Connection, name: str) -> None:
    result = conn.execute("MATCH (c:Concept {name: $name}) RETURN c.name", {"name": name})
    if not result.has_next():
        conn.execute("CREATE (:Concept {name: $name})", {"name": name})


def ensure_note(conn: kuzu.Connection, path: str) -> None:
    result = conn.execute("MATCH (n:Note {path: $path}) RETURN n.path", {"path": path})
    if not result.has_next():
        conn.execute("CREATE (:Note {path: $path, title: $title})", {"path": path, "title": Path(path).stem})


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the local Kuzu graph from Markdown links and embedded semantic edges.")
    parser.add_argument("--notes-root", type=Path, default=ROOT, help="Root to scan for Markdown semantic-edge blocks.")
    parser.add_argument("--edges", type=Path, help="Optional JSONL edge file to include in addition to Markdown blocks.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()

    edges = read_markdown_edges(args.notes_root)
    links = read_markdown_links(args.notes_root)
    if args.edges:
        edges.extend(read_jsonl_edges(args.edges))
    if args.db.is_dir():
        shutil.rmtree(args.db)
    elif args.db.exists():
        args.db.unlink()

    db = kuzu.Database(str(args.db))
    conn = kuzu.Connection(db)
    conn.execute("CREATE NODE TABLE Note(path STRING, title STRING, PRIMARY KEY(path))")
    conn.execute("CREATE NODE TABLE Concept(name STRING, PRIMARY KEY(name))")
    conn.execute(
        """
        CREATE REL TABLE LINKS_TO(
            FROM Note TO Note,
            label STRING,
            anchor STRING
        )
        """
    )
    conn.execute(
        """
        CREATE REL TABLE SEMANTIC_EDGE(
            FROM Concept TO Concept,
            relation STRING,
            evidence_path STRING,
            evidence_heading STRING,
            evidence_summary STRING,
            confidence DOUBLE
        )
        """
    )

    for link in links:
        source_path = link["source_path"]
        target_path = link["target_path"]
        ensure_note(conn, source_path)
        ensure_note(conn, target_path)
        conn.execute(
            """
            MATCH (source:Note {path: $source_path}), (target:Note {path: $target_path})
            CREATE (source)-[:LINKS_TO {
                label: $label,
                anchor: $anchor
            }]->(target)
            """,
            {
                "source_path": source_path,
                "target_path": target_path,
                "label": link["label"],
                "anchor": link["anchor"],
            },
        )

    for edge in edges:
        source = str(edge["source"])
        target = str(edge["target"])
        ensure_concept(conn, source)
        ensure_concept(conn, target)
        conn.execute(
            """
            MATCH (source:Concept {name: $source}), (target:Concept {name: $target})
            CREATE (source)-[:SEMANTIC_EDGE {
                relation: $relation,
                evidence_path: $evidence_path,
                evidence_heading: $evidence_heading,
                evidence_summary: $evidence_summary,
                confidence: $confidence
            }]->(target)
            """,
            {
                "source": source,
                "target": target,
                "relation": str(edge["relation"]),
                "evidence_path": str(edge.get("evidence_path", "")),
                "evidence_heading": str(edge.get("evidence_heading", "")),
                "evidence_summary": str(edge.get("evidence_summary", "")),
                "confidence": float(edge.get("confidence", 0.0)),
            },
        )

    print(f"Built {args.db} from {len(links)} Markdown link(s) and {len(edges)} semantic edge(s).")


if __name__ == "__main__":
    main()
