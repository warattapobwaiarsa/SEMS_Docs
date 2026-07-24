#!/usr/bin/env python3
"""Check repository links, document navigation, indexes and supporting metadata."""

from pathlib import Path, PurePath
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
LOCAL_ANYWHERE = re.compile(r"(?:file://|(?<![A-Za-z0-9])[A-Za-z]:[\\/])", re.I)
TEMP_PARTS = {"tmp", ".tmp-sheet-inspect", ".agents", ".obsidian"}
NAV_START = "<!-- DOC_NAV_START -->"
NAV_END = "<!-- DOC_NAV_END -->"
NAV_CONFIG = ROOT / "scripts/document-navigation.json"
TRACKED = set(
    subprocess.check_output(
        ["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8"
    ).splitlines()
)
KNOWN = TRACKED | {"scripts/document-navigation.json"}


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


def without_fenced_code(text: str) -> str:
    return re.sub(r"^```.*?^```\s*$", "", text, flags=re.M | re.S)


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
    exact = relative in KNOWN or any(p.startswith(f"{relative.rstrip('/')}/") for p in KNOWN)
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


def validate_navigation(markdown: list[Path], errors: list[str]) -> None:
    try:
        config = json.loads(NAV_CONFIG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"scripts/document-navigation.json: cannot load navigation map: {exc}")
        return

    documents = config.get("documents")
    exemptions = config.get("exemptions")
    if not isinstance(documents, dict) or not isinstance(exemptions, dict):
        errors.append(
            "scripts/document-navigation.json: documents and exemptions must be objects"
        )
        return

    markdown_paths = {path.relative_to(ROOT).as_posix() for path in markdown}
    configured = set(documents)
    for missing in sorted(markdown_paths - configured):
        errors.append(f"{missing}: missing from scripts/document-navigation.json")
    for extra in sorted(configured - markdown_paths):
        errors.append(
            f"scripts/document-navigation.json: untracked Markdown document: {extra}"
        )
    for path, reason in exemptions.items():
        if path not in documents or not isinstance(reason, str) or not reason.strip():
            errors.append(
                f"scripts/document-navigation.json: exemption requires a document and reason: {path}"
            )

    titles = {}
    for source in markdown:
        relative = source.relative_to(ROOT).as_posix()
        text = source.read_text(encoding="utf-8")
        title = HEADING.search(text)
        titles[relative] = title.group(1) if title else relative
        if text.count(NAV_START) != 1 or text.count(NAV_END) != 1:
            errors.append(f"{relative}: navigation markers must appear exactly once")
            continue
        start = text.index(NAV_START)
        end = text.index(NAV_END, start) + len(NAV_END)
        if text[end:].strip():
            errors.append(f"{relative}: navigation block must be the final content")
        nav = text[start:end]
        entry = documents.get(relative, {})
        if not isinstance(entry, dict):
            errors.append(f"{relative}: navigation entry must be an object")
            continue
        exemptions_for_file = set(entry.get("exemptions", []))
        if "breadcrumb" not in exemptions_for_file and " › " not in text[:start]:
            errors.append(f"{relative}: missing breadcrumb")

        resolved_links = set()
        for raw in LINK.findall(nav):
            target, problem = repository_target(source, raw)
            if not target:
                errors.append(f"{relative}: navigation link {raw}: {problem}")
                continue
            resolved_links.add(target.relative_to(ROOT).as_posix())

        for field in ("section_index", "home"):
            target = entry.get(field)
            if target and target not in resolved_links:
                errors.append(f"{relative}: navigation block missing {field}: {target}")
        for field in ("previous", "next"):
            target = entry.get(field)
            if target == relative:
                errors.append(f"{relative}: {field} must not link to itself")
            elif target and target not in resolved_links:
                errors.append(f"{relative}: navigation block missing {field}: {target}")
        action = entry.get("next_action")
        if action:
            if "ขั้นตอนถัดไป" not in nav:
                errors.append(f"{relative}: next action label is missing")
            for target in action.get("targets", []):
                if target not in resolved_links:
                    errors.append(
                        f"{relative}: navigation block missing next action target: {target}"
                    )

    for path, entry in documents.items():
        if not isinstance(entry, dict):
            continue
        next_path = entry.get("next")
        if next_path:
            peer = documents.get(next_path, {})
            if peer.get("previous") != path:
                errors.append(
                    f"{path}: next is {next_path}, but its previous is "
                    f"{peer.get('previous')!r}"
                )
        previous = entry.get("previous")
        if previous:
            peer = documents.get(previous, {})
            action_targets = peer.get("next_action", {}).get("targets", [])
            if peer.get("next") != path and path not in action_targets:
                errors.append(
                    f"{path}: previous is {previous}, but its next is "
                    f"{peer.get('next')!r}"
                )

    numbered_sets = (
        "Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping",
        "Design/Database/SEMS_Data_Dictionary",
    )
    for directory in numbered_sets:
        sequence = sorted(
            path
            for path in markdown_paths
            if path.startswith(f"{directory}/")
            and re.match(r"^\d{2}_", PurePath(path).name)
        )
        for previous, current in zip(sequence, sequence[1:]):
            if documents.get(previous, {}).get("next") != current:
                errors.append(
                    f"{previous}: numbered sequence must continue to {current}"
                )
            if documents.get(current, {}).get("previous") != previous:
                errors.append(
                    f"{current}: numbered sequence must return to {previous}"
                )

    for path in sorted(markdown_paths):
        if path.endswith("/README.md"):
            text = (ROOT / path).read_text(encoding="utf-8")
            if "## ลำดับการอ่านที่แนะนำ" not in text:
                errors.append(f"{path}: missing recommended reading order")

    action_documents = {
        path
        for path in markdown_paths
        if re.search(
            r"(?i)(?:Approval_Record|MEETING_NOTE_TEMPLATE|Checklist)\.md$", path
        )
    }
    for path in sorted(action_documents):
        if not documents.get(path, {}).get("next_action"):
            errors.append(f"{path}: template/checklist requires a next action")


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
        if LOCAL_ANYWHERE.search(text):
            errors.append(f"{source.relative_to(ROOT)}: local-only path in content")
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.rstrip() != line:
                errors.append(f"{source.relative_to(ROOT)}:{line_no}: trailing whitespace")
        for raw in LINK.findall(without_fenced_code(text)):
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
    validate_navigation(markdown, errors)

    for error in errors:
        print(error)
    print(f"checked {len(markdown)} Markdown files; errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
