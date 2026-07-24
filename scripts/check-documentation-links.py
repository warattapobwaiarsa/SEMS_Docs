#!/usr/bin/env python3
"""Check local Markdown paths, anchors, case collisions and trailing whitespace."""

from pathlib import Path
import json
import re
import subprocess
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
LOCAL_ONLY = re.compile(r"^(?:file://|[A-Za-z]:[\\/])", re.I)
TEMP_PARTS = {"tmp", ".tmp-sheet-inspect", ".agents", ".obsidian"}
TRACKED = set(
    subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()
)


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


def repository_target(source: Path, raw: str) -> tuple[Path | None, str]:
    if LOCAL_ONLY.match(raw):
        return None, "local-only path"
    path_part, _, fragment = unquote(raw).partition("#")
    target = source if not path_part else (source.parent / path_part).resolve()
    try:
        relative = target.relative_to(ROOT).as_posix()
    except ValueError:
        return None, "path escapes repository"
    if TEMP_PARTS.intersection(Path(path_part).parts):
        return None, "temporary/workspace path"
    exact = relative in TRACKED or any(p.startswith(f"{relative.rstrip('/')}/") for p in TRACKED)
    if not exact:
        folded = [p for p in TRACKED if p.casefold() == relative.casefold()]
        return None, "path case mismatch" if folded else "missing or untracked target"
    return target, fragment


def validate_json_paths(errors: list[str]) -> None:
    config = ROOT / "Design/Criteria/SEMS_Criteria_Config.json"
    data = json.loads(config.read_text(encoding="utf-8"))
    for field in ("source_files", "related_documents"):
        for raw in data.get(field, []):
            target, problem = repository_target(config, raw)
            if target is None:
                errors.append(f"{config.relative_to(ROOT)}: {field}: {raw}: {problem}")

    manifest = ROOT / "Design/UI_UX/screen_manifest.json"
    for item in json.loads(manifest.read_text(encoding="utf-8")):
        raw = item.get("image")
        if not raw:
            errors.append(f"{manifest.relative_to(ROOT)}: {item.get('id')}: missing image")
            continue
        target, problem = repository_target(manifest, raw)
        if target is None:
            errors.append(f"{manifest.relative_to(ROOT)}: {item.get('id')}: {raw}: {problem}")


def validate_openapi_and_traceability(errors: list[str]) -> None:
    openapi_path = ROOT / "Design/API/openapi.yaml"
    openapi = openapi_path.read_text(encoding="utf-8")
    for raw in re.findall(r"^\s*x-documentation-source:\s*(\S+)\s*$", openapi, re.M):
        target, problem = repository_target(openapi_path, raw)
        if target is None:
            errors.append(
                f"{openapi_path.relative_to(ROOT)}: x-documentation-source: "
                f"{raw}: {problem}"
            )
    operations = set(re.findall(r"^\s+operationId:\s*(\w+)\s*$", openapi, re.M))
    components = set(re.findall(r"^    ([A-Za-z0-9_.-]+):\s*$", openapi, re.M))
    for raw in re.findall(r"\$ref:\s*['\"]([^'\"]+)['\"]", openapi):
        if raw.startswith("#/components/") and raw.rsplit("/", 1)[-1] not in components:
            errors.append(f"Design/API/openapi.yaml: unresolved local $ref: {raw}")

    trace = ROOT / "Requirements/SEMS_Traceability_Matrix.md"
    for line_no, line in enumerate(trace.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| TRC-"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        for operation in re.findall(r"`([A-Za-z]\w+)`", cells[6]):
            if operation not in operations:
                errors.append(
                    f"{trace.relative_to(ROOT)}:{line_no}: undefined operationId: {operation}"
                )


def validate_start_index(errors: list[str]) -> None:
    start = ROOT / "START_HERE.md"
    indexed: set[str] = set()
    for raw in LINK.findall(start.read_text(encoding="utf-8")):
        target, problem = repository_target(start, raw)
        if target and not problem:
            relative = target.relative_to(ROOT).as_posix()
            if relative in TRACKED:
                indexed.add(relative)
    for missing in sorted(TRACKED - indexed):
        errors.append(f"START_HERE.md: Complete File Index missing tracked file: {missing}")


def main() -> int:
    errors: list[str] = []
    files = [ROOT / p for p in TRACKED]
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
            target, fragment = repository_target(source, raw)
            if not target:
                errors.append(f"{source.relative_to(ROOT)}: {fragment}: {raw}")
                continue
            if fragment and target.suffix.lower() == ".md":
                fragment = unicodedata.normalize("NFKC", fragment)
                anchor_cache.setdefault(target, anchors(target))
                if fragment not in anchor_cache[target]:
                    errors.append(f"{source.relative_to(ROOT)}: missing anchor: {raw}")

    validate_json_paths(errors)
    validate_openapi_and_traceability(errors)
    validate_start_index(errors)

    for error in errors:
        print(error)
    print(f"checked {len(markdown)} Markdown files; errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
