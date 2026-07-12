#!/usr/bin/env python3
"""Build a Kuzu graph from Markdown files in this repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

import kuzu

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+\.md)(?:#[^)]+)?\)", re.IGNORECASE)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def note_id(path: Path) -> str:
    return hashlib.sha256(path.as_posix().encode("utf-8")).hexdigest()[:24]


def cypher_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path(".artifacts/obsidian.kuzu"))
    args = parser.parse_args()

    repo = args.repo.resolve()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    ignored = {".git", ".obsidian", "node_modules", ".venv", "venv", ".artifacts"}
    files = sorted(
        p for p in repo.rglob("*.md")
        if not any(part in ignored for part in p.relative_to(repo).parts)
    )

    notes = []
    by_stem: dict[str, list[dict]] = {}
    by_path: dict[str, dict] = {}
    for path in files:
        rel = path.relative_to(repo)
        text = path.read_text(encoding="utf-8", errors="replace")
        heading = TITLE_RE.search(text)
        title = heading.group(1).strip() if heading else path.stem
        note = {
            "id": note_id(rel),
            "path": rel.as_posix(),
            "title": title,
            "content": text,
        }
        notes.append(note)
        by_path[rel.as_posix().lower()] = note
        by_stem.setdefault(path.stem.lower(), []).append(note)

    db = kuzu.Database(str(output))
    conn = kuzu.Connection(db)
    conn.execute("CREATE NODE TABLE Note(id STRING, path STRING, title STRING, content STRING, PRIMARY KEY(id))")
    conn.execute("CREATE REL TABLE LINKS_TO(FROM Note TO Note, raw_target STRING)")

    for note in notes:
        conn.execute(
            "CREATE (:Note {id: '" + cypher_string(note["id"]) +
            "', path: '" + cypher_string(note["path"]) +
            "', title: '" + cypher_string(note["title"]) +
            "', content: '" + cypher_string(note["content"]) + "'})"
        )

    edges = []
    for source in notes:
        targets = set(WIKILINK_RE.findall(source["content"]))
        targets.update(MD_LINK_RE.findall(source["content"]))
        for raw in sorted(targets):
            cleaned = raw.strip().replace("\\", "/")
            target = by_path.get(cleaned.lower())
            if target is None:
                candidates = by_stem.get(Path(cleaned).stem.lower(), [])
                target = candidates[0] if len(candidates) == 1 else None
            if target is None:
                continue
            conn.execute(
                "MATCH (a:Note), (b:Note) WHERE a.id = '" + cypher_string(source["id"]) +
                "' AND b.id = '" + cypher_string(target["id"]) +
                "' CREATE (a)-[:LINKS_TO {raw_target: '" + cypher_string(raw) + "'}]->(b)"
            )
            edges.append({"from": source["path"], "to": target["path"], "raw_target": raw})

    manifest = {
        "notes": len(notes),
        "links": len(edges),
        "database": str(output),
        "sample_paths": [n["path"] for n in notes[:20]],
    }
    manifest_path = output.parent / "kuzu-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
