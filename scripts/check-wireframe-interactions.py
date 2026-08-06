"""Check SEMS prototype routes, Phase 3.6 state guards, and manifest mapping."""

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
        self.forms = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        element_id = values.get("id", "")
        if tag == "section" and element_id.startswith("screen-"):
            self.screens.add(element_id.removeprefix("screen-"))
        if tag == "button":
            self.buttons.append(values)
        if tag == "form" and element_id:
            self.forms.add(element_id)


def main():
    source = PROTOTYPE.read_text(encoding="utf-8")
    parser = PrototypeParser()
    parser.feed(source)
    actions = set(re.findall(r"^\s*'([^']+)':", source, re.MULTILINE))
    errors = []

    for number, tag in enumerate(re.findall(r"<button\b[^>]*>", source), 1):
        if not re.search(r"\btype\s*=", tag):
            errors.append(f"source button {number}: missing explicit type")
    source_actions = set(re.findall(r'data-action="([^"]+)"', source))
    for action in sorted(source_actions - actions):
        errors.append(f"source action '{action}': missing handler")

    for number, button in enumerate(parser.buttons, 1):
        if not button.get("type"):
            errors.append(f"button {number}: missing explicit type")
        if "disabled" in button:
            continue
        if button.get("data-action") == "prototype":
            errors.append(
                f"button {number}: enabled placeholder action '{button['data-action']}'"
            )
            continue
        if button.get("type") == "submit":
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
        required = {
            "id",
            "title",
            "role",
            "route",
            "summary_item",
            "requirement_reference",
            "moscow",
            "prototype_status",
            "coverage_scope",
            "feature_coverage",
            "coverage_note",
        }
        missing = required - item.keys()
        if missing:
            errors.append(f"screen '{item.get('id')}': missing manifest fields {sorted(missing)}")
        if item.get("route") != f"#{item.get('id')}":
            errors.append(f"screen '{item.get('id')}': route must match screen id")
        if item.get("coverage_scope") != "screen-level":
            errors.append(f"screen '{item.get('id')}': coverage_scope must be screen-level")
        image = item.get("image")
        target = f"Design/UI_UX/{image}" if image else None
        if image and target not in tracked:
            errors.append(f"screen '{item['id']}': missing or untracked image '{image}'")
        if not image and item.get("image_status") != "Deferred to Phase 6":
            errors.append(f"screen '{item['id']}': missing image or Phase 6 deferral")

    for required_text in (
        "routeRoles",
        "resetDemo",
        "showPermissionDenied",
        "clearTemporaryUi",
        "$('#demoRole').value=role",
        "console.assert($('#demoRole').value===role",
        "$('#demoRole').value=DEFAULT_ROLE",
        "toast.textContent=''",
        "event.target.value=demoState.currentRole||DEFAULT_ROLE",
        "function hasActiveDemoAuthorization(requiredRole)",
        "authenticationState==='AUTHENTICATED'",
        "sessionState==='ACTIVE'",
        "currentRole===requiredRole",
    ):
        if required_text not in source:
            errors.append(f"prototype state/guard missing '{required_text}'")

    if "addUserForm" not in parser.forms or "submitAddUser()" not in source:
        errors.append("add-user form or prevented submit handler missing")
    if re.search(r"'prototype':", source):
        errors.append("generic placeholder/toast-only action handler remains enabled in source")
    for label, pattern in {
        "ADMIN login sync": r"'login-admin':\(\)=>login\('ADMIN'\)",
        "EVALUATOR login sync": r"'login-evaluator':\(\)=>login\('EVALUATOR'\)",
        "login cleanup": r"function login\(role\)\{[^}]*clearTemporaryUi",
        "logout cleanup": r"function logout\([^)]*\)\{clearTemporaryUi",
        "reset cleanup": r"function resetDemo\(\)\{clearTemporaryUi",
        "session cleanup": r"function showSessionExpired\(\)\{clearTemporaryUi",
        "permission cleanup": r"function showPermissionDenied\([^)]*\)\{clearTemporaryUi",
        "role-switch cleanup": r"event\.target\.id==='demoRole'.*?clearTemporaryUi",
    }.items():
        if not re.search(pattern, source, re.S):
            errors.append(f"prototype stabilization missing {label}")

    required_phase3_forms = {
        "roundForm",
        "editApplicantForm",
        "documentUploadForm",
        "criteriaForm",
    }
    missing_forms = required_phase3_forms - parser.forms
    if missing_forms:
        errors.append(f"Phase 3 semantic forms missing {sorted(missing_forms)}")

    for label, required_text in {
        "round readiness": "function roundReadiness(",
        "guarded round open": "'request-open-round'",
        "required mapping validation": "function validateMappings(",
        "transactional import": "function commitImport(",
        "applicant/application render": "function renderApplicantDetail(",
        "document security render": "function renderDocuments(",
        "criteria validation": "function validateCriteria(",
        "scenario fixtures": "function applyScenario(",
        "cross-flow criteria readiness": "round.criteriaId=demoState.criteriaState.id",
        "shared import commit guard": "function validateImportCommitEligibility(",
        "Application document context": "selectedApplicationId",
        "guarded document detail": "document.security!=='CLEAN'",
        "Criteria edit buffer": "editBuffer",
        "deterministic scenario base": "const next=freshState()",
        "Item 11 boundary": "function enforcePhase35Boundaries(",
    }.items():
        if required_text not in source:
            errors.append(f"Phase 3 interaction missing {label}")

    if re.search(r"Phase 3 · Item [3-6]|จะดำเนินการใน Phase 3", source):
        errors.append("stale enabled/disabled Phase 3 placeholder text remains for Item 3–6")
    if re.search(r"'(?:show-close-round|close-round|create-round|open-round)':", source):
        errors.append("out-of-scope or legacy round action handler remains")

    for label, pattern in {
        "commitImport calls shared guard": r"function commitImport\(\)\{[^}]*validateImportCommitEligibility",
        "request import calls shared guard": r"'request-import':\(\)=>\{[^}]*validateImportCommitEligibility",
        "confirm import calls shared guard": r"'confirm-import':\(\)=>\{[^}]*validateImportCommitEligibility",
        "empty dataset guard": r"!dataset\.rows\.length\)issues\.push\('EMPTY_FILE'\)",
        "unsupported dataset guard": r"UNSUPPORTED_FILE_TYPE",
        "blocking error guard": r"rows\.some\(row=>row\.status==='ERROR'\)",
        "failed dataset guard": r"SIMULATED_IMPORT_FAILURE",
        "Criteria input edits buffer": r"const item=state\.editBuffer\[",
        "Criteria Save commits buffer": r"state\.items=clone\(state\.editBuffer\)",
        "Criteria Activate blocks buffer": r"state\.editorOpen\|\|state\.dirty\|\|state\.editBuffer",
        "scenario selected before login": r"phase3Scenarios\.includes\(scenario\).*?applyScenario\(scenario\)",
        "direct export route guard": r"if\(id==='export'\)",
        "import authentication invariant": r"function validateImportCommitEligibility\([^)]*\)\{.*?hasActiveDemoAuthorization\('ADMIN'\)",
        "round confirm authentication invariant": r"'confirm-open-round':\(\)=>\{if\(!hasActiveDemoAuthorization\('ADMIN'\)\)",
        "applicant save authentication invariant": r"function submitApplicantEdit\(\)\{if\(!hasActiveDemoAuthorization\('ADMIN'\)\)",
        "document upload authentication invariant": r"function submitDocumentUpload\(\)\{if\(!hasActiveDemoAuthorization\('ADMIN'\)\)",
        "Criteria save authentication invariant": r"function saveCriteriaDraft\(\)\{if\(!hasActiveDemoAuthorization\('ADMIN'\)\)",
        "Criteria activation authentication invariant": r"'confirm-activate-criteria':\(\)=>\{if\(!hasActiveDemoAuthorization\('ADMIN'\)\)",
    }.items():
        if not re.search(pattern, source, re.S):
            errors.append(f"Phase 3.6 guard missing {label}")

    if "applicant.documents" in source:
        errors.append("Applicant-level document collection remains in Business Flow")
    if "application.documents" not in source:
        errors.append("Application-level document collection missing")
    if not re.search(r'<label[^>]+for="roundSearch"', source):
        errors.append("roundSearch accessible label missing")
    if not re.search(r'<label[^>]+for="roundStatus"', source):
        errors.append("roundStatus accessible label missing")
    if not re.search(r'<select[^>]+id="documentSample"[^>]+aria-describedby="documentUploadError"', source):
        errors.append("documentSample error description missing")
    if "Clickable Prototype v1.4 · Phase 3.6" not in source:
        errors.append("Phase 3.6 prototype badge missing")
    export_handler = re.search(r"'export-report':([^\n]+)", source)
    if not export_handler or "download(" in export_handler.group(1) or "exportState.status=" in export_handler.group(1):
        errors.append("Item 11 export handler is not safely guarded")

    phase3_items = {3, 4, 5, 6}
    for item in phase3_items:
        mapped = [entry for entry in manifest if item in entry.get("summary_item", [])]
        if not mapped:
            errors.append(f"Summary Item {item}: no manifest screen mapping")
        if any(entry.get("feature_coverage") == "complete" for entry in mapped):
            errors.append(f"Summary Item {item}: complete claimed before browser verification")
        if not any(entry.get("feature_coverage") == "partial" for entry in mapped):
            errors.append(f"Summary Item {item}: partial static evidence missing")

    assert not errors, "\n".join(errors)
    print(
        f"OK: {len(parser.screens)} screens, {len(parser.buttons)} buttons, "
        f"{len(actions)} actions, {len(manifest)} manifest images"
    )


if __name__ == "__main__":
    main()
