# SEMS Product Requirements Document

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-PRD-001` |
| Version | **v0.4** |
| Last Updated | **2026-07-24** |
| Status | **Baseline Candidate — Pending Formal Approval** |
| Owner | SEMS Product Owner / Scholarship Office |

## ปัญหาที่ต้องแก้ไข (Problem Statement)

กระบวนการประเมินทุนกระจายอยู่ในหลายไฟล์และหลายระบบ ทำให้ข้อมูลซ้ำ การตรวจเอกสารและคะแนนไม่ต่อเนื่อง การคำนวณ/รายงานผิดพลาดได้ และตรวจสอบย้อนหลังยาก

## เป้าหมายผลิตภัณฑ์ (Product Goals)

- รวมข้อมูลผู้สมัคร เอกสาร เกณฑ์ การประเมิน คะแนน และรายงานในระบบเดียว
- บังคับใช้สิทธิ์และสถานะงานจาก Backend พร้อม Audit
- ลดงานคำนวณและรวมผลด้วยมือ โดยผลลัพธ์ตรวจสอบย้อนกลับได้
- รองรับผู้ประเมินไม่ซ้ำ 2–3 คนและคำนวณใหม่เมื่อคนที่ 3 Submit

## ผู้ใช้งาน (Users)

| ผู้ใช้ | ความต้องการ |
|---|---|
| ผู้ดูแลระบบ (`ADMIN`) / เจ้าหน้าที่งานทุน | จัดการผู้ใช้ รอบทุน การนำเข้าข้อมูล เอกสาร เกณฑ์ การปิดรอบ Dashboard การส่งออกรายงาน และ Audit |
| ผู้ประเมิน (`EVALUATOR`) | เลือกผู้สมัคร ดูข้อมูลที่ได้รับสิทธิ์ บันทึก `DRAFT` ตรวจทาน และส่งผล (`SUBMITTED`) เฉพาะของตน |

## ขอบเขต (Scope)

### ความสามารถหลัก (Core Features)

ครอบคลุม KKU OAuth/OIDC, บัญชี SEMS และ RBAC, รอบทุน, การนำเข้าผู้สมัครจาก `.xlsx`/`.csv`, การจัดการผู้สมัครและเอกสาร, เวอร์ชันเกณฑ์, การเลือกผู้ประเมิน, `DRAFT`/Review/`SUBMITTED`, ผลสรุปคะแนน, การคำนวณใหม่เมื่อมีผู้ประเมินคนที่ 3, การปิด/จัดเก็บรอบ, Dashboard, การส่งออก Excel/CSV และ Audit Trail

### ความสามารถแบบควบคุมใน Release 1

- การ Reopen Evaluation ต้องมีคำขอ การอนุมัติที่เป็นอิสระ การเก็บ revision เดิมแบบ immutable และการส่งผลใหม่
- การ Reopen รอบแบบยกเว้นจาก `CLOSED → OPEN`; รอบ `ARCHIVED` ห้ามเปิดใหม่
- ใช้ Controlled Correction หลังมี Evaluation แล้ว
- เก็บ final report snapshot แบบ immutable พร้อมประวัติการแทนที่ `Superseded`
- รองรับ account pre-provisioning, การแยกข้อมูลผู้ประเมิน, การจัดการ code list และการ Quarantine/สแกน malware

### นอกขอบเขต (Out of Scope)

ไม่รวมการจัดการรหัสผ่าน KKU, การจ่ายเงินทุน, mobile native app, การแทนระบบทะเบียนกลาง และ National ID ทุกกรณีใน Release 1 Core Flow โดย National ID มีสถานะ `Out of Scope for Release 1 — requires separate lawful-need and security approval`

## ตัวชี้วัดความสำเร็จ (Success Metrics)

เป้าหมายด้าน capacity บันทึกไว้ใน RD-040 แต่ยังไม่ใช่ผลการวัดจริง ส่วน baseline ของกระบวนการ manual และเป้าหมายปรับปรุง 50% ยังเป็น `Confirmed Direction — Pending Measurement` ตาม RD-045 การวัดต้องครอบคลุมความสำเร็จของ Import, เวลาประเมิน, reconciliation error, authorization incident, ความครบถ้วนของ Audit, เวลาเตรียม/รวมข้อมูล, เวลาแก้ไข, เวลาสร้างรายงาน, จำนวนเจ้าหน้าที่ และ rework

## ข้อจำกัด (Constraints)

- Proposal ที่ได้รับอนุมัติเป็น Source of Truth สูงสุด
- Next.js, NestJS, PostgreSQL และ Prisma ตามข้อเสนอ/แบบร่างสถาปัตยกรรม
- ข้อมูลส่วนบุคคลต้องใช้เท่าที่จำเป็น แยกสิทธิ์ และไม่รั่วผ่าน Error/Log/Export
- คำตอบที่ยืนยันจากผู้มีส่วนเกี่ยวข้องเป็นแหล่งตัดสินใจสำหรับ working baseline แต่ยังรอการอนุมัติ baseline อย่างเป็นทางการ

## สิ่งที่ต้องพึ่งพา (Dependencies)

KKU OAuth/OIDC registration และ claims, PostgreSQL, file/object storage, deployment environment, backup/restore, เจ้าหน้าที่งานทุนผู้มีอำนาจตัดสินใจ และชุดข้อมูลสังเคราะห์สำหรับทดสอบ

## ความเสี่ยง (Risks)

| ความเสี่ยง | การลดความเสี่ยง |
|---|---|
| ยังไม่มีหลักฐานอนุมัติ baseline อย่างเป็นทางการ | คงสถานะ Pending และใช้ Decision Register เป็น baseline candidate |
| PII ในไฟล์อ้างอิง | จำกัดการเข้าถึง ตรวจ source และแทนด้วย synthetic data เมื่อได้รับอนุญาต |
| เลือกผู้ประเมินพร้อมกันเกิน 3 | Transaction, unique constraint/lock และ concurrency test |
| Criteria เปลี่ยนย้อนหลัง | Version binding และ immutable referenced version |
| Export ไม่ตรงฐานข้อมูล | Snapshot/as-of, reconciliation และ audit |

## บันทึกและผลการวัดจากภายนอกที่ยังต้องจัดหา

ไม่มี decision ระดับ Critical/High ของ Release 1 ที่ยังเป็น Open รายการที่ต้องติดตามจากภายนอก ได้แก่ ชื่อผู้อนุมัติ วันที่อนุมัติ ลายเซ็น/หลักฐาน ผู้รับผิดชอบงานปฏิบัติการ production endpoints/claims และผลการวัด RD-040/RD-045 ดูรายละเอียดใน [Decision Register](../SEMS_Requirement_Decision_Register.md) และ [Traceability Matrix](../SEMS_Traceability_Matrix.md)

## หมุดหมายโครงการ (Milestones)

1. ตรวจทาน baseline candidate และอนุมัติอย่างเป็นทางการ
2. อนุมัติ Requirement Baseline
3. ตรวจทานและอนุมัติ System Design
4. ดำเนินการ Implementation และ integration testing
5. ทำ UAT, security testing และ data migration rehearsal
6. ตรวจความพร้อม Release และอนุมัติ production

## สถานะ Requirement Baseline

**Ready for Formal Review; Pending Formal Approval** — ซิงก์คำตอบที่ยืนยันแล้ว แต่ยังไม่มีหลักฐานชื่อผู้อนุมัติ วันที่ หรือลายเซ็นที่ตรวจสอบได้

## Related Documents

- Next: [Requirement Decision Analysis](../SEMS_Requirement_Decision_Analysis.md) and [Requirement Decision Register](../SEMS_Requirement_Decision_Register.md)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.4 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.3 | 2026-07-24 | SEMS Documentation Team | Added explicit lifecycle navigation to requirement decision analysis and registration. |
| v0.2 | 2026-07-24 | SEMS Documentation Team | Synchronized confirmed Release 1 decisions, scope, measurements and baseline readiness without asserting approval. |
| v0.1 | 2026-07-23 | SEMS Documentation Team | Initial pre-baseline PRD compiled from repository sources; no stakeholder approval asserted. |
