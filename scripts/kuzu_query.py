from __future__ import annotations

import argparse
from pathlib import Path

import kuzu


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "Graph" / "kuzu-db"


def rows(result: kuzu.QueryResult) -> list[list[object]]:
    out: list[list[object]] = []
    while result.has_next():
        out.append(result.get_next())
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the local Kuzu semantic graph.")
    parser.add_argument("concept", nargs="?", help="Concept name to inspect.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--list", action="store_true", help="List all concepts.")
    parser.add_argument("--list-notes", action="store_true", help="List all note paths.")
    parser.add_argument("--note", action="store_true", help="Inspect Markdown links for a note path instead of semantic edges for a concept.")
    parser.add_argument("--all", action="store_true", help="Inspect both concept semantic edges and note links.")
    args = parser.parse_args()

    if not args.db.exists():
        raise SystemExit(f"Database not found: {args.db}. Run scripts/kuzu_build.py first.")

    db = kuzu.Database(str(args.db), read_only=True)
    conn = kuzu.Connection(db)

    if args.list:
        result = conn.execute("MATCH (c:Concept) RETURN c.name ORDER BY c.name")
        for (name,) in rows(result):
            print(name)
        return

    if args.list_notes:
        result = conn.execute("MATCH (n:Note) RETURN n.path ORDER BY n.path")
        for (path,) in rows(result):
            print(path)
        return

    if not args.concept:
        raise SystemExit("Provide a concept/note name or pass --list/--list-notes.")

    if args.note or args.all:
        result = conn.execute(
            """
            MATCH (source:Note {path: $path})-[edge:LINKS_TO]->(target:Note)
            RETURN source.path, edge.label, edge.anchor, target.path, 'outgoing'
            UNION ALL
            MATCH (source:Note)-[edge:LINKS_TO]->(target:Note {path: $path})
            RETURN source.path, edge.label, edge.anchor, target.path, 'incoming'
            """,
            {"path": args.concept},
        )
        found_links = rows(result)
        if found_links:
            print(f"Markdown links for {args.concept!r}:")
            for source, label, anchor, target, direction in found_links:
                anchor_text = f"#{anchor}" if anchor else ""
                arrow = "->" if direction == "outgoing" else "<-"
                other = target if direction == "outgoing" else source
                print(f"  {arrow} {other}{anchor_text}  label={label!r}")
        elif args.note:
            print(f"No Markdown links found for note {args.concept!r}.")
        if args.note and not args.all:
            return

    result = conn.execute(
        """
        MATCH (source:Concept {name: $concept})-[edge:SEMANTIC_EDGE]->(target:Concept)
        RETURN source.name, edge.relation, target.name, edge.evidence_path,
               edge.evidence_heading, edge.evidence_summary, edge.confidence
        UNION ALL
        MATCH (source:Concept)-[edge:SEMANTIC_EDGE]->(target:Concept {name: $concept})
        RETURN source.name, edge.relation, target.name, edge.evidence_path,
               edge.evidence_heading, edge.evidence_summary, edge.confidence
        """,
        {"concept": args.concept},
    )

    found = rows(result)
    if not found:
        if not args.all:
            print(f"No semantic edges found for {args.concept!r}.")
        return

    if args.all:
        print(f"Semantic edges for {args.concept!r}:")
    for source, relation, target, evidence_path, evidence_heading, evidence_summary, confidence in found:
        print(f"{source} -[{relation}]-> {target}  confidence={confidence}")
        if evidence_path:
            heading = f"#{evidence_heading}" if evidence_heading else ""
            print(f"  evidence: {evidence_path}{heading}")
        if evidence_summary:
            print(f"  summary: {evidence_summary}")


if __name__ == "__main__":
    main()
