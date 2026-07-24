#!/usr/bin/env python3
"""Compare Markdown document versions with linked indexes and repository tree."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "tmp", ".tmp-sheet-inspect"}
VERSION = re.compile(
    r"(?:^version:\s*[\"']?v?|\|\s*(?:(?:Current|Template) )?Version\s*\|\s*\**v?)(\d+\.\d+)",
    re.I | re.M,
)
LINK_VERSION = re.compile(r"\[[^\]]+]\(([^)#]+)\)[^|\n]*\|\s*(v\d+\.\d+)", re.I)
TREE_VERSION = re.compile(r"([A-Za-z0-9_.-]+\.(?:md|yaml|csv|json))\s+\[(v\d+\.\d+)", re.I)
LINE_LINK = re.compile(r"\[[^\]]+]\(([^)#]+)(?:#[^)]*)?\)")
STATUS = re.compile(
    r"(?:^status:\s*[\"']?([^\"'\n]+)|^\|\s*(?:Document )?Status\s*\|\s*\**(.*?)\**\s*\|)",
    re.I | re.M,
)
STATUS_EXPECTATIONS = {
    "Requirements/SRS/SEMS-SRS.md": (
        "Baseline Candidate - Pending Formal Approval",
        "Requirements/README.md",
        "Baseline Candidate — Pending Formal Approval",
    ),
    "Requirements/Meeting_Notes/MEETING_NOTE_TEMPLATE.md": (
        "Template",
        "Requirements/Meeting_Notes/README.md",
        "Template",
    ),
    "Design/Architecture/SEMS_State_Transition_Specification.md": (
        "Confirmed Response — Pending Formal Approval",
        "Design/README.md",
        "Confirmed Response — Pending Formal Approval",
    ),
    "Design/Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md": (
        "Confirmed Response — Pending Formal Approval",
        "Design/README.md",
        "Confirmed Response — Pending Formal Approval",
    ),
    "Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md": (
        "Baseline Candidate — Pending Formal Approval",
        "Design/README.md",
        "Baseline Candidate — Pending Formal Approval",
    ),
    "Design/Database/SEMS_ER_Prisma_Data_Dictionary.md": (
        "Draft — Pre-Implementation Review",
        "Design/README.md",
        "Draft — Pre-Implementation Review",
    ),
    "Design/UI_UX/SEMS_Wireframe_Specification.md": (
        "Draft — User Validation",
        "Design/UI_UX/README.md",
        "Draft — User Validation",
    ),
}


def own_version(path: Path) -> str | None:
    match = VERSION.search(path.read_text(encoding="utf-8")[:3000])
    return f"v{match.group(1)}" if match else None


def own_status(path: Path) -> str | None:
    match = STATUS.search(path.read_text(encoding="utf-8")[:3000])
    if not match:
        return None
    return next(value.strip() for value in match.groups() if value)


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

        for line_no, line in enumerate(text.splitlines(), 1):
            links = list(LINE_LINK.finditer(line))
            for position, link in enumerate(links):
                target = (index.parent / link.group(1)).resolve()
                actual = versions.get(target)
                if not actual:
                    continue
                end = links[position + 1].start() if position + 1 < len(links) else len(line)
                stated = re.search(r"\bv\d+\.\d+\b", line[link.end() : end], re.I)
                if stated and stated.group(0).lower() != actual.lower():
                    errors.append(
                        f"{index.relative_to(ROOT)}:{line_no}: {link.group(1)} "
                        f"states {stated.group(0)}, document is {actual}"
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

    ui_index = ROOT / "Design/UI_UX/README.md"
    ui_version = own_version(ui_index)
    tree_text = tree.read_text(encoding="utf-8")
    ui_tree = re.search(
        r"│   ├── UI_UX/.*?│   │   ├── README\.md \[(v\d+\.\d+)",
        tree_text,
        re.S,
    )
    if ui_tree and ui_tree.group(1) != ui_version:
        errors.append(
            f"REPOSITORY_TREE.md: Design/UI_UX/README.md states "
            f"{ui_tree.group(1)}, document is {ui_version}"
        )

    for raw, (expected_source, index_raw, expected_index) in STATUS_EXPECTATIONS.items():
        source = ROOT / raw
        actual = own_status(source)
        if actual != expected_source:
            errors.append(f"{raw}: status is {actual!r}, expected {expected_source!r}")
        index = ROOT / index_raw
        matching = [
            line
            for line in index.read_text(encoding="utf-8").splitlines()
            if source.name in line
        ]
        if not any(expected_index in line for line in matching):
            errors.append(
                f"{index_raw}: {raw} must state status {expected_index!r}"
            )

    for error in errors:
        print(error)
    print(f"checked {len(docs)} versioned Markdown documents; errors={len(errors)}")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
