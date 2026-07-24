# SEMS Traceability Matrix

| Metadata | Value |
|---|---|
| Document ID | `SEMS-TRACE-001` |
| Version | **v0.3** |
| Last Updated | **2026-07-24** |
| Status | **Baseline Candidate — Pending Formal Approval** |

Source order follows Proposal → confirmed decisions → Decision Register → SRS → Stories/AC → Design/API/DB → Tests. `Provisional` means stakeholder confirmation is still required.

| Trace ID | Core Flow / Proposal | Decision | SRS | User Story / AC | Process / State / Permission | API operationId | Database / Constraint | Test Case | Current Status |
|---|---|---|---|---|---|---|---|---|---|
| TRC-001 | Login §5.1 | — | FR-AUT-001..005 | US-AUTH-001 / AC-01..05 | PF-AUTH-001..003 / PM-001 | `startLogin`, `handleLoginCallback` | User, OAuthIdentity, Session / unique provider+subject | AUTH-003..010; SEC-AUTH-002..007 | Mapped |
| TRC-002 | User Management §5.2.1 | — | FR-AUT-007..010 | US-USR-001..003 | PM-003..008 | `listUsers`, `createUser`, `updateUser` | User / unique email, kkuSub | AUTH-011..012 | Mapped |
| TRC-003 | Scholarship Round §5.2 | RD-007, RD-023, RD-048–049 | FR-RND-001..011 | US-RND-001..004 | PF-RND-001 / TR-RND-001..005 / PM-009..010 | `createScholarshipRound`, `setRoundOpen`, `setRoundClose`, `requestRoundReopen`, `decideRoundReopen`, `setRoundArchive` | ScholarshipRound, ReportSnapshot | RND-001..011; CR-012..015 | Confirmed response; approval pending |
| TRC-004 | Import §5.2.2 | RD-017..020 | FR-IMP-001..015 | US-IMP-001..003 | PF-IMP-001..002 / PM-011..014 | `createImport`, `validateImport`, `confirmImport` | ImportBatch, ApplicantRound / transaction + business key | IMP-001..016; IMP-D-001..027 | Mapped; DB key open |
| TRC-005 | Applicant §5.2.3 | RD-015..020, RD-024..029 | FR-APP-001..009 | US-APP-004, US-COR-001 | PF-IMP-001 / PM-015..018 | `listApplicants`, `getApplicant`, `updateApplicant`, `createControlledCorrection` | Applicant, Application / unique round+type+student | CR-001..007 | Confirmed response; approval pending |
| TRC-006 | Documents §5.2.4 | RD-022 | FR-DOC-001..006 | US-DOC-001..002 | PM-019..023 | `uploadApplicantDocument`, `downloadDocument` | ApplicantDocument / private storage key | DOC-001..007; SEC-OWN-007 | Mapped |
| TRC-007 | Criteria §5.2.5 | RD-012..014 | FR-CRI-001..012 | US-CRI-001..003 | PF-CRI-001 | `createCriteriaSet`, `activateCriteriaSet`, `createCriteriaVersion` | CriteriaSet, Criterion / version binding | CRT-001..012 | Confirmed response; formal approval record pending |
| TRC-008 | Applicant Selection §5.2.6 | RD-001..003 | FR-EVA-001..003 | US-SEL-001..002 | PF-EVA-001 / PM-024..026 | `createEvaluation` | Evaluation / evaluator uniqueness + max 3 transaction | SEL-001..005; HR-SEL-001..004 | Mapped |
| TRC-009 | Draft §5.2.7 | RD-004, RD-009 | FR-EVA-004..008 | US-DRF-001..003 | PF-EVA-002 / PM-027..030 | `getEvaluation`, `updateEvaluationDraft`, `cancelEvaluation` | EvaluationStatus DRAFT/CANCELLED | EVA-001..004; SCR-D-009, SCR-D-014 | Mapped |
| TRC-010 | Review | RD-010..014 | FR-EVA-009..011 | US-SUB-001 / AC-01..05 | PF-EVA-002 | `reviewEvaluation` | EvaluationScore / required criteria | EVA-005; SCR-D-004..007 | Mapped |
| TRC-011 | Submit §5.2.8 | RD-004 | FR-EVA-012..016 | US-SUB-002 / AC-01..07 | PF-EVA-002 / PM-031..034 | `submitEvaluation` | EvaluationStatus SUBMITTED / optimistic concurrency | EVA-006..012 | Mapped |
| TRC-012 | Score Calculation §5.2.9 | RD-010..014, RD-047 | FR-SCO-001..015 | US-SCR-001..003 | PF-SCR-001 | `getResultSummary`, `recalculateResultSummary` | EvaluationScore, ResultSummary / Decimal | SCR-001..010; SCR-D-001..016; CR-016..019 | Confirmed response; tests specified |
| TRC-013 | Third Evaluator §5.2.9 | RD-001, RD-005 | FR-SCO-006..008 | US-SCR-003 / AC-01..05 | PF-SCR-002 | `createEvaluation`, `submitEvaluation` | ResultSummary calculationVersion | SEL-010; SCR-005; HR-SCR-002 | Mapped |
| TRC-014 | Close Round §5.2.10 | RD-006..008 | FR-RND-006..008, FR-SCO-009..012 | US-CLS-001..002 | PF-RND-001 / TR-RND-003 | `setRoundClose` | RoundStatus, ApplicantResultStatus | RND-006..007; HR-RND-001..002 | Mapped |
| TRC-015 | Dashboard §5.2.10 | RD-004..007 | FR-DSH-001..003 | US-DSH-001..002 | PM-035 | `getDashboardSummary` | ResultSummary / submitted-only query | DSH-001..005 | Mapped |
| TRC-016 | Report Export §5.2.11 | RD-021..022, RD-031–032, RD-049 | FR-RPT-001..010 | US-RPT-001..003 | PF-RPT-001 / PM-036 | `createReportExport`, `listReportSnapshots`, `downloadReportSnapshot` | ReportExport, ReportSnapshot / immutable final | REP-001..010; CR-020..023 | Confirmed response; approval pending |
| TRC-017 | Audit §5.5 | RD-008, RD-021..022 | FR-AUD-001..004 | Cross-cutting AC | PM audit controls | `listAuditLogs`, `getAuditLog` | AuditLog / append-only, `traceId`, redaction | AUD-001..006; SEC-AUD-001..004 | Mapped; retention open |
| TRC-018 | Account/session isolation | RD-034–037 | FR-AUT-011; NFR-SEC-010 | US-SEC-004 | PM-001..008 | `handleLoginCallback`, `getEvaluation` | User, AuthSession | CR-024..028 | Confirmed response; approval pending |
| TRC-019 | File security | RD-038–039 | FR-DOC-007 | US-SEC-004 | PF-DOC-SCAN | `uploadApplicantDocument`, `getDocumentScanStatus` | ApplicantDocument, DocumentScanStatus | CR-029..031 | Confirmed response; approval pending |
| TRC-020 | Retention/backup/capacity | RD-030–033, RD-040–041 | NFR-RET-001, NFR-BCP-001, NFR-CAP-001 | Operational AC | Architecture operations controls | — | Retention jobs, backup evidence | CR-032..035 | Measurements pending where stated |

## Coverage Statement

- Core/cross-cutting flows mapped: **20/20**
- Mapped flows with at least one linked test specification: **20/20**
- Baseline candidate coverage is complete for changed Release 1 Must requirements. Formal approval and test execution are not claimed.
- This table does not claim every SRS requirement or every AC is fully traced; detailed row-level completion remains a baseline action.

## Decision, Approval and Test Evidence Status

| Scope | Open Decision | Approval Evidence | Test Specification | Test Execution Status |
|---|---|---|---|---|
| Flows TRC-001–TRC-020 | No Release 1 Critical/High business decision remains Open; RD-040/RD-045 measurements remain pending | Pending; no approver name/date or signed baseline evidence recorded | Defined for all 20 mapped flows | Not Yet; no system execution evidence is recorded |

| Lifecycle State | Current Value |
|---|---|
| Test Case Defined | Yes |
| Test Automated | No/Partial |
| Test Executed | Not Yet |
| Test Passed | Not Claimed |
| UAT Accepted | No |

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Documentation Team | Added confirmed-response traceability for application identity, correction/reopen, reporting, account/session isolation, file security, retention, backup and capacity. |
| v0.2 | 2026-07-24 | SEMS Documentation Team | Separated decision/approval evidence and test definition, automation, execution, pass and UAT states without changing 17/17 core-flow coverage. |
| v0.1 | 2026-07-23 | SEMS Documentation Team | Created core-flow traceability matrix with explicit partial/provisional status. |
