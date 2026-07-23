# SEMS Documentation Review Report

| Metadata | Value |
|---|---|
| Document ID | `SEMS-DOC-REVIEW-001` |
| Version | **v0.2** |
| Last Updated | **2026-07-23** |
| Status | **Draft — Pending Stakeholder Review** |
| Review Scope | Requirements, Design, API/OpenAPI, Database, UI/UX, Testing, Deployment, binary reference files and repository indexes |

## Executive Summary

Repository ได้รับการ reconcile สำหรับ pre-baseline แล้ว: เอกสารใหม่เชื่อมจาก index, version mismatch หลักได้รับการแก้, User Stories ใช้ consolidated source พร้อม stable anchors, error contract/code เป็นมาตรฐานเดียว, round/import/scoring rules ตรงกันในเอกสารที่เกี่ยวข้อง และ core traceability มี test link ครบ 17/17 flows

**ยังไม่พร้อม Freeze/Approve** เพราะพบไฟล์ที่อาจมี PII จริง, Open Decisions ด้านคะแนน/ฐานข้อมูล/การเปิดรอบยังไม่อนุมัติ และยังไม่ได้ผลจาก independent OpenAPI 3.1 validator ในเครื่องนี้

## Critical

### C-01 Potential real PII in public repository — Open

ห้าม Push/Public ต่อจนเจ้าของข้อมูลยืนยันและอนุมัติ remediation:

| File | Location | Finding |
|---|---|---|
| `README.md` | lines 23–24 | ชื่อบุคคลและรหัสนักศึกษา |
| `Requirements/Proposal/SEMS-project-proposal.md` | lines 34–35 | ชื่อผู้จัดทำและรหัสนักศึกษา |
| `Requirements/Proposal/SEMS-project-proposal.pdf` | page 1 | ชื่อผู้จัดทำและรหัสนักศึกษา; ตรวจภาพยืนยันแล้ว |
| `Design/Criteria/Criteria.xlsx` | `Assessment!A2,E2,B3`; `Sheet3!B4:B8`; `Data!B3:B7,I4,L3:L7` | รูปแบบรหัสนักศึกษา เลขบัตรประชาชน และอีเมลใน workbook; ต้องให้เจ้าของข้อมูลยืนยันว่าเป็นจริงหรือ synthetic |

ไม่ได้ลบหรือแก้ไฟล์ต้นฉบับตามข้อห้ามของงานนี้ ข้อเสนอ: หยุดเผยแพร่ไฟล์, จำกัดสิทธิ์, ทำสำเนาสำรองที่ควบคุมการเข้าถึง และแทน public copy ด้วย synthetic names/IDs/national ID/phone/email/address/coordinates/income/financial/family data หลังได้รับอนุญาต

## High

- **H-01 OpenAPI independent validation pending:** structural audit พบ 60 operations, 60 unique `operationId`, ทุก endpoint มี `x-roles`, และทุก mutation มี CSRF + audit metadata; แต่การรัน Redocly ในเครื่องถูกบล็อกเพราะ external package execution ไม่ได้รับอนุมัติ จึงห้ามระบุว่า OpenAPI ผ่าน 3.1 validator จน CI/ผู้ใช้รัน workflow สำเร็จ
- **H-02 Database Freeze Blockers open:** RD-024–RD-029 ยังไม่มีข้อสรุป; schema คง Draft
- **H-03 Scoring rule provisional:** EMBEDDED_POINT, 5–100, arithmetic mean, third evaluator recalculation, Decimal/HALF_UP ยังรอ Scholarship Office approval
- **H-04 Round opening provisional:** Applicant ≥1 เป็น Blocking Error ชั่วคราวตาม RD-023; งานทุนต้องเลือกระหว่าง Blocking กับ Warning
- **H-05 PII examples requiring classification:** Data Dictionary/import-mapping workbooksและ Markdown มีรูปแบบ ID/phone/email ที่ดูเป็นตัวอย่าง (`student@example.com`/เลขทดสอบ) แต่ต้องให้ Data Owner ยืนยันว่า synthetic ก่อน Public release

## Medium

- Deployment ยังไม่มี setup/operations/user manuals; มีเพียง architecture considerations
- Mermaid diagrams ใช้ syntax ที่ GitHub รองรับ แต่ยังไม่มี local automated Mermaid parser ในผลรอบนี้
- Full row-level traceability ของ SRS/AC ทั้งหมดไม่ครบ; matrix ปัจจุบันครอบคลุม core flows เท่านั้น
- UI overview แสดง placeholder applicant data; visual review ไม่พบข้อมูลที่ยืนยันว่าเป็นบุคคลจริง แต่ต้องยืนยันแหล่ง synthetic data

## Low

- ชื่อ `README.md` ซ้ำตามโครงสร้างโฟลเดอร์เป็นเรื่องปกติ; automated check ตรวจ case-colliding relative path แทนการห้าม basename `README.md`
- เวอร์ชัน pre-baseline เดิมมีทั้ง v0.x/v1.x/v2.x; policy ใหม่รักษาประวัติเดิมและห้ามใช้เลขเวอร์ชันเป็นหลักฐานอนุมัติ

## Fixed

- Decision Register index mismatch: document/index/tree ใช้ v1.2 ตรงกัน
- Documentation Policy รองรับ `v0.x` Working Draft/Pre-baseline และสงวน v1.0 สำหรับ First Approved/Official Release
- User Stories index เปลี่ยนจากไฟล์ที่ไม่มีจริงเป็น stable section anchors; traceability ใช้ไฟล์กลางไม่คัดลอกซ้ำ
- Error response เป็น `{code,message,details[],traceId,timestamp}` และ OpenAPI ใช้ schema กลาง
- Canonical aliases: `DUPLICATE_EVALUATION`, `EVALUATOR_LIMIT_REACHED`, `EVALUATION_NOT_OWNER`
- Round state baseline เป็น `DRAFT → OPEN → CLOSED → ARCHIVED`; ไม่มี `DRAFT → ARCHIVED`; controlled reopen เป็น Provisional; Archived read-only
- Release 1 import รับ `.xlsx`/`.csv`; `.xls` เป็น Optional / Out of Scope
- Scoring test range แก้เป็น 5–100; เพิ่ม embedded-point, min/max, 2/3 evaluator, rounding, exclusion, recalculation and version-binding reference cases
- Functional Test Catalog เพิ่ม `Linked Requirement` และ `Linked Decision`
- Database document เพิ่ม Database Freeze Blockers
- เพิ่ม PRD, System Architecture, approval/meeting templates, error catalog, traceability matrix, scoring reference data และ documentation workflow/scripts

## Pending Stakeholder Decision

1. RD-023: ไม่มี Applicant ก่อนเปิดรอบเป็น Blocking หรือ Warning
2. RD-024: ผู้สมัครหนึ่งคนสมัครหลายประเภททุนในรอบเดียวได้หรือไม่
3. RD-025: Business Key รวม `scholarship_type_id` หรือไม่
4. RD-026: Loan/Scholarship History เป็น Applicant-level หรือ per-round snapshot
5. RD-027: Duplicate Applicant update fields ใดได้และถึงจุดใด
6. RD-028: Required fields ขั้นสุดท้าย
7. RD-029: ความจำเป็น/ฐานกฎหมาย/retention/access ของเลขบัตรประชาชน
8. RD-008–RD-014: Reopen, scoring formula, HALF_UP, criteria/custom score rules
9. KKU claims/client registration/redirect/logout, session timeout, retention, rate/file limits
10. Export fields/template, snapshot/as-of policy และ report retention

## Validation Results

| Check | Before | After / Current Result |
|---|---|---|
| Broken relative file paths | 0 | 0 after final script run |
| Broken internal anchors | 10 converted Data Dictionary anchor mismatches found by strict checker | 0 after stable anchors |
| Index references to nonexistent User Story files | 14 conceptual file references | 0; replaced by stable sections |
| Version consistency | Decision Register v1.1 vs indexes v1.0 plus changed-document drift | Automated version check: 0 errors after reconciliation |
| JSON | Not recorded | Tracked JSON 2/2 files parse successfully |
| YAML/OpenAPI syntax | Existing file readable | Structural checks pass; Redocly 3.1 result **Pending** |
| OpenAPI metadata | Not recorded | 60/60 operations have unique operationId/roles; all mutations have CSRF and audit metadata |
| Secret pattern review | Not recorded | No committed credential value detected; placeholders/references only |
| PII review | Not recorded | Critical potential PII locations listed above; no source binary modified |

## Traceability and Test Coverage

- Core flow traceability: **17/17 mapped**
- Core flows linked to at least one test: **17/17**
- Required P0 scenarios present across Functional/High-Risk/Import/Scoring/Security suites: login state/nonce/token/inactive, role denial, duplicate/fourth/concurrent/double-click selection, Draft/Cancelled exclusion, second/third submit, complete/incomplete close, invalid/orphan/duplicate/rollback import, document IDOR, criteria version mismatch, DB report reconciliation, embedded-point regression and secret-in-log
- Baseline traceability completeness: **Partial**, not “Complete,” until every Must requirement/AC has executable evidence and all provisional decisions are resolved

## Files Added

- `DOCUMENTATION_REVIEW_REPORT.md`
- `.github/workflows/documentation-check.yml`
- `scripts/check-documentation-links.py`
- `scripts/check-document-versions.py`
- `Requirements/PRD/SEMS-PRD.md`
- `Requirements/SEMS_Traceability_Matrix.md`
- `Requirements/Approvals/Requirement_Baseline_Approval_Record.md`
- `Requirements/Approvals/System_Design_Approval_Record.md`
- `Requirements/Meeting_Notes/README.md`
- `Requirements/Meeting_Notes/MEETING_NOTE_TEMPLATE.md`
- `Design/Architecture/SEMS_System_Architecture.md`
- `Design/API/SEMS_Error_Code_Catalog.md`
- `Testing/Test_Data/SEMS_Scoring_Reference_Cases.md`

## Files Modified

Root/index/governance: `.gitignore`, `README.md`, `START_HERE.md`, `REPOSITORY_TREE.md`, `DOCUMENTATION_POLICY.md`; Requirements: README, SRS, Decision Register, User Stories index/consolidated document; Design: README, API spec/OpenAPI/endpoint matrix, state/permission, scoring, database/data-dictionary indexes, import mapping, UI/UX index/spec/UAT; Testing: README, master plan, functional/high-risk/scoring test documents; Deployment README

## Files Moved or Deleted

**None.** Source files and binary references were preserved; no branch, push or merge was performed.

## Recommendations Before Requirement Baseline Approval

1. Resolve C-01 and record Data Owner authorization/remediation evidence.
2. Answer RD-023–RD-029 and RD-008–RD-014; update Decision Register without inventing approver/date.
3. Run documentation workflow, require Redocly success and attach output.
4. Expand traceability from core-flow level to every Must SRS/AC and attach test execution evidence.
5. Complete UAT and use the pending approval template only after evidence exists.

## Recommendations Before System Design Approval

1. Freeze business key, history scope, required fields and national-ID decision before schema/migration approval.
2. Confirm KKU integration, session/CSRF, object authorization, storage, retention, backup RPO/RTO and observability/SLO.
3. Validate OpenAPI 3.1 independently; review excessive data exposure and object-level authorization responses.
4. Approve scoring/reference dataset and prove DB/UI/API/export reconciliation.
5. Complete deployment/operations/security/restore runbooks and threat/security review.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 2026-07-23 | SEMS Documentation Team | Initial pre-baseline repository reconciliation report; open findings and pending approvals retained. |
| v0.2 | 2026-07-23 | SEMS Documentation Team | Record final link/version/JSON/table checks, generated-cache exclusion, and independent OpenAPI validator limitation. |
