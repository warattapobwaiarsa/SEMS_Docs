#!/usr/bin/env python3
"""Check local Markdown paths, anchors, case collisions and trailing whitespace."""

from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
SKIP = {".git", "tmp", ".tmp-sheet-inspect"}
LINK = re.compile(r"!?\[[^\]]*]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
EXPLICIT_ID = re.compile(r"<a\s+(?:name|id)=[\"']([^\"']+)[\"']", re.I)


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).strip().lower()
    text = "".join(
        c
        for c in text
        if c in "-_ " or unicodedata.category(c)[0] in {"L", "M", "N"}
    )
    return re.sub(r"[\s]+", "-", text)


def anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    found = set(EXPLICIT_ID.findall(text))
    seen: dict[str, int] = {}
    for heading in HEADING.findall(text):
        base = slug(re.sub(r"`([^`]*)`", r"\1", heading))
        count = seen.get(base, 0)
        found.add(base if count == 0 else f"{base}-{count}")
        seen[base] = count + 1
    return found


def main() -> int:
    errors: list[str] = []
    files = [p for p in ROOT.rglob("*") if p.is_file() and not SKIP.intersection(p.parts)]
    folded: dict[str, Path] = {}
    for path in files:
        key = str(path.relative_to(ROOT)).casefold()
        if key in folded:
            errors.append(f"case-colliding path: {folded[key]} <> {path}")
        folded[key] = path

    markdown = [p for p in files if p.suffix.lower() == ".md"]
    anchor_cache: dict[Path, set[str]] = {}
    for source in markdown:
        text = source.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{source.relative_to(ROOT)}:{line_no}: trailing whitespace")
        for raw in LINK.findall(text):
            if re.match(r"^(?:https?://|mailto:|data:)", raw):
                continue
            path_part, _, fragment = unquote(raw).partition("#")
            target = source if not path_part else (source.parent / path_part).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: path escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing target: {raw}")
                continue
            if fragment and target.suffix.lower() == ".md":
                fragment = unicodedata.normalize("NFKC", fragment)
                anchor_cache.setdefault(target, anchors(target))
                if fragment not in anchor_cache[target]:
                    errors.append(f"{source.relative_to(ROOT)}: missing anchor: {raw}")

    for error in errors:
        print(error)
    print(f"checked {len(markdown)} Markdown files; errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
