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

    if not args.concept:
        raise SystemExit("Provide a concept name or pass --list.")

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
        print(f"No semantic edges found for {args.concept!r}.")
        return

    for source, relation, target, evidence_path, evidence_heading, evidence_summary, confidence in found:
        print(f"{source} -[{relation}]-> {target}  confidence={confidence}")
        if evidence_path:
            heading = f"#{evidence_heading}" if evidence_heading else ""
            print(f"  evidence: {evidence_path}{heading}")
        if evidence_summary:
            print(f"  summary: {evidence_summary}")


if __name__ == "__main__":
    main()
