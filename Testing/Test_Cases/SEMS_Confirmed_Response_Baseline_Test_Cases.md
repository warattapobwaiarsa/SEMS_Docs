# SEMS Confirmed-Response Baseline Test Cases

| Metadata | Value |
|---|---|
| Version | **v0.2** |
| Last Updated | **2026-07-24** |
| Status | **Test Specification — Not Yet Executed** |
| Source | RD-008–RD-049; SRS Section 12 |

| ID | Requirement / decision | Scenario | Expected result |
|---|---|---|---|
| CR-001 | FR-APP-008 / RD-024 | Same student applies to two scholarship types in one round. | Two UUID applications exist; evaluations/status/result/documents remain independent. |
| CR-002 | FR-APP-008 / RD-025 | Create duplicate same round/type/student triplet. | Conflict/Skip; no second application and no automatic Upsert. |
| CR-003 | FR-RND-009 / RD-023 | Open Draft round with zero applications. | Blocking `NO_APPLICANTS`; state remains Draft. |
| CR-004 | RD-023 | Import new application while round is Open. | Import succeeds after validation. |
| CR-005 | FR-APP-009 / RD-027 | Explicitly update mutable application fields before any Evaluation. | Update and audit succeed; identity triplet unchanged. |
| CR-006 | FR-APP-009 / RD-027 | Normal Import Update after a Draft exists. | Score-affecting update rejected; Controlled Correction required. |
| CR-007 | FR-APP-009 / RD-027 | Apply authorized Controlled Correction after Evaluation exists. | Before/after snapshot, reason, approver and audit persist; affected result recalculates as specified. |
| CR-008 | FR-EVA-018 / RD-009 | Owner cancels Draft with reason. | Soft `CANCELLED`, audit event, slot released atomically; row remains. |
| CR-009 | FR-EVA-017 / RD-008 | Owner requests reopen of Submitted Evaluation and Head/delegate approves. | Prior submission immutable; editable copy returns Draft; technical requester cannot self-approve. |
| CR-010 | FR-EVA-017 / RD-008 | Inspect previous submission after reopen. | Revision/hash/timestamp remain unchanged and readable to authorized Admin. |
| CR-011 | FR-EVA-017 / RD-010 | Resubmit reopened Evaluation. | Only current Submitted totals enter mean; Result Summary recalculates. |
| CR-012 | FR-RND-010 / RD-007 | Close with applications below two Submitted results. | Warning/list shown; explicit confirmation+reason required; affected state `CLOSED_INCOMPLETE` and Final Score null. |
| CR-013 | FR-RND-011 / RD-048 | Approved reopen of Closed round. | Round opens through controlled workflow; audit/reference recorded. |
| CR-014 | FR-RND-011 / RD-048 | Attempt to reopen Archived round. | Rejected `ROUND_ARCHIVED`; no mutation. |
| CR-015 | FR-RND-011 / RD-049 | Create replacement Final report after reopened round closes. | Old immutable report marked Superseded; new Final snapshot inserted; neither overwritten. |
| CR-016 | FR-SCO-015 / RD-013 | Custom Score outside standard options without reason. | Submit rejected `EVALUATION_INCOMPLETE`/validation error. |
| CR-017 | FR-SCO-015 / RD-047 | Custom Amount exceeds round/type ceiling. | Validation error; amount excluded from score. |
| CR-018 | FR-AUT-011 / RD-037 | Evaluator requests another evaluator’s identity. | Denied/omitted; only slot/Submitted/minimum-completion counts returned. |
| CR-019 | FR-AUT-011 / RD-037 | Evaluator requests another evaluator’s scores/comments/amount. | Denied/omitted with no side-channel values. |
| CR-020 | FR-DOC-007 / RD-038 | Upload PDF/JPG/PNG or import above configured limit. | `DOCUMENT_TOO_LARGE`/`IMPORT_FILE_TOO_LARGE`; no usable object. |
| CR-021 | FR-DOC-007 / RD-038 | MIME/signature does not match extension. | Rejected `DOCUMENT_TYPE_UNSUPPORTED`; quarantined bytes unavailable. |
| CR-022 | FR-DOC-007 / RD-039 | Malware scan rejects or scanner unavailable. | Status Rejected/Scan Unavailable; file remains inaccessible and upload not completed. |
| CR-023 | FR-RPT-010 / RD-031–032 | Interim export expires; Final snapshot mutation attempted. | Interim file unavailable after ≤30 days with audit retained; Final update/delete rejected. |
| CR-024 | NFR-SEC-010 / RD-034 | Protected request after 30 minutes idle. | Session rejected and safe expiry UI shown. |
| CR-025 | NFR-SEC-010 / RD-035 | Protected request after eight-hour absolute lifetime. | Session rejected regardless of activity. |
| CR-026 | FR-AUT-011 / RD-036 | KKU user lacks provisioned SEMS account or account becomes inactive. | `USER_NOT_PROVISIONED` or `USER_INACTIVE`; no role/data; inactive denied on next call. |
| CR-027 | FR-AUT-011 / RD-037 | Evaluator reads own Evaluation and progress counts. | Own data plus slot/Submitted/minimum status returned; no peer detail. |
| CR-028 | NFR-SEC-010 / RD-035 | Admin revokes a session. | Next protected request denied. |
| CR-029 | FR-DOC-007 / RD-038 | Upload executable/archive/macro or 11th applicant file. | Rejected before availability. |
| CR-030 | FR-DOC-007 / RD-039 | Clean scan completes. | Authorized short-lived Backend download becomes available; unauthorized user still denied. |
| CR-031 | NFR-SEC-010 / RD-029 | National ID appears in import, UI, API, schema, export, log or test fixture. | Contract/static/runtime check fails; value is not persisted/rendered/emitted. |
| CR-032 | NFR-BCP-001 / RD-041 | Restore latest daily/weekly DB+file backup. | RPO ≤24h and RTO ≤8 business hours demonstrated; FK/key/version/report/audit reconciliation passes. |
| CR-033 | FR-RPT-010 / RD-049 | Reconcile DB Submitted totals to report detail/summary. | 10 Embedded Point total, 2–3 equal-weight mean and rounded summary exactly match DB. |
| CR-034 | NFR-RET-001 / RD-030–033 | Retention job reaches expiry with/without Legal Hold. | Eligible artifact securely deleted; held artifact retained; audit evidence recorded. |
| CR-035 | NFR-CAP-001 / RD-040 | Load test design targets including concurrent selection. | Target results recorded as measurements; no fourth active Evaluation; no estimate mislabeled as observed. |

Execution evidence, pass/fail status, defects and UAT sign-off must be recorded separately; this catalog does not claim execution.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.1 | 2026-07-24 | SEMS QA Team | Added baseline-candidate tests for confirmed stakeholder rules. |
