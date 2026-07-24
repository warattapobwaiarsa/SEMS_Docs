# SEMS Product Requirements Document

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-PRD-001` |
| Version | **v0.2** |
| Last Updated | **2026-07-24** |
| Status | **Baseline Candidate — Pending Formal Approval** |
| Owner | SEMS Product Owner / Scholarship Office |

## Problem Statement

กระบวนการประเมินทุนกระจายอยู่ในหลายไฟล์และหลายระบบ ทำให้ข้อมูลซ้ำ การตรวจเอกสารและคะแนนไม่ต่อเนื่อง การคำนวณ/รายงานผิดพลาดได้ และตรวจสอบย้อนหลังยาก

## Product Goals

- รวมข้อมูลผู้สมัคร เอกสาร เกณฑ์ การประเมิน คะแนน และรายงานในระบบเดียว
- บังคับใช้สิทธิ์และสถานะงานจาก Backend พร้อม Audit
- ลดงานคำนวณและรวมผลด้วยมือ โดยผลลัพธ์ตรวจสอบย้อนกลับได้
- รองรับผู้ประเมินไม่ซ้ำ 2–3 คนและคำนวณใหม่เมื่อคนที่ 3 Submit

## Users

| User | Need |
|---|---|
| Admin / Scholarship Officer | จัดการผู้ใช้ รอบทุน Import เอกสาร เกณฑ์ ปิดรอบ Dashboard Export และ Audit |
| Evaluator | เลือกผู้สมัคร ดูข้อมูลที่ได้รับสิทธิ์ บันทึก Draft Review และ Submit เฉพาะของตน |

## Scope

### Core Features

KKU OAuth/OIDC, SEMS account/RBAC, scholarship round, applicant import `.xlsx`/`.csv`, applicant/document management, versioned criteria, evaluator selection, Draft/Review/Submit, scoring summary, third-evaluator recalculation, close/archive, dashboard, Excel/CSV export และ audit trail

### Controlled Release 1 Features

- Evaluation reopen with request, independent approval, immutable prior revision and resubmission
- Exceptional `CLOSED → OPEN` round reopen; `ARCHIVED` is never reopened
- Controlled Correction after any Evaluation exists
- Immutable final report snapshots with `Superseded` replacement history
- Account pre-provisioning, evaluator isolation, code-list administration and file quarantine/malware scanning

### Out of Scope

การจัดการรหัสผ่าน KKU, การจ่ายเงินทุน, mobile native app, การแทนระบบทะเบียนกลาง และ national ID ทุกกรณีใน Release 1 Core Flow. National ID is `Out of Scope for Release 1 — requires separate lawful-need and security approval`.

## Success Metrics

Capacity design targets are recorded in RD-040, but are not measured facts. The current manual-process baseline and the proposed 50% improvement target remain `Confirmed Direction — Pending Measurement` under RD-045. Measure import success, evaluation time, reconciliation errors, authorization incidents, audit completeness, preparation/merge time, correction time, report time, staff count and rework.

## Constraints

- Proposal ที่ได้รับอนุมัติเป็น Source of Truth สูงสุด
- Next.js, NestJS, PostgreSQL และ Prisma ตามข้อเสนอ/แบบร่างสถาปัตยกรรม
- ข้อมูลส่วนบุคคลต้องใช้เท่าที่จำเป็น แยกสิทธิ์ และไม่รั่วผ่าน Error/Log/Export
- Confirmed stakeholder responses are the working decision source; formal baseline approval is still pending.

## Dependencies

KKU OAuth/OIDC registration และ claims, PostgreSQL, file/object storage, deployment environment, backup/restore, เจ้าหน้าที่งานทุนผู้มีอำนาจตัดสินใจ และชุดข้อมูลสังเคราะห์สำหรับทดสอบ

## Risks

| Risk | Mitigation |
|---|---|
| Formal baseline evidence absent | Keep approval pending and use the Decision Register as the baseline candidate |
| PII ในไฟล์อ้างอิง | จำกัดการเข้าถึง ตรวจ source และแทนด้วย synthetic data เมื่อได้รับอนุญาต |
| เลือกผู้ประเมินพร้อมกันเกิน 3 | Transaction, unique constraint/lock และ concurrency test |
| Criteria เปลี่ยนย้อนหลัง | Version binding และ immutable referenced version |
| Export ไม่ตรงฐานข้อมูล | Snapshot/as-of, reconciliation และ audit |

## Remaining external records and measurements

No Release 1 Critical/High decision remains Open. Formal approver names, approval dates, signatures/evidence, operational assignees, production endpoints/claims and the RD-040/RD-045 measurements remain external follow-up items; see the [Decision Register](../SEMS_Requirement_Decision_Register.md) and [Traceability Matrix](../SEMS_Traceability_Matrix.md).

## Milestones

1. Baseline candidate review and formal approval
2. Requirement Baseline Approval
3. System Design Review / Approval
4. Implementation และ integration testing
5. UAT / security / data migration rehearsal
6. Release readiness และ production approval

## Requirement Baseline Status

**Ready for Formal Review; Pending Formal Approval** — confirmed responses are synchronized, but no verifiable approver/date/signature evidence exists.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2026-07-24 | SEMS Documentation Team | Synchronized confirmed Release 1 decisions, scope, measurements and baseline readiness without asserting approval. |
| v0.1 | 2026-07-23 | SEMS Documentation Team | Initial pre-baseline PRD compiled from repository sources; no stakeholder approval asserted. |
