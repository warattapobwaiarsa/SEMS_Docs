# SEMS Product Requirements Document

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-PRD-001` |
| Version | **v0.1** |
| Last Updated | **2026-07-23** |
| Status | **Draft — Pending Stakeholder Approval** |
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

### Optional Features

- `.xls` import (Out of Scope for Release 1)
- Controlled reopen ของรอบ `CLOSED → OPEN` (Provisional)
- Reopen ผล Submitted ตามผู้อนุมัติและเงื่อนไขที่ต้องยืนยัน

### Out of Scope

การจัดการรหัสผ่าน KKU, การจ่ายเงินทุน, mobile native app, การแทนระบบทะเบียนกลาง และการเก็บเลขบัตรประชาชนโดยไม่มีฐานกฎหมาย/ความจำเป็นที่ยืนยันแล้ว

## Success Metrics

ค่าตัวเลขเป้าหมายยังเป็น **Open Decision**; ตัวชี้วัดที่ต้องกำหนด ได้แก่อัตรา Import สำเร็จ เวลาประเมินต่อผู้สมัคร ความคลาดเคลื่อนรายงาน จำนวน incident ด้านสิทธิ์ และความครบถ้วนของ Audit

## Constraints

- Proposal ที่ได้รับอนุมัติเป็น Source of Truth สูงสุด
- Next.js, NestJS, PostgreSQL และ Prisma ตามข้อเสนอ/แบบร่างสถาปัตยกรรม
- ข้อมูลส่วนบุคคลต้องใช้เท่าที่จำเป็น แยกสิทธิ์ และไม่รั่วผ่าน Error/Log/Export
- กฎคะแนนในปัจจุบันเป็น **Draft Provisional**

## Dependencies

KKU OAuth/OIDC registration และ claims, PostgreSQL, file/object storage, deployment environment, backup/restore, เจ้าหน้าที่งานทุนผู้มีอำนาจตัดสินใจ และชุดข้อมูลสังเคราะห์สำหรับทดสอบ

## Risks

| Risk | Mitigation |
|---|---|
| Requirement/สูตรคะแนนยังไม่อนุมัติ | คง Provisional, ใช้ decision register และห้าม freeze |
| PII ในไฟล์อ้างอิง | จำกัดการเข้าถึง ตรวจ source และแทนด้วย synthetic data เมื่อได้รับอนุญาต |
| เลือกผู้ประเมินพร้อมกันเกิน 3 | Transaction, unique constraint/lock และ concurrency test |
| Criteria เปลี่ยนย้อนหลัง | Version binding และ immutable referenced version |
| Export ไม่ตรงฐานข้อมูล | Snapshot/as-of, reconciliation และ audit |

## Open Decisions

ดู [Requirement Decision Register](../SEMS_Requirement_Decision_Register.md) และ [Traceability Matrix](../SEMS_Traceability_Matrix.md) โดยเฉพาะสูตรคะแนน การเปิดรอบโดยไม่มีผู้สมัคร Database Freeze Blockers, Reopen, KKU claims, retention และ export fields

## Milestones

1. Requirement reconciliation และ Open Decision review
2. Requirement Baseline Approval
3. System Design Review / Approval
4. Implementation และ integration testing
5. UAT / security / data migration rehearsal
6. Release readiness และ production approval

## Requirement Baseline Status

**Not Ready for Approval** — ยังมี Provisional/Open Decisions, PII remediation และ trace/test gaps ที่ระบุใน `DOCUMENTATION_REVIEW_REPORT.md`

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.1 | 2026-07-23 | SEMS Documentation Team | Initial pre-baseline PRD compiled from repository sources; no stakeholder approval asserted. |
