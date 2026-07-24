"""Fail when the SEMS prototype contains an enabled button with no valid action."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROTOTYPE = ROOT / "Design" / "UI_UX" / "SEMS_Wireframe_Prototype.html"
MANIFEST = ROOT / "Design" / "UI_UX" / "screen_manifest.json"


class PrototypeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.screens = set()
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        element_id = values.get("id", "")
        if tag == "section" and element_id.startswith("screen-"):
            self.screens.add(element_id.removeprefix("screen-"))
        if tag == "button":
            self.buttons.append(values)


def main():
    source = PROTOTYPE.read_text(encoding="utf-8")
    parser = PrototypeParser()
    parser.feed(source)
    actions = set(re.findall(r"^\s*'([^']+)':", source, re.MULTILINE))
    errors = []

    for number, button in enumerate(parser.buttons, 1):
        if "disabled" in button:
            continue
        destination = button.get("data-go")
        action = button.get("data-action")
        if destination and destination not in parser.screens:
            errors.append(f"button {number}: missing screen '{destination}'")
        elif action and action not in actions:
            errors.append(f"button {number}: missing action '{action}'")
        elif not destination and not action:
            errors.append(f"button {number}: no data-go or data-action")

    tracked = set(
        subprocess.check_output(
            ["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8"
        ).splitlines()
    )
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest_ids = {item["id"] for item in manifest}
    if manifest_ids != parser.screens:
        errors.append(
            f"screen manifest mismatch: manifest={sorted(manifest_ids)} "
            f"prototype={sorted(parser.screens)}"
        )
    for item in manifest:
        image = item.get("image")
        target = f"Design/UI_UX/{image}" if image else ""
        if not image or target not in tracked:
            errors.append(f"screen '{item['id']}': missing or untracked image '{image}'")

    assert not errors, "\n".join(errors)
    print(
        f"OK: {len(parser.screens)} screens, {len(parser.buttons)} buttons, "
        f"{len(actions)} actions, {len(manifest)} manifest images"
    )


if __name__ == "__main__":
    main()
