#!/usr/bin/env python3
"""Compare Markdown document versions with linked indexes and repository tree."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "tmp", ".tmp-sheet-inspect"}
VERSION = re.compile(
    r"(?:^version:\s*[\"']?v?|\|\s*(?:Current )?Version\s*\|\s*\**v?)(\d+\.\d+)",
    re.I | re.M,
)
LINK_VERSION = re.compile(r"\[[^\]]+]\(([^)#]+)\)[^|\n]*\|\s*(v\d+\.\d+)", re.I)
TREE_VERSION = re.compile(r"([A-Za-z0-9_.-]+\.(?:md|yaml|csv|json))\s+\[(v\d+\.\d+)", re.I)


def own_version(path: Path) -> str | None:
    match = VERSION.search(path.read_text(encoding="utf-8")[:3000])
    return f"v{match.group(1)}" if match else None


def main() -> int:
    docs = [
        p
        for p in ROOT.rglob("*.md")
        if not SKIP.intersection(p.parts) and own_version(p)
    ]
    versions = {p.resolve(): own_version(p) for p in docs}
    errors: list[str] = []

    for index in docs:
        text = index.read_text(encoding="utf-8")
        for raw, stated in LINK_VERSION.findall(text):
            target = (index.parent / raw).resolve()
            actual = versions.get(target)
            if actual and actual != stated:
                errors.append(
                    f"{index.relative_to(ROOT)}: {raw} states {stated}, document is {actual}"
                )

    tree = ROOT / "REPOSITORY_TREE.md"
    if tree.exists():
        by_name: dict[str, list[Path]] = {}
        for path, version in versions.items():
            by_name.setdefault(path.name, []).append(Path(path))
        for name, stated in TREE_VERSION.findall(tree.read_text(encoding="utf-8")):
            matches = by_name.get(name, [])
            if len(matches) == 1 and versions[matches[0].resolve()] != stated:
                errors.append(
                    f"REPOSITORY_TREE.md: {name} states {stated}, document is "
                    f"{versions[matches[0].resolve()]}"
                )

    for error in errors:
        print(error)
    print(f"checked {len(docs)} versioned Markdown documents; errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
