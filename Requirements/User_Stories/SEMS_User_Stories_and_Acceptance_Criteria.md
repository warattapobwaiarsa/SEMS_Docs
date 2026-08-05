---
document_id: SEMS-US-INDEX
title: "SEMS User Stories and Acceptance Criteria — Index"
version: "v0.7"
status: "Baseline Candidate — Pending Formal Approval"
last_updated: 2026-08-05
owner: SEMS Project Team
author: SEMS Requirements Team
source_sections: "Proposal 5.1–5.5; Requirement Decision Register; Import Mapping; KKU OAuth Summary"
---
# SEMS — User Stories และ Acceptance Criteria

[START HERE](../../START_HERE.md) › [SEMS User Stories](./README.md) › SEMS — User Stories และ Acceptance Criteria

เอกสารชุดนี้แปลงขอบเขตของ **Scholarship Evaluation Management System (SEMS)** ให้เป็น User Story ที่สามารถนำไปวาง Backlog, ออกแบบหน้าจอ/API และสร้าง Test Case ได้โดยตรง

## ขอบเขตเอกสาร

| โมดูล | Section | Story IDs |
|---|---|---|
| Login และสิทธิ์ | [01 Login and Access](#login-and-access) | `US-AUTH-*` |
| จัดการผู้ใช้ | [02 User Management](#user-management) | `US-USR-*` |
| จัดการรอบทุน | [03 Scholarship Round](#scholarship-round) | `US-RND-*` |
| Import ผู้สมัคร | [04 Applicant Import](#applicant-import) | `US-IMP-*` |
| เอกสารผู้สมัคร | [05 Applicant Documents](#applicant-documents) | `US-DOC-*` |
| เกณฑ์คะแนน | [06 Criteria Management](#criteria-management) | `US-CRI-*` |
| เลือกผู้สมัคร | [07 Applicant Selection](#applicant-selection) | `US-SEL-*` |
| บันทึก Draft | [08 Evaluation Draft](#evaluation-draft) | `US-DRF-*` |
| Review และ Submit | [09 Review and Submit](#review-and-submit) | `US-SUB-*` |
| คำนวณคะแนน | [10 Score Calculation](#score-calculation) | `US-SCR-*` |
| ปิดรอบทุน | [11 Close Round](#close-round) | `US-CLS-*` |
| Dashboard | [12 Dashboard](#dashboard) | `US-DSH-*` |
| Export รายงาน | [13 Report Export](#report-export) | `US-RPT-*` |
| Traceability | [Traceability Matrix](../SEMS_Traceability_Matrix.md) | Story → Requirement/Decision/Test |

## รูปแบบ Acceptance Criteria

Acceptance Criteria ใช้โครงสร้าง **Given / When / Then** และมีรหัสคงที่ เช่น `US-SEL-002-AC-04` เพื่อให้ทีม QA อ้างอิงใน Test Case ได้โดยไม่ต้องคัดลอกข้อความ Story ทั้งหมด

## กฎกลางที่ใช้กับทุก Story

1. Backend ต้องตรวจสิทธิ์ซ้ำทุกครั้ง ไม่พึ่งการซ่อนเมนูที่ Frontend เพียงอย่างเดียว
2. การดำเนินการที่เปลี่ยนข้อมูลสำคัญต้องบันทึกผู้ดำเนินการ วันเวลา รายการอ้างอิง และผลลัพธ์ลง Audit Log
3. ระบบต้องไม่บันทึกรหัสผ่าน KKU Account, Access Token, Refresh Token, Session Secret หรือข้อมูลลับลง Audit Log
4. เวลาในหน้าจอและรายงานใช้เขตเวลา `Asia/Bangkok`; เวลาในฐานข้อมูลควรจัดเก็บแบบ timezone-aware
5. API Error Response ต้องใช้ `{code, message, details[], traceId, timestamp}` โดยไม่มี object `error` ครอบ และ `code` ต้องเป็นค่าคงที่จาก Error Code Catalog
6. ข้อมูลผู้สมัครและเอกสารต้องจำกัดตามบทบาท รอบทุน และความเป็นเจ้าของ Evaluation
7. การคำนวณและ Visualization ด้านคะแนนใช้เฉพาะ Evaluation สถานะ `SUBMITTED` ที่ยังไม่ถูกยกเลิก
8. Confirmed responses may define the baseline candidate; formal approval evidence is still required before Freeze/Approved status.

## Definition of Ready

Story พร้อมเข้าสู่ Sprint เมื่อ Actor, Preconditions, Acceptance Criteria, ข้อมูลที่ต้องใช้, Error Case และ Open Decision ระดับ Critical ได้รับการยืนยันแล้ว

## Definition of Done

Story ถือว่าเสร็จเมื่อ:

- Code Review ผ่านและรวมเข้า Branch หลักตาม Workflow ของทีม
- Unit/Integration/E2E Test ที่เกี่ยวข้องผ่าน
- Acceptance Criteria ทุกข้อมี Test Case หรือหลักฐานการทดสอบ
- RBAC, Validation, Error Handling และ Audit Event ที่เกี่ยวข้องได้รับการทดสอบ
- ไม่มี Critical Defect ที่ขัดขวาง Core Flow
- เอกสาร API, Data Model หรือคู่มือได้รับการปรับปรุงเมื่อ Story ทำให้พฤติกรรมระบบเปลี่ยน

## Confirmed decisions that govern this story set

| Decision | ประเด็น | Story ที่ได้รับผลกระทบ |
|---|---|---|
| RD-008 | Reopen หลัง Submit | `US-SUB-003`, `US-SCR-*` |
| RD-009 | การยกเลิก Draft และคืนช่องผู้ประเมิน | `US-SEL-003` |
| RD-010 | สูตรคะแนนสรุป | `US-SCR-001`, `US-SCR-002`, `US-SCR-003` |
| RD-011 | หลักการปัดเศษ | `US-SCR-*`, `US-RPT-*` |
| RD-012–014 | โครงสร้างและช่วงคะแนนของเกณฑ์ | `US-CRI-*`, `US-DRF-*` |
| RD-015 | Business Key ผู้สมัคร | `US-IMP-*` |
| RD-018 | นโยบาย Duplicate/Update ตอน Import | `US-IMP-002`, `US-IMP-003` |
| RD-019–020 | Required Fields และรูปแบบ Legacy | `US-IMP-*` |
| RD-021–022 | Report Template และสิทธิ์ Export | `US-RPT-*` |

## แหล่งอ้างอิงหลัก

- [`SEMS-project-proposal.pdf`](../Proposal/SEMS-project-proposal.pdf)
- [`SEMS_Requirement_Decision_Analysis.md`](../SEMS_Requirement_Decision_Analysis.md)
- [`SEMS_Applicant_Import_Mapping_Specification.md`](../../Design/Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md)
- `SEMS_Data_Dictionary.xlsx`
- [`Criteria.xlsx`](../../Design/Criteria/Criteria.xlsx)
- `kku-oauth-summary.md`


## Confirmed-response Release 1 stories

### US-APP-004 — Multiple scholarship applications

- **Given** student `S1` already has an application for type `T1` in round `R1`, **when** Admin imports type `T2`, **then** a separate application is created.
- **Given** `(R1,T1,S1)` already exists, **when** the same triplet is imported, **then** default action is Skip and automatic Upsert never occurs.

### US-COR-001 — Controlled Correction

- **Given** no Evaluation exists, **when** Admin explicitly updates mutable data, **then** the update succeeds without changing student, round or type.
- **Given** any Draft/Submitted Evaluation exists, **when** score-affecting data changes, **then** normal update is rejected and Controlled Correction requires authorization, reason, before/after snapshot and audit.

### US-EVA-010 — Reopen and cancel

- **Given** an owned Submitted Evaluation before round close, **when** owner/staff submits a reasoned request and an independent Head/delegate approves, **then** prior submission becomes an immutable revision and editable work returns to Draft.
- **Given** a reopened Evaluation is resubmitted, **then** the Result Summary recalculates from current Submitted totals.
- **Given** an owned Draft, **when** evaluator cancels with reason, **then** state is Cancelled, the row remains, an audit event is written and the slot is released atomically.

### US-RND-004 — Controlled close and reopen

- **Given** incomplete applications, **when** Admin closes, **then** the UI warns, lists them, requires explicit confirmation/reason, marks them `CLOSED_INCOMPLETE` and produces no Final Score.
- **Given** a Closed round, **when** an approved exceptional reopen occurs, **then** the old Final report is immutable and Superseded.
- **Given** an Archived round, **when** reopen is attempted, **then** access is denied.

### US-RPT-003 — Report profiles and snapshots

- **Given** authorized Admin, **when** exporting, **then** Excel has Summary/Evaluator Detail and CSV has two files (optionally ZIP), using `INTERNAL_FULL` or `SUMMARY_MASKED`.
- **Given** an evaluator, **when** requesting another evaluator’s identity, scores, comments or amount recommendation, **then** the system returns no restricted data.
- **Given** an interim export older than 30 days, **then** its file is unavailable while audit metadata remains.
- **Given** a Final snapshot, **when** overwrite/delete is attempted, **then** the mutation is rejected.

### US-SEC-004 — Account, session and file safety

- **Given** a KKU user without a pre-provisioned SEMS account, **when** login completes, **then** `USER_NOT_PROVISIONED` is shown and no role is granted.
- **Given** 30 minutes idle or 8 hours absolute lifetime, **when** the next protected action occurs, **then** the session expires with a safe message.
- **Given** an inactive SEMS account, **when** the next API request occurs, **then** access is denied.
- **Given** an invalid/oversize/MIME-mismatched file, **then** upload is rejected; otherwise production content remains Quarantined until malware scan passes.

### US-DAT-005 — Release 1 data minimization

- **Given** import, UI, API, database, export, log or test data, **when** national ID is encountered, **then** it is rejected/not persisted/not rendered and the check fails.
- **Given** round/type Criteria configuration adds `required_before_evaluation`, **when** data is missing, **then** Evaluation creation is blocked without a source-code change.

<div style="page-break-after: always;"></div>

<a id="login-and-access"></a>
# 01 — Login และการควบคุมการเข้าถึง

## US-AUTH-001 — เข้าสู่ระบบด้วย KKU Account
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ / อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะผู้ใช้งาน SEMS ฉันต้องการเข้าสู่ระบบด้วย KKU Account เพื่อใช้งานระบบโดยไม่ต้องมีรหัสผ่านแยกสำหรับ SEMS

**คุณค่าทางธุรกิจ:** ลดความเสี่ยงจากการจัดการรหัสผ่านเองและใช้ตัวตนของมหาวิทยาลัยเป็นแหล่งยืนยันตัวตนกลาง

### Preconditions

- ผู้ใช้ยังไม่มี SEMS Session ที่ใช้งานได้
- Application ได้รับการลงทะเบียนกับ KKU OAuth/OIDC และมี Redirect URI ที่ถูกต้อง

### Acceptance Criteria

#### US-AUTH-001-AC-01

- **Given (กำหนดให้):** ผู้ใช้เปิดหน้า SEMS โดยยังไม่ได้เข้าสู่ระบบ
- **When (เมื่อ):** ผู้ใช้เลือก “เข้าสู่ระบบด้วย KKU Account”
- **Then (ระบบต้อง):** ระบบต้องสร้าง `state`, `nonce` และ PKCE `code_challenge` แล้ว Redirect ไปยัง KKU Authorization Endpoint โดยไม่แสดงหรือรับรหัสผ่าน KKU ใน SEMS
#### US-AUTH-001-AC-02

- **Given (กำหนดให้):** KKU SSO ส่ง Authorization Code กลับมายัง Callback URI
- **When (เมื่อ):** SEMS ประมวลผล Callback
- **Then (ระบบต้อง):** ระบบต้องตรวจสอบ `state`, แลก Code ด้วย PKCE `code_verifier`, ตรวจสอบ ID Token/Claims และยืนยันตัวตนสำเร็จก่อนสร้าง Session
#### US-AUTH-001-AC-03

- **Given (กำหนดให้):** ตัวตน KKU ถูกต้องและมีบัญชี SEMS สถานะ `Active`
- **When (เมื่อ):** Callback ผ่านการตรวจสอบทั้งหมด
- **Then (ระบบต้อง):** ระบบต้องสร้าง Session ที่ปลอดภัย ผูกกับผู้ใช้และบทบาท แล้วนำผู้ใช้ไปยังหน้าเริ่มต้นตามบทบาท
#### US-AUTH-001-AC-04

- **Given (กำหนดให้):** ตัวตน KKU ถูกต้องแต่ไม่มีบัญชี SEMS หรือบัญชีเป็น `Inactive`
- **When (เมื่อ):** ระบบตรวจ Authorization ภายใน SEMS
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธการเข้าใช้ ไม่สร้าง Session ที่ใช้งานได้ แสดงข้อความว่าไม่ได้รับอนุญาต และบันทึก Audit Event
#### US-AUTH-001-AC-05

- **Given (กำหนดให้):** Callback มี `state`/`nonce` ไม่ตรง Token ไม่ผ่านการตรวจสอบ หรือ KKU SSO ตอบข้อผิดพลาด
- **When (เมื่อ):** ระบบตรวจพบความผิดปกติ
- **Then (ระบบต้อง):** ระบบต้องยุติ Login Flow ไม่สร้าง Session ลบข้อมูลชั่วคราวของ Flow และแสดงข้อความทั่วไปที่ไม่เปิดเผยข้อมูลลับ

### Notes / Open Decisions

- ควรใช้ OIDC Discovery และ JWKS แทนการ Hardcode Endpoint/Signing Key
- Permanent Identity Claim ที่ใช้เชื่อม KKU Identity กับ SEMS User ต้องยืนยันกับหน่วยงาน KKU SSO

---

## US-AUTH-002 — เข้าถึงเมนูและข้อมูลตามบทบาท
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ / อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะผู้ใช้งานที่เข้าสู่ระบบแล้ว ฉันต้องการเห็นและใช้เฉพาะเมนู ข้อมูล และการดำเนินการที่บทบาทของฉันอนุญาต

**คุณค่าทางธุรกิจ:** ป้องกันการเปิดเผยข้อมูลผู้สมัครและการแก้ไขข้อมูลนอกหน้าที่

### Preconditions

- ผู้ใช้มี Session ที่ตรวจสอบแล้ว
- บัญชี SEMS ยังเป็น Active และมีบทบาทอย่างน้อยหนึ่งบทบาท

### Acceptance Criteria

#### US-AUTH-002-AC-01

- **Given (กำหนดให้):** ผู้ใช้บทบาท Evaluator เข้าสู่ระบบ
- **When (เมื่อ):** ระบบสร้างเมนูและตอบ API
- **Then (ระบบต้อง):** ระบบต้องไม่แสดงหรือส่งสิทธิ์จัดการผู้ใช้ รอบทุน Import เกณฑ์รวม หรือ Export รายงานรวม
#### US-AUTH-002-AC-02

- **Given (กำหนดให้):** Evaluator เรียกข้อมูลรายละเอียดหรือเอกสารของผู้สมัคร
- **When (เมื่อ):** Evaluator ยังไม่มี Evaluation ที่ใช้งานอยู่สำหรับผู้สมัครรายนั้น
- **Then (ระบบต้อง):** Backend ต้องปฏิเสธข้อมูลละเอียดอ่อนและอนุญาตเพียงข้อมูลขั้นต่ำสำหรับค้นหา/เลือกตามที่กำหนด
#### US-AUTH-002-AC-03

- **Given (กำหนดให้):** Evaluator มี Evaluation ของตนเอง
- **When (เมื่อ):** เปิด แก้ไข บันทึก หรือ Submit
- **Then (ระบบต้อง):** ระบบต้องอนุญาตเฉพาะ Evaluation ที่มี `evaluator_user_id` ตรงกับผู้ใช้และอยู่ในรอบที่อนุญาต
#### US-AUTH-002-AC-04

- **Given (กำหนดให้):** ผู้ใช้เรียกหน้า/API ที่ไม่มีสิทธิ์โดยตรง
- **When (เมื่อ):** Backend ตรวจ Permission ไม่ผ่าน
- **Then (ระบบต้อง):** ระบบต้องตอบ `403 Forbidden` พร้อม error code คงที่ ไม่ส่งข้อมูล Resource และบันทึก `ACCESS_DENIED`
#### US-AUTH-002-AC-05

- **Given (กำหนดให้):** Admin เข้าถึงฟังก์ชันบริหาร
- **When (เมื่อ):** ระบบตรวจบทบาท Admin และบัญชี Active
- **Then (ระบบต้อง):** ระบบต้องอนุญาตตาม Permission Matrix แต่ยังต้องบังคับกฎสถานะรอบทุนและกฎความถูกต้องของข้อมูล

---

## US-AUTH-003 — ออกจากระบบ
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ / อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะผู้ใช้งาน ฉันต้องการออกจากระบบเพื่อยุติการเข้าถึง SEMS บนอุปกรณ์ที่กำลังใช้งาน

**คุณค่าทางธุรกิจ:** ลดความเสี่ยงจาก Session ค้างบนอุปกรณ์ส่วนกลางหรืออุปกรณ์ที่ผู้อื่นเข้าถึงได้

### Preconditions

- ผู้ใช้มี SEMS Session ที่ใช้งานอยู่

### Acceptance Criteria

#### US-AUTH-003-AC-01

- **Given (กำหนดให้):** ผู้ใช้เลือกออกจากระบบ
- **When (เมื่อ):** ระบบรับคำขอ Logout
- **Then (ระบบต้อง):** ระบบต้องยกเลิก SEMS Session/Refresh Token ที่เกี่ยวข้องก่อน Redirect ผู้ใช้
#### US-AUTH-003-AC-02

- **Given (กำหนดให้):** การยกเลิก Session สำเร็จ
- **When (เมื่อ):** ผู้ใช้กลับไปยัง URL ที่ต้อง Login
- **Then (ระบบต้อง):** ระบบต้องไม่ยอมรับ Session เดิมและต้องเริ่ม Authentication Flow ใหม่
#### US-AUTH-003-AC-03

- **Given (กำหนดให้):** ระบบใช้ KKU OIDC Logout
- **When (เมื่อ):** สร้าง Logout URL
- **Then (ระบบต้อง):** ระบบต้องใช้ Redirect URI ที่ลงทะเบียนและไม่แนบข้อมูลลับใน URL
#### US-AUTH-003-AC-04

- **Given (กำหนดให้):** Logout Endpoint ของ KKU ไม่พร้อมใช้งาน
- **When (เมื่อ):** SEMS ยกเลิก Session ภายในสำเร็จแล้ว
- **Then (ระบบต้อง):** ผู้ใช้ต้องถูกออกจาก SEMS อย่างน้อย และระบบต้องแสดงสถานะที่ไม่ทำให้เข้าใจผิดว่าออกจากทุกบริการของ KKU แล้ว

### Notes / Open Decisions

- Default logout ends the SEMS application session; optional full KKU logout is shown only when KKU supports it and the user explicitly confirms.

---



<div style="page-break-after: always;"></div>

<a id="user-management"></a>
# 02 — จัดการผู้ใช้งาน

## US-USR-001 — ค้นหาและดูบัญชี SEMS
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการค้นหาและดูบัญชี SEMS เพื่อทราบว่าใครได้รับสิทธิ์ บทบาทใด และอยู่ในสถานะใด

**คุณค่าทางธุรกิจ:** ช่วยควบคุมสิทธิ์ก่อนเปิดรอบทุนและตรวจสอบผู้ประเมินที่พร้อมใช้งาน

### Preconditions

- ผู้ใช้เข้าสู่ระบบด้วยบทบาท Admin

### Acceptance Criteria

#### US-USR-001-AC-01

- **Given (กำหนดให้):** Admin เปิดหน้าจัดการผู้ใช้
- **When (เมื่อ):** ระบบโหลดรายการ
- **Then (ระบบต้อง):** ระบบต้องแสดงชื่อ ตัวระบุ KKU ที่อนุญาตให้แสดง อีเมล/หน่วยงานตาม Claim ที่ได้รับ บทบาท สถานะ และเวลาปรับปรุงล่าสุด
#### US-USR-001-AC-02

- **Given (กำหนดให้):** มีผู้ใช้จำนวนมาก
- **When (เมื่อ):** Admin ค้นหาด้วยชื่อ อีเมล หรือตัวระบุที่อนุญาต
- **Then (ระบบต้อง):** ระบบต้องคืนเฉพาะรายการที่ตรงเงื่อนไขและรองรับ Pagination
#### US-USR-001-AC-03

- **Given (กำหนดให้):** ผู้ใช้ทั่วไปหรือ Evaluator เปิด URL/API จัดการผู้ใช้
- **When (เมื่อ):** ระบบตรวจสิทธิ์
- **Then (ระบบต้อง):** ต้องปฏิเสธด้วย `403` และไม่เปิดเผยรายชื่อผู้ใช้

---

## US-USR-002 — เชื่อม KKU Identity และกำหนดบทบาท
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการเชื่อมตัวตน KKU เข้ากับบัญชี SEMS และกำหนดบทบาท เพื่ออนุญาตให้บุคลากรใช้ระบบตามหน้าที่

**คุณค่าทางธุรกิจ:** ทำให้ Authentication แยกจาก Authorization และไม่ต้องจัดการรหัสผ่านใน SEMS

### Preconditions

- Admin ได้รับข้อมูลตัวตน KKU ที่ผ่านช่องทางอนุมัติ
- บทบาทเป้าหมายมีอยู่ใน Permission Matrix

### Acceptance Criteria

#### US-USR-002-AC-01

- **Given (กำหนดให้):** Admin ระบุตัวตน KKU ที่ยังไม่ถูกเชื่อม
- **When (เมื่อ):** บันทึกบัญชี SEMS
- **Then (ระบบต้อง):** ระบบต้องสร้างบัญชีโดยเก็บเฉพาะ Claim ที่จำเป็น บทบาท สถานะ และข้อมูล Audit โดยไม่สร้าง/เก็บรหัสผ่าน KKU
#### US-USR-002-AC-02

- **Given (กำหนดให้):** ตัวตน KKU เดียวกันถูกเชื่อมอยู่แล้ว
- **When (เมื่อ):** Admin พยายามสร้างบัญชีซ้ำ
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธด้วย Conflict และชี้ไปยังบัญชีเดิม
#### US-USR-002-AC-03

- **Given (กำหนดให้):** Admin เลือกบทบาท Admin หรือ Evaluator
- **When (เมื่อ):** ยืนยันการเปลี่ยนแปลง
- **Then (ระบบต้อง):** ระบบต้องบันทึกบทบาทและใช้สิทธิ์ใหม่ในการตรวจคำขอครั้งถัดไป
#### US-USR-002-AC-04

- **Given (กำหนดให้):** ข้อมูลจำเป็นไม่ครบหรือ Claim ไม่ตรงรูปแบบที่กำหนด
- **When (เมื่อ):** Admin กดบันทึก
- **Then (ระบบต้อง):** ระบบต้องไม่สร้างบัญชีและแสดง Validation รายฟิลด์
#### US-USR-002-AC-05

- **Given (กำหนดให้):** สร้างหรือแก้ไขบัญชีสำเร็จ
- **When (เมื่อ):** Transaction Commit
- **Then (ระบบต้อง):** ระบบต้องบันทึกผู้ดำเนินการ ค่าเดิม/ค่าใหม่ที่ไม่เป็นข้อมูลลับ และเวลาใน Audit Log

### Notes / Open Decisions

- KKU `sub` is the stable identity; email is display/contact data and never the primary identity.

---

## US-USR-003 — เปิดหรือปิดสิทธิ์บัญชี SEMS
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการเปิดหรือปิดสิทธิ์บัญชี SEMS เพื่อควบคุมผู้ที่สามารถเข้าใช้งานระบบได้

**คุณค่าทางธุรกิจ:** รองรับการเปลี่ยนผู้รับผิดชอบและลดความเสี่ยงจากบัญชีที่ไม่ควรใช้งานต่อ

### Preconditions

- บัญชีเป้าหมายมีอยู่ใน SEMS
- Admin มีสิทธิ์จัดการผู้ใช้

### Acceptance Criteria

#### US-USR-003-AC-01

- **Given (กำหนดให้):** บัญชีเป็น Inactive
- **When (เมื่อ):** Admin เปลี่ยนเป็น Active และยืนยัน
- **Then (ระบบต้อง):** ระบบต้องอนุญาต Login ในครั้งถัดไปตามบทบาทที่กำหนด
#### US-USR-003-AC-02

- **Given (กำหนดให้):** บัญชีเป็น Active
- **When (เมื่อ):** Admin เปลี่ยนเป็น Inactive
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธการสร้าง Session ใหม่และยกเลิก/ทำให้ Session เดิมใช้ไม่ได้ตาม Session Policy
#### US-USR-003-AC-03

- **Given (กำหนดให้):** Evaluator ถูกปิดสิทธิ์แต่มี Draft อยู่
- **When (เมื่อ):** สถานะถูกเปลี่ยนเป็น Inactive
- **Then (ระบบต้อง):** ระบบต้องเก็บ Draft ไว้เพื่อ Audit แต่ไม่อนุญาตให้บัญชีนั้นแก้ไขหรือ Submit
#### US-USR-003-AC-04

- **Given (กำหนดให้):** Admin กำลังปิดบัญชีของตนเองหรือบัญชี Admin สำคัญ
- **When (เมื่อ):** การเปลี่ยนจะทำให้ไม่มี Active Admin เหลืออยู่
- **Then (ระบบต้อง):** [ข้อเสนอแนะ] ระบบควรปฏิเสธและแจ้งว่าต้องมีผู้ดูแลระบบอย่างน้อยหนึ่งบัญชี
#### US-USR-003-AC-05

- **Given (กำหนดให้):** การเปลี่ยนสถานะสำเร็จ
- **When (เมื่อ):** ระบบ Commit
- **Then (ระบบต้อง):** ต้องบันทึกเหตุผล ผู้ดำเนินการ และเวลาใน Audit Log

---



<div style="page-break-after: always;"></div>

<a id="scholarship-round"></a>
# 03 — จัดการรอบทุน

## US-RND-001 — สร้างรอบทุน
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการสร้างรอบทุนใหม่ เพื่อแยกผู้สมัคร เกณฑ์ Evaluation และรายงานออกจากรอบอื่น

**คุณค่าทางธุรกิจ:** ทำให้ข้อมูลและกฎของแต่ละรอบไม่ปะปนกัน

### Preconditions

- Admin เข้าสู่ระบบ
- มีข้อมูลรอบทุนขั้นต่ำที่องค์กรกำหนด

### Acceptance Criteria

#### US-RND-001-AC-01

- **Given (กำหนดให้):** Admin กรอกข้อมูลรอบทุนที่ไม่ซ้ำและครบถ้วน
- **When (เมื่อ):** กดสร้าง
- **Then (ระบบต้อง):** ระบบต้องสร้างรอบทุนสถานะ `DRAFT` และกำหนดรหัสอ้างอิงที่ไม่ซ้ำ
#### US-RND-001-AC-02

- **Given (กำหนดให้):** รหัสหรือชื่ออ้างอิงที่กำหนดให้ Unique ซ้ำ
- **When (เมื่อ):** กดสร้าง
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธด้วย Conflict และไม่สร้างข้อมูลบางส่วน
#### US-RND-001-AC-03

- **Given (กำหนดให้):** สร้างรอบทุนสำเร็จ
- **When (เมื่อ):** Admin เปิดข้อมูลรอบทุน
- **Then (ระบบต้อง):** ต้องยังไม่มีผู้สมัคร เกณฑ์ Evaluation หรือ Result Summary ของรอบอื่นถูกเชื่อมเข้ามา
#### US-RND-001-AC-04

- **Given (กำหนดให้):** ผู้ใช้ที่ไม่ใช่ Admin เรียกสร้างรอบทุน
- **When (เมื่อ):** Backend ตรวจสิทธิ์
- **Then (ระบบต้อง):** ต้องตอบ `403` และไม่สร้างรอบทุน

---

## US-RND-002 — แก้ไขและเปิดรอบทุน
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการแก้ไขข้อมูลและเปิดรอบทุนเมื่อข้อมูลพร้อม เพื่อให้อาจารย์เริ่มเลือกและประเมินผู้สมัครได้

**คุณค่าทางธุรกิจ:** ป้องกันการเริ่มประเมินก่อนข้อมูลผู้สมัครและเกณฑ์พร้อมใช้งาน

### Preconditions

- รอบทุนอยู่ในสถานะ Draft
- มีชุดเกณฑ์ที่ผ่าน Validation และถูกกำหนดให้ใช้งาน
- มีข้อมูลผู้สมัครที่พร้อมประเมิน

### Acceptance Criteria

#### US-RND-002-AC-01

- **Given (กำหนดให้):** รอบทุนเป็น Draft และยังไม่มี Evaluation
- **When (เมื่อ):** Admin แก้ไข Metadata
- **Then (ระบบต้อง):** ระบบต้องอนุญาตให้แก้ไขและบันทึก Audit
#### US-RND-002-AC-02

- **Given (กำหนดให้):** เกณฑ์ยังไม่ครบหรือยังไม่ Activate
- **When (เมื่อ):** Admin พยายามเปลี่ยนรอบเป็น Open
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธและแสดงรายการเงื่อนไขที่ยังไม่ผ่าน
#### US-RND-002-AC-03

- **Given (กำหนดให้):** เงื่อนไขเปิดรอบครบ
- **When (เมื่อ):** Admin ยืนยันเปลี่ยนเป็น Open
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยนสถานะเป็น `OPEN` และอนุญาต Evaluator ที่ Active ค้นหา/เลือก Application; pre-open requires Application ≥1 and zero is Blocking `NO_APPLICANTS`
#### US-RND-002-AC-04

- **Given (กำหนดให้):** รอบเป็น Open
- **When (เมื่อ):** มีการแก้ไขข้อมูลที่กระทบคะแนนหรือการประเมิน
- **Then (ระบบต้อง):** ระบบต้องใช้ข้อจำกัดของโมดูลนั้น เช่น Criteria Versioning และห้ามแก้ข้อมูลผู้สมัครสำคัญผ่าน Import หลังเริ่ม Evaluation
#### US-RND-002-AC-05

- **Given (กำหนดให้):** เปลี่ยนสถานะสำเร็จ
- **When (เมื่อ):** Transaction Commit
- **Then (ระบบต้อง):** ระบบต้องบันทึกสถานะเดิม สถานะใหม่ ผู้ดำเนินการ และเวลา

---

## US-RND-003 — เก็บรอบทุนเป็น Archived
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Should have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการเก็บรอบทุนที่เสร็จสิ้นเป็น Archived เพื่อให้ข้อมูลย้อนหลังค้นหาได้แต่ไม่ถูกแก้ไขโดยไม่ตั้งใจ

**คุณค่าทางธุรกิจ:** ช่วยแยกรอบที่ใช้งานอยู่จากรอบย้อนหลังและรักษาหลักฐานการประเมิน

### Preconditions

- รอบทุนอยู่ในสถานะ Closed
- กระบวนการตรวจสอบและ Export ที่จำเป็นเสร็จแล้ว

### Acceptance Criteria

#### US-RND-003-AC-01

- **Given (กำหนดให้):** รอบทุนเป็น Closed
- **When (เมื่อ):** Admin ยืนยัน Archive
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยนสถานะเป็น `ARCHIVED` โดยไม่ลบผู้สมัคร Evaluation Result Summary เอกสาร หรือ Audit Log
#### US-RND-003-AC-02

- **Given (กำหนดให้):** รอบทุนเป็น Archived
- **When (เมื่อ):** ผู้ใช้เปิดดูตามสิทธิ์
- **Then (ระบบต้อง):** ระบบต้องแสดงข้อมูลแบบ Read-only และไม่อนุญาตเลือกผู้สมัคร บันทึก Draft Submit หรือแก้เกณฑ์
#### US-RND-003-AC-03

- **Given (กำหนดให้):** Admin พยายาม Archive รอบที่ยัง Open
- **When (เมื่อ):** ระบบตรวจสถานะ
- **Then (ระบบต้อง):** ต้องปฏิเสธและแนะนำให้ปิดรอบก่อน
#### US-RND-003-AC-04

- **Given (กำหนดให้):** มีความจำเป็นต้องนำ Archived กลับมาใช้งาน
- **When (เมื่อ):** Admin ร้องขอเปลี่ยนสถานะ
- **Then (ระบบต้อง):** exceptional Round Reopen requires request, reason/reference, designated approval and Audit; Archived is rejected and prior Final report becomes Superseded

---



<div style="page-break-after: always;"></div>

<a id="applicant-import"></a>
# 04 — Import ข้อมูลผู้สมัคร

## US-IMP-001 — อัปโหลดไฟล์และจับคู่คอลัมน์
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการอัปโหลด Excel/CSV และจับคู่คอลัมน์กับฟิลด์ SEMS เพื่อเตรียมข้อมูลผู้สมัครก่อนนำเข้าจริง

**คุณค่าทางธุรกิจ:** รองรับไฟล์จากระบบเดิมและลดการแก้ข้อมูลด้วยมือ

### Preconditions

- Admin เลือกรอบทุนปลายทางแล้ว
- Release 1 รับเฉพาะ `.xlsx` หรือ `.csv`; `.xls` เป็น Optional / Out of Scope

### Acceptance Criteria

#### US-IMP-001-AC-01

- **Given (กำหนดให้):** Admin เลือกไฟล์และรอบทุน
- **When (เมื่อ):** กด Upload
- **Then (ระบบต้อง):** ระบบต้องสร้าง Import Batch พร้อมชื่อไฟล์ ขนาด Hash ผู้ Upload รอบทุน และเวลา โดยยังไม่สร้าง Applicant จริง
#### US-IMP-001-AC-02

- **Given (กำหนดให้):** ระบบอ่าน Header สำเร็จ
- **When (เมื่อ):** เข้าสู่ขั้นตอน Mapping
- **Then (ระบบต้อง):** ระบบต้องเสนอ Mapping จากชื่อจริงและ Alias เช่น `ชือ` → `ชื่อ/first_name` และอนุญาต Admin แก้ Mapping
#### US-IMP-001-AC-03

- **Given (กำหนดให้):** Header ที่จำเป็นหายหรือคอลัมน์เดียวถูกจับคู่ซ้ำอย่างขัดแย้ง
- **When (เมื่อ):** Admin ขอ Preview
- **Then (ระบบต้อง):** ระบบต้องบล็อกขั้นตอนถัดไปและแสดง `MISSING_REQUIRED_COLUMN` หรือ `DUPLICATE_COLUMN_MAPPING`
#### US-IMP-001-AC-04

- **Given (กำหนดให้):** Identifier เช่นรหัสนักศึกษาและโทรศัพท์อยู่ในไฟล์
- **When (เมื่อ):** ระบบอ่านข้อมูล
- **Then (ระบบต้อง):** ระบบต้องอ่านเป็น Text และตรวจจับ Scientific Notation เพื่อไม่ให้เลขศูนย์หรือรูปแบบรหัสเสียหาย
#### US-IMP-001-AC-05

- **Given (กำหนดให้):** อัปโหลดไฟล์ชนิดไม่รองรับหรืออ่านไม่ได้
- **When (เมื่อ):** ระบบ Parse
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธไฟล์ ไม่สร้างข้อมูลจริง และบันทึกสถานะ Batch เป็น Failed พร้อม Error Code

---

## US-IMP-002 — Preview และตรวจสอบความถูกต้องของข้อมูล
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-015, RD-017, RD-019, RD-020 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการเห็นข้อมูลหลังแปลงและข้อผิดพลาดรายแถว เพื่อแก้ปัญหาก่อนยืนยัน Import

**คุณค่าทางธุรกิจ:** ลดข้อมูลผิดรูปแบบ ข้อมูลซ้ำ และการผูกประวัติหลายแถวผิดคน

### Preconditions

- Import Batch ผ่าน Header Mapping
- ระบบยังไม่ Commit Applicant จริง

### Acceptance Criteria

#### US-IMP-002-AC-01

- **Given (กำหนดให้):** แถวมี `student_id` หลัง Trim
- **When (เมื่อ):** ระบบจำแนกแถว
- **Then (ระบบต้อง):** ต้องถือเป็น Applicant Row และตรวจ Hard Required, รูปแบบรหัส, GPA, วันที่, Contact และฟิลด์อื่นตาม Mapping
#### US-IMP-002-AC-02

- **Given (กำหนดให้):** แถวไม่มี `student_id` แต่มีเฉพาะข้อมูล กยศ./ทุน
- **When (เมื่อ):** มี Applicant Row ก่อนหน้าที่ Valid
- **Then (ระบบต้อง):** ต้องจำแนกเป็น Continuation Row สืบทอดผู้สมัครเจ้าของ และสร้างเฉพาะ Child History ใน Payload Preview
#### US-IMP-002-AC-03

- **Given (กำหนดให้):** Continuation Row ไม่มี Applicant เจ้าของหรือมีข้อมูล Applicant อื่นปะปน
- **When (เมื่อ):** ระบบ Validate
- **Then (ระบบต้อง):** ต้องแสดง `ORPHAN_CONTINUATION_ROW` หรือ `VALIDATION_ERROR` และไม่ถือว่าแถว Valid
#### US-IMP-002-AC-04

- **Given (กำหนดให้):** มีรหัสผู้สมัครซ้ำภายในไฟล์
- **When (เมื่อ):** ระบบตรวจ Business Key
- **Then (ระบบต้อง):** ต้องแสดง `DUPLICATE_STUDENT_IN_FILE` และไม่รวมแถวดังกล่าวเป็นรายการนำเข้าที่ Valid
#### US-IMP-002-AC-05

- **Given (กำหนดให้):** พบ GPA นอก 0.00–4.00 วันที่แปลงไม่ได้ หรือพิกัดนอกช่วง
- **When (เมื่อ):** ระบบ Validate
- **Then (ระบบต้อง):** ต้องแสดง Error Code เฉพาะฟิลด์ เช่น `INVALID_GPA`, `INVALID_DATE`, `INVALID_COORDINATE` พร้อม Source Row, Raw Value และข้อความ
#### US-IMP-002-AC-06

- **Given (กำหนดให้):** Preview เสร็จ
- **When (เมื่อ):** Admin ตรวจผล
- **Then (ระบบต้อง):** ระบบต้องแสดงจำนวน Total, Applicant, Continuation, Valid, Warning, Error, Duplicate และ Skipped รวมถึง Normalized Value ของแต่ละฟิลด์
#### US-IMP-002-AC-07

- **Given (กำหนดให้):** Batch มี Blocking Error
- **When (เมื่อ):** Admin พยายามยืนยัน
- **Then (ระบบต้อง):** ระบบต้องปิดใช้งานหรือปฏิเสธ Confirm จนกว่าจะมีนโยบาย Partial Import ที่ได้รับอนุมัติ

---

## US-IMP-003 — ยืนยันและบันทึกผล Import
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-018, RD-019 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการยืนยัน Import หลังตรวจ Preview เพื่อบันทึกข้อมูลผู้สมัครและประวัติที่ผ่านกฎอย่างครบถ้วน

**คุณค่าทางธุรกิจ:** ทำให้การนำเข้าตรวจสอบย้อนหลังได้และไม่เกิดข้อมูลครึ่งชุด

### Preconditions

- Batch ผ่าน Validation ตาม Import Policy
- Admin ยืนยันรอบทุนและนโยบาย Duplicate

### Acceptance Criteria

#### US-IMP-003-AC-01

- **Given (กำหนดให้):** Batch ไม่มี Blocking Error
- **When (เมื่อ):** Admin กดยืนยัน Import
- **Then (ระบบต้อง):** ระบบต้องบันทึก Applicant และ Child Records ภายใน Database Transaction เดียวกันตาม Payload ที่ Preview แล้ว
#### US-IMP-003-AC-02

- **Given (กำหนดให้):** เกิด Database/File Processing Error ระหว่าง Commit
- **When (เมื่อ):** Transaction ล้มเหลว
- **Then (ระบบต้อง):** ระบบต้อง Rollback ข้อมูลทั้ง Batch ตามโหมด All-or-Nothing และบันทึก `IMPORT_STATE_INVALID` เมื่อ state ไม่อนุญาตให้ commit
#### US-IMP-003-AC-03

- **Given (กำหนดให้):** ผู้สมัครซ้ำกับฐานข้อมูลในรอบเดียวกัน
- **When (เมื่อ):** ยังไม่มี Evaluation
- **Then (ระบบต้อง):** ค่าเริ่มต้นต้อง Skip; never auto-Upsert; explicit Update เฉพาะก่อนมี Evaluation; หลังจากนั้นใช้ Controlled Correction พร้อม before/after Audit
#### US-IMP-003-AC-04

- **Given (กำหนดให้):** ผู้สมัครซ้ำและมี Evaluation แล้ว
- **When (เมื่อ):** Admin พยายาม Update ผ่าน Import
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธด้วย `IMPORT_STATE_INVALID` เพื่อป้องกันข้อมูลที่ใช้ประกอบการประเมินเปลี่ยนย้อนหลัง
#### US-IMP-003-AC-05

- **Given (กำหนดให้):** Commit สำเร็จ
- **When (เมื่อ):** ระบบสรุปผล
- **Then (ระบบต้อง):** ต้องแสดงจำนวน Imported/Updated/Skipped/Failed และบันทึก Import History ที่ค้นหาได้ภายหลัง
#### US-IMP-003-AC-06

- **Given (กำหนดให้):** Admin เปิด Import History
- **When (เมื่อ):** เลือกรายการ Batch
- **Then (ระบบต้อง):** ระบบต้องแสดงชื่อไฟล์ Hash รอบทุน ผู้นำเข้า เวลา Mapping สรุปผล และ Error/Warning Report โดยไม่เปิดเผยข้อมูลเกินสิทธิ์

---



<div style="page-break-after: always;"></div>

<a id="applicant-documents"></a>
# 05 — อัปโหลดและเข้าถึงเอกสารผู้สมัคร

## US-DOC-001 — อัปโหลดเอกสารให้ผู้สมัคร
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการอัปโหลดเอกสารประกอบให้ผู้สมัครแต่ละราย เพื่อให้อาจารย์ใช้พิจารณาในหน้าประเมิน

**คุณค่าทางธุรกิจ:** รวมข้อมูลและเอกสารไว้ในระบบเดียว ลดการเปิดหลายไฟล์และลดการแนบผิดคน

### Preconditions

- ผู้สมัครถูกสร้างในรอบทุนแล้ว
- Admin มีสิทธิ์จัดการข้อมูลผู้สมัครในรอบนั้น

### Acceptance Criteria

#### US-DOC-001-AC-01

- **Given (กำหนดให้):** Admin เลือกผู้สมัครและไฟล์ PDF/JPG/PNG ที่ผ่านข้อกำหนด
- **When (เมื่อ):** กด Upload
- **Then (ระบบต้อง):** ระบบต้องจัดเก็บ Binary ใน File/Object Storage และบันทึก Metadata/Reference ใน PostgreSQL โดยไม่เก็บ Binary ในตารางฐานข้อมูล
#### US-DOC-001-AC-02

- **Given (กำหนดให้):** ไฟล์ชนิดไม่รองรับ ขนาดเกินกำหนด หรือ Signature ไม่ตรง Extension
- **When (เมื่อ):** ระบบตรวจไฟล์
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธก่อนเผยแพร่ไฟล์และแสดง Error Code ที่ชัดเจน
#### US-DOC-001-AC-03

- **Given (กำหนดให้):** Upload สำเร็จ
- **When (เมื่อ):** ระบบ Commit Metadata
- **Then (ระบบต้อง):** ต้องบันทึกชื่อเดิม ชื่อจัดเก็บ MIME Type ขนาด Storage Key ผู้ Upload เวลา และ Applicant/Round ที่อ้างอิง
#### US-DOC-001-AC-04

- **Given (กำหนดให้):** เกิด Storage Error หลังสร้าง Metadata หรือกลับกัน
- **When (เมื่อ):** กระบวนการไม่ครบทั้งสองส่วน
- **Then (ระบบต้อง):** ระบบต้องชดเชย/rollback เพื่อไม่ให้มี Metadata กำพร้าหรือไฟล์กำพร้าโดยไม่ถูกติดตาม
#### US-DOC-001-AC-05

- **Given (กำหนดให้):** Upload สำเร็จ
- **When (เมื่อ):** Admin กลับมาดูรายการเอกสาร
- **Then (ระบบต้อง):** ต้องเห็นเอกสารอยู่กับผู้สมัครและรอบทุนที่ถูกต้อง พร้อม Audit Event

### Notes / Open Decisions

- PDF 20 MB, JPG/PNG 10 MB, 10 files/application, import 20 MB; production files stay Quarantined until malware scan passes.

---

## US-DOC-002 — เปิดดูหรือดาวน์โหลดเอกสารตามสิทธิ์
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ / อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะผู้มีสิทธิ์ประเมิน ฉันต้องการเปิดดูเอกสารของผู้สมัคร เพื่อใช้ข้อมูลประกอบการให้คะแนนโดยไม่ออกจากกระบวนการหลัก

**คุณค่าทางธุรกิจ:** ทำให้การสัมภาษณ์และประเมินต่อเนื่องและปลอดภัย

### Preconditions

- ผู้ใช้ Login แล้ว
- เอกสารมี Metadata ที่ใช้งานได้

### Acceptance Criteria

#### US-DOC-002-AC-01

- **Given (กำหนดให้):** Admin หรือ Evaluator เจ้าของ Evaluation ขอเอกสาร
- **When (เมื่อ):** Backend ตรวจ Role, Round และ Ownership ผ่าน
- **Then (ระบบต้อง):** ระบบต้องส่งไฟล์ผ่าน Endpoint ที่ตรวจสิทธิ์ทุกครั้งหรือ URL ชั่วคราวที่มีอายุจำกัด
#### US-DOC-002-AC-02

- **Given (กำหนดให้):** ไฟล์เป็น PDF/JPG/PNG และ Browser รองรับ
- **When (เมื่อ):** ผู้ใช้กดเปิดดู
- **Then (ระบบต้อง):** ระบบควรแสดง Preview ใน Browser โดยไม่เปิดเผย Storage Path ถาวร
#### US-DOC-002-AC-03

- **Given (กำหนดให้):** ไฟล์เปิด Preview ไม่ได้แต่ผู้ใช้มีสิทธิ์
- **When (เมื่อ):** ผู้ใช้กดดาวน์โหลด
- **Then (ระบบต้อง):** ระบบต้องดาวน์โหลดด้วยชื่อไฟล์ที่เหมาะสมและ Content-Type/Disposition ที่ถูกต้อง
#### US-DOC-002-AC-04

- **Given (กำหนดให้):** Evaluator ไม่มี Evaluation สำหรับผู้สมัครหรือเรียกเอกสารข้ามรอบ
- **When (เมื่อ):** Backend ตรวจสิทธิ์ไม่ผ่าน
- **Then (ระบบต้อง):** ระบบต้องตอบ `403/404` ตาม Security Policy ไม่ส่งไฟล์หรือ Storage URL
#### US-DOC-002-AC-05

- **Given (กำหนดให้):** ไฟล์สูญหายหรือเสียหายใน Storage
- **When (เมื่อ):** ผู้ใช้ขอเปิด
- **Then (ระบบต้อง):** ระบบต้องแสดงข้อผิดพลาดที่ไม่เปิดเผย Path ภายในและบันทึกเหตุการณ์เพื่อให้ Admin ตรวจสอบ

---



<div style="page-break-after: always;"></div>

<a id="criteria-management"></a>
# 06 — จัดการเกณฑ์คะแนน

## US-CRI-001 — สร้างชุดเกณฑ์สำหรับรอบทุน
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-012, RD-013, RD-014 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการสร้างชุดเกณฑ์คะแนนแยกตามรอบทุน เพื่อให้อาจารย์ประเมินผู้สมัครด้วยแบบฟอร์มเดียวกัน

**คุณค่าทางธุรกิจ:** ทำให้คะแนนมีโครงสร้างชัดเจนและคำนวณได้อัตโนมัติ

### Preconditions

- รอบทุนอยู่ในสถานะ Draft
- Admin มีสิทธิ์จัดการเกณฑ์

### Acceptance Criteria

#### US-CRI-001-AC-01

- **Given (กำหนดให้):** Admin สร้าง Criteria Set ใหม่
- **When (เมื่อ):** บันทึกข้อมูล
- **Then (ระบบต้อง):** ระบบต้องผูกชุดเกณฑ์กับรอบทุนและกำหนด Version/Status เริ่มต้นเป็น Draft
#### US-CRI-001-AC-02

- **Given (กำหนดให้):** Admin เพิ่ม Criterion
- **When (เมื่อ):** กรอกข้อมูล
- **Then (ระบบต้อง):** ระบบต้องรองรับอย่างน้อย criterion_code, ชื่อ, คำอธิบาย, คะแนนต่ำสุด, คะแนนเต็ม, น้ำหนัก, ลำดับ, required flag และ version
#### US-CRI-001-AC-03

- **Given (กำหนดให้):** criterion_code ซ้ำใน Criteria Version เดียวกัน
- **When (เมื่อ):** กดบันทึก
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธด้วย Conflict
#### US-CRI-001-AC-04

- **Given (กำหนดให้):** คะแนนต่ำสุดมากกว่าคะแนนเต็ม น้ำหนักติดลบ หรือลำดับซ้ำตามกฎที่กำหนด
- **When (เมื่อ):** Validate
- **Then (ระบบต้อง):** ระบบต้องแสดง Validation ราย Criterion และไม่ Activate ชุดเกณฑ์
#### US-CRI-001-AC-05

- **Given (กำหนดให้):** Admin จัดลำดับเกณฑ์
- **When (เมื่อ):** บันทึก
- **Then (ระบบต้อง):** Evaluator ต้องเห็นเกณฑ์ตามลำดับเดียวกันในแบบฟอร์ม Review และรายงาน

---

## US-CRI-002 — ตรวจสอบและเปิดใช้เกณฑ์
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการตรวจสอบและ Activate ชุดเกณฑ์ที่สมบูรณ์ เพื่อให้รอบทุนเปิดใช้งานได้โดยไม่มีแบบฟอร์มไม่ครบ

**คุณค่าทางธุรกิจ:** ป้องกัน Evaluation ที่ไม่มีสูตรหรือเกณฑ์อ้างอิงชัดเจน

### Preconditions

- Criteria Set อยู่ในสถานะ Draft
- รอบทุนยังไม่มี Evaluation ที่อ้างอิง Version นี้

### Acceptance Criteria

#### US-CRI-002-AC-01

- **Given (กำหนดให้):** Criteria Set มี Criterion ครบและกฎคะแนนผ่าน Validation
- **When (เมื่อ):** Admin ขอ Activate
- **Then (ระบบต้อง):** ระบบต้องตรวจ Required Metadata, คะแนนต่ำสุด/เต็ม, น้ำหนัก, ลำดับ และสูตรที่อ้างอิง
#### US-CRI-002-AC-02

- **Given (กำหนดให้):** สูตรหรือน้ำหนักยังไม่ผ่านการยืนยัน/กำหนด
- **When (เมื่อ):** กฎดังกล่าวจำเป็นต่อการคำนวณ
- **Then (ระบบต้อง):** ระบบต้องบล็อก Activate และแสดงว่าต้องยืนยัน Scoring Rule ก่อน
#### US-CRI-002-AC-03

- **Given (กำหนดให้):** Validation ผ่าน
- **When (เมื่อ):** Admin ยืนยัน Activate
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยน Version เป็น Active และทำให้ Evaluation ใหม่ของรอบนั้นอ้างอิง Version นี้
#### US-CRI-002-AC-04

- **Given (กำหนดให้):** มี Active Version อยู่แล้ว
- **When (เมื่อ):** Admin Activate Version ใหม่ก่อนเริ่ม Evaluation
- **Then (ระบบต้อง):** ระบบต้องทำให้มี Active Version เดียวต่อรอบตาม Policy และบันทึก Version เดิมไว้
#### US-CRI-002-AC-05

- **Given (กำหนดให้):** Activate สำเร็จ
- **When (เมื่อ):** ผู้ประเมินเริ่ม Evaluation
- **Then (ระบบต้อง):** ระบบต้องแสดง Criterion จาก Version ที่ถูกอ้างอิง ไม่ใช้ข้อมูลจากรอบอื่น

### Notes / Open Decisions

- Confirmed: Template เริ่มต้น 10 scoring criteria รวม 100 คะแนน.
- Confirmed: เกณฑ์ดุลพินิจรับจำนวนเต็ม 0–10; non-standard option requires reason.

---

## US-CRI-003 — สร้าง Version ใหม่เมื่อเกณฑ์ถูกใช้งานแล้ว
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการสร้าง Criteria Version ใหม่แทนการแก้เกณฑ์ที่ถูกใช้แล้ว เพื่อรักษาความถูกต้องของคะแนนย้อนหลัง

**คุณค่าทางธุรกิจ:** ทำให้แต่ละ Evaluation ตรวจสอบได้ว่าคำนวณจากเกณฑ์ชุดใด

### Preconditions

- Criteria Version เดิมถูกอ้างอิงโดย Evaluation อย่างน้อยหนึ่งรายการ

### Acceptance Criteria

#### US-CRI-003-AC-01

- **Given (กำหนดให้):** Version ถูกอ้างอิงโดย Evaluation
- **When (เมื่อ):** Admin พยายามแก้คะแนนเต็ม น้ำหนัก หรือสูตรโดยตรง
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธการแก้ไขที่กระทบคะแนน
#### US-CRI-003-AC-02

- **Given (กำหนดให้):** Admin เลือกสร้าง Version ใหม่
- **When (เมื่อ):** ระบบ Copy Criteria
- **Then (ระบบต้อง):** ต้องสร้าง Draft Version ใหม่พร้อม version number ใหม่และไม่เปลี่ยนข้อมูลของ Version เดิม
#### US-CRI-003-AC-03

- **Given (กำหนดให้):** Evaluation เดิมมี Criteria Version อ้างอิง
- **When (เมื่อ):** Version ใหม่ถูก Activate
- **Then (ระบบต้อง):** Evaluation เดิมต้องยังแสดง/คำนวณจาก Version เดิมตาม Snapshot/Reference ที่เก็บไว้
#### US-CRI-003-AC-04

- **Given (กำหนดให้):** ยังไม่มี Evaluation ในรอบ
- **When (เมื่อ):** Admin แก้ Draft/Active ตาม Policy
- **Then (ระบบต้อง):** ระบบอาจอนุญาตแก้ไข แต่ต้องบันทึก Audit และ Revalidate ก่อนเปิดรอบ
#### US-CRI-003-AC-05

- **Given (กำหนดให้):** Version ใหม่ถูกใช้กับ Evaluation ใหม่
- **When (เมื่อ):** สร้าง Evaluation
- **Then (ระบบต้อง):** ระบบต้องเก็บ criteria_version_id อย่างชัดเจนเพื่อใช้คำนวณและรายงาน

---



<div style="page-break-after: always;"></div>

<a id="applicant-selection"></a>
# 07 — ค้นหาและเลือกผู้สมัคร

## US-SEL-001 — ค้นหาผู้สมัครในรอบที่เปิด
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการค้นหาผู้สมัครที่กำลังสัมภาษณ์ด้วยรหัส ชื่อ หรือนามสกุล เพื่อเลือกคนที่ถูกต้องอย่างรวดเร็ว

**คุณค่าทางธุรกิจ:** ลดการเลือกผิดคนและทำให้การสัมภาษณ์ต่อเนื่อง

### Preconditions

- Evaluator Login และบัญชี Active
- มีรอบทุนสถานะ Open

### Acceptance Criteria

#### US-SEL-001-AC-01

- **Given (กำหนดให้):** Evaluator เปิดหน้าค้นหาผู้สมัคร
- **When (เมื่อ):** เลือกรอบที่ Open
- **Then (ระบบต้อง):** ระบบต้องแสดงรายชื่อผู้สมัครเฉพาะรอบนั้นและรองรับค้นหาด้วยรหัสนักศึกษา ชื่อ หรือนามสกุล
#### US-SEL-001-AC-02

- **Given (กำหนดให้):** Evaluator ยังไม่เลือกผู้สมัคร
- **When (เมื่อ):** ระบบแสดงผลค้นหา
- **Then (ระบบต้อง):** ต้องแสดงข้อมูลขั้นต่ำที่จำเป็น เช่น รหัส ชื่อ สาขา/ชั้นปี และสถานะจำนวนผู้ประเมิน โดยไม่แสดงข้อมูลละเอียดอ่อนหรือเอกสาร
#### US-SEL-001-AC-03

- **Given (กำหนดให้):** ผู้สมัครมี Evaluation ที่ยังไม่ยกเลิกครบ 3 รายการ
- **When (เมื่อ):** แสดงผลค้นหา
- **Then (ระบบต้อง):** ระบบต้องระบุว่าเต็มและไม่ให้เริ่ม Evaluation ใหม่
#### US-SEL-001-AC-04

- **Given (กำหนดให้):** รอบทุนไม่ใช่ Open
- **When (เมื่อ):** Evaluator ค้นหาหรือเรียก API เลือกผู้สมัคร
- **Then (ระบบต้อง):** ระบบต้องไม่อนุญาตสร้าง Evaluation ใหม่
#### US-SEL-001-AC-05

- **Given (กำหนดให้):** ไม่มีผลลัพธ์ตรงคำค้น
- **When (เมื่อ):** ระบบค้นหาเสร็จ
- **Then (ระบบต้อง):** ต้องแสดงสถานะไม่พบข้อมูลโดยไม่เปิดเผยรายชื่อจากรอบอื่น

---

## US-SEL-002 — เลือกผู้สมัครและสร้าง Evaluation Draft
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |
| Decision Reference | RD-001, RD-002, RD-003, RD-005 |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการเลือกผู้สมัครที่กำลังสัมภาษณ์ เพื่อเริ่มบันทึกผลการประเมินของฉัน

**คุณค่าทางธุรกิจ:** สร้างรายการประเมินที่มีเจ้าของชัดเจนและควบคุมจำนวนผู้ประเมินไม่เกิน 3 คน

### Preconditions

- รอบทุนเป็น Open
- Evaluator Active
- ผู้สมัครอยู่ในรอบที่เลือก

### Acceptance Criteria

#### US-SEL-002-AC-01

- **Given (กำหนดให้):** Evaluator ไม่มี Evaluation ที่ยังไม่ถูกยกเลิกสำหรับผู้สมัคร
- **When (เมื่อ):** กดเลือกผู้สมัคร
- **Then (ระบบต้อง):** ระบบต้องตรวจเงื่อนไขทั้งหมดอีกครั้งที่ Backend ภายใน Transaction
#### US-SEL-002-AC-02

- **Given (กำหนดให้):** จำนวน Evaluation ที่ยังไม่ถูกยกเลิกของผู้สมัครน้อยกว่า 3
- **When (เมื่อ):** เงื่อนไขอื่นผ่าน
- **Then (ระบบต้อง):** ระบบต้องสร้าง Evaluation สถานะ `DRAFT` ผูกกับรอบ ผู้สมัคร Evaluator และ Criteria Version ที่ใช้งาน
#### US-SEL-002-AC-03

- **Given (กำหนดให้):** Evaluator คนเดิมมี Evaluation อยู่แล้ว
- **When (เมื่อ):** กดเลือกซ้ำ
- **Then (ระบบต้อง):** ระบบต้องไม่สร้างรายการใหม่และนำผู้ใช้กลับไปยัง Draft เดิมหรือแจ้งว่ามีรายการอยู่แล้ว
#### US-SEL-002-AC-04

- **Given (กำหนดให้):** ผู้สมัครมี Submitted ครบ 2 แต่ยังมี Active Evaluation น้อยกว่า 3 และรอบยัง Open
- **When (เมื่อ):** Evaluator คนที่ 3 เลือก
- **Then (ระบบต้อง):** ระบบต้องอนุญาตให้สร้าง Draft คนที่ 3
#### US-SEL-002-AC-05

- **Given (กำหนดให้):** ผู้สมัครมี Active Evaluation ครบ 3
- **When (เมื่อ):** Evaluator คนที่ 4 พยายามเลือก
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธด้วย Conflict และไม่สร้างรายการ
#### US-SEL-002-AC-06

- **Given (กำหนดให้):** Evaluator หลายคนเลือกพร้อมกันขณะเหลือช่องเดียว
- **When (เมื่อ):** คำขอชนกัน
- **Then (ระบบต้อง):** ระบบต้องใช้ Transaction/Lock/Unique Constraint ให้สำเร็จได้ไม่เกินหนึ่งคำขอและจำนวน Active Evaluation หลัง Commit ต้องไม่เกิน 3
#### US-SEL-002-AC-07

- **Given (กำหนดให้):** สร้าง Evaluation สำเร็จ
- **When (เมื่อ):** ระบบตอบกลับ
- **Then (ระบบต้อง):** ต้องเปิดหน้าประเมินของ Evaluation นั้นและบันทึก Audit Event

---

## US-SEL-003 — ยกเลิก Draft ก่อน Submit
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Should have |
| Decision Reference | RD-009 |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการยกเลิก Draft ที่เลือกผิดก่อน Submit เพื่อคืนช่องให้ผู้ประเมินคนอื่น

**คุณค่าทางธุรกิจ:** ลดภาระ Admin และป้องกันช่องผู้ประเมินถูกล็อกโดยรายการที่ไม่ใช้แล้ว

### Preconditions

- Evaluation เป็นของผู้ใช้
- สถานะยังเป็น Draft และไม่เคย Submitted

### Acceptance Criteria

#### US-SEL-003-AC-01

- **Given (กำหนดให้):** เจ้าของ Draft เลือกยกเลิก
- **When (เมื่อ):** ยืนยันใน Dialog
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยนสถานะเป็น `CANCELLED` แบบ Soft Delete, ไม่ลบประวัติ, Audit และคืน slot atomically
#### US-SEL-003-AC-02

- **Given (กำหนดให้):** ยกเลิกสำเร็จ
- **When (เมื่อ):** Transaction Commit
- **Then (ระบบต้อง):** รายการต้องไม่ถูกนับในเพดาน 3 คนและช่องต้องพร้อมให้ผู้ประเมินคนอื่นเลือกทันที
#### US-SEL-003-AC-03

- **Given (กำหนดให้):** Evaluation เป็น Submitted หรือไม่ใช่ของผู้ใช้
- **When (เมื่อ):** ผู้ใช้พยายามยกเลิก
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธและชี้ให้ใช้ Reopen/Approval Policy หากเกี่ยวข้อง
#### US-SEL-003-AC-04

- **Given (กำหนดให้):** ผู้ใช้ยืนยันยกเลิก
- **When (เมื่อ):** ระบบบันทึก
- **Then (ระบบต้อง):** ต้องบันทึกเหตุผล (ถ้ากำหนด) ผู้ดำเนินการ เวลา และค่าก่อน/หลังใน Audit Log
#### US-SEL-003-AC-05

- **Given (กำหนดให้):** เกิด Concurrent Selection ขณะยกเลิก
- **When (เมื่อ):** Transaction ทำงาน
- **Then (ระบบต้อง):** ระบบต้องรักษาเพดาน Active Evaluation ไม่เกิน 3 และไม่เกิด Lost Update

---



<div style="page-break-after: always;"></div>

<a id="evaluation-draft"></a>
# 08 — บันทึกผลการประเมินแบบ Draft

## US-DRF-001 — ดูข้อมูลประกอบการประเมินในหน้าเดียว
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการดูข้อมูลผู้สมัคร เอกสาร ประวัติทุน และเกณฑ์ในหน้าเดียว เพื่อประเมินได้อย่างต่อเนื่อง

**คุณค่าทางธุรกิจ:** ลดการสลับหลายระบบและลดความผิดพลาดจากการดูข้อมูลผิดคน

### Preconditions

- Evaluator เป็นเจ้าของ Evaluation ที่ยังใช้งานอยู่

### Acceptance Criteria

#### US-DRF-001-AC-01

- **Given (กำหนดให้):** Evaluator เปิด Evaluation ของตน
- **When (เมื่อ):** ระบบโหลดหน้า
- **Then (ระบบต้อง):** ต้องแสดงข้อมูลพื้นฐาน ข้อมูลประกอบ ประวัติ กยศ./ทุน เอกสาร และ Criteria Version ของรอบเดียวกัน
#### US-DRF-001-AC-02

- **Given (กำหนดให้):** ข้อมูลบางส่วนว่าง
- **When (เมื่อ):** แสดงหน้า
- **Then (ระบบต้อง):** ระบบต้องแสดงว่าไม่มีข้อมูลแทนการแสดงค่าหลอกหรือเกิด Error
#### US-DRF-001-AC-03

- **Given (กำหนดให้):** Evaluator พยายามเปิด Evaluation ของผู้อื่น
- **When (เมื่อ):** Backend ตรวจ Ownership
- **Then (ระบบต้อง):** ต้องตอบ `403/404` และไม่ส่งข้อมูลผู้สมัครละเอียดอ่อน
#### US-DRF-001-AC-04

- **Given (กำหนดให้):** Criteria Version ถูกเปลี่ยนภายหลัง
- **When (เมื่อ):** เปิด Evaluation เดิม
- **Then (ระบบต้อง):** ระบบต้องแสดง Version ที่ Evaluation อ้างอิง ไม่เปลี่ยนตาม Active Version ใหม่โดยอัตโนมัติ
#### US-DRF-001-AC-05

- **Given (กำหนดให้):** เอกสารไม่พร้อมใช้งาน
- **When (เมื่อ):** หน้าโหลด
- **Then (ระบบต้อง):** ส่วนคะแนนและข้อมูลอื่นต้องยังใช้งานได้ พร้อมแสดงข้อผิดพลาดเฉพาะเอกสาร

---

## US-DRF-002 — กรอกคะแนนและความคิดเห็น
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการกรอกคะแนนรายเกณฑ์และความคิดเห็น เพื่อบันทึกเหตุผลและผลการพิจารณาของฉัน

**คุณค่าทางธุรกิจ:** เก็บคะแนนในรูปแบบที่ตรวจสอบและคำนวณได้

### Preconditions

- Evaluation สถานะ Draft
- รอบทุนยัง Open สำหรับการแก้ไข/ส่งตาม Policy

### Acceptance Criteria

#### US-DRF-002-AC-01

- **Given (กำหนดให้):** Evaluator กรอกคะแนนใน Criterion
- **When (เมื่อ):** ค่าต่ำกว่าคะแนนต่ำสุดหรือสูงกว่าคะแนนเต็ม
- **Then (ระบบต้อง):** ระบบต้องแสดง Validation และไม่ยอมรับค่าเป็นคะแนนที่ Valid
#### US-DRF-002-AC-02

- **Given (กำหนดให้):** Criterion กำหนดชนิดค่าเป็นจำนวนเต็ม/ทศนิยม/ตัวเลือก
- **When (เมื่อ):** Evaluator กรอกค่า
- **Then (ระบบต้อง):** ระบบต้องบังคับชนิดและ Step ตาม Criteria Metadata
#### US-DRF-002-AC-03

- **Given (กำหนดให้):** Evaluator กรอกความคิดเห็น
- **When (เมื่อ):** ความยาวเกินกำหนดหรือมีข้อมูลที่ระบบห้าม
- **Then (ระบบต้อง):** ระบบต้องแสดง Validation โดยไม่ทำให้คะแนนที่กรอกสูญหาย
#### US-DRF-002-AC-04

- **Given (กำหนดให้):** ความคิดเห็นเป็น Optional ตาม Baseline
- **When (เมื่อ):** เว้นว่างและบันทึก Draft
- **Then (ระบบต้อง):** ระบบต้องอนุญาต; หาก Criteria/Submit Rule กำหนด Required ให้ตรวจตอน Submit
#### US-DRF-002-AC-05

- **Given (กำหนดให้):** Evaluation เป็น Submitted/Cancelled หรือผู้ใช้ไม่ใช่เจ้าของ
- **When (เมื่อ):** พยายามแก้คะแนน
- **Then (ระบบต้อง):** Backend ต้องปฏิเสธการแก้ไข

### Notes / Open Decisions

- Overall comment is optional; reason is required for non-standard Custom Score, Custom Amount, reopen/cancel/override/correction, or criterion configured `comment_required=true`.

---

## US-DRF-003 — บันทึกและกลับมาแก้ Draft
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการบันทึกแบบร่างและกลับมาแก้ภายหลัง เพื่อไม่ให้ข้อมูลสูญหายก่อนพร้อม Submit

**คุณค่าทางธุรกิจ:** รองรับการประเมินที่ใช้เวลาหลายช่วงและลดความเสี่ยงจากการปิด Browser

### Preconditions

- Evaluation เป็น Draft และเป็นของผู้ใช้

### Acceptance Criteria

#### US-DRF-003-AC-01

- **Given (กำหนดให้):** Evaluator กรอกข้อมูลบางส่วน
- **When (เมื่อ):** กดบันทึก Draft
- **Then (ระบบต้อง):** ระบบต้องบันทึกค่าที่ผ่าน Validation โดยไม่บังคับให้ทุก Criterion ครบ
#### US-DRF-003-AC-02

- **Given (กำหนดให้):** บันทึกสำเร็จ
- **When (เมื่อ):** ระบบตอบกลับ
- **Then (ระบบต้อง):** ต้องแสดงเวลาบันทึกล่าสุดและคงสถานะ `DRAFT`
#### US-DRF-003-AC-03

- **Given (กำหนดให้):** เกิด Validation Error บางฟิลด์
- **When (เมื่อ):** กดบันทึก
- **Then (ระบบต้อง):** ระบบต้องระบุฟิลด์ที่ผิดและไม่ทำให้ค่าที่ถูกต้องในหน้าจอหาย; นโยบายบันทึกบางส่วนต้องสอดคล้องกันทั้ง UI/API
#### US-DRF-003-AC-04

- **Given (กำหนดให้):** ผู้สมัครมี Active Evaluation ครบ 3 แล้ว
- **When (เมื่อ):** เจ้าของ Draft เดิมกลับมาแก้
- **Then (ระบบต้อง):** ระบบต้องยังอนุญาตให้เปิดและแก้ Draft ของตน เพราะเพดาน 3 ใช้กับการสร้างรายการใหม่
#### US-DRF-003-AC-05

- **Given (กำหนดให้):** Session หมดอายุระหว่างบันทึก
- **When (เมื่อ):** API ตอบ Unauthorized
- **Then (ระบบต้อง):** ระบบต้องไม่สร้างข้อมูลในชื่อผู้ใช้อื่นและควรแจ้งให้ Login ใหม่โดยรักษาข้อมูลในหน้าเท่าที่ปลอดภัย
#### US-DRF-003-AC-06

- **Given (กำหนดให้):** บันทึก Draft สำเร็จ
- **When (เมื่อ):** มีการแก้ไขข้อมูล
- **Then (ระบบต้อง):** ระบบต้องบันทึก Updated By/At และ Audit Event ตามระดับรายละเอียดที่กำหนด

### Notes / Open Decisions

- Autosave เป็นฟังก์ชันเสริม; Manual Save เป็น Core Requirement

---



<div style="page-break-after: always;"></div>

<a id="review-and-submit"></a>
# 09 — Review และ Submit ผลการประเมิน

## US-SUB-001 — ตรวจสอบผลก่อนส่ง
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการตรวจคะแนนและความคิดเห็นก่อนส่ง เพื่อยืนยันว่าข้อมูลถูกต้องและครบถ้วน

**คุณค่าทางธุรกิจ:** ลดการส่งคะแนนผิดและทำให้ผู้ประเมินเห็นผลรวมก่อนล็อกข้อมูล

### Preconditions

- Evaluation เป็น Draft และเป็นของผู้ใช้

### Acceptance Criteria

#### US-SUB-001-AC-01

- **Given (กำหนดให้):** Evaluator เลือก Review
- **When (เมื่อ):** ระบบตรวจข้อมูล
- **Then (ระบบต้อง):** ต้องตรวจว่า Criterion ที่ Required มีค่าครบและทุกคะแนนอยู่ในช่วงที่กำหนด
#### US-SUB-001-AC-02

- **Given (กำหนดให้):** ข้อมูลไม่ครบหรือผิดช่วง
- **When (เมื่อ):** ระบบสร้าง Review
- **Then (ระบบต้อง):** ต้องไม่อนุญาตไปขั้น Confirm และแสดงรายการ Criterion/Field ที่ต้องแก้
#### US-SUB-001-AC-03

- **Given (กำหนดให้):** ข้อมูลผ่าน Validation
- **When (เมื่อ):** เปิด Review Page
- **Then (ระบบต้อง):** ต้องแสดงข้อมูลผู้สมัคร เกณฑ์ คะแนนรายข้อ คะแนนรวมชั่วคราวตามกฎ และความคิดเห็นในรูปแบบ Read-only
#### US-SUB-001-AC-04

- **Given (กำหนดให้):** ข้อมูล Draft เปลี่ยนหลัง Review ถูกเปิด เช่นจาก Tab อื่น
- **When (เมื่อ):** Evaluator กดยืนยัน
- **Then (ระบบต้อง):** ระบบต้องตรวจ Version/Updated At ซ้ำและปฏิเสธหากข้อมูลไม่ตรง เพื่อป้องกันส่งข้อมูลเก่า
#### US-SUB-001-AC-05

- **Given (กำหนดให้):** รอบทุนถูกปิดระหว่าง Review
- **When (เมื่อ):** Evaluator พยายามยืนยัน
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธ Submit และคง Draft ตาม Policy

---

## US-SUB-002 — ยืนยันส่งผลการประเมิน
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน |
| Priority | Must have |

### User Story

> ในฐานะอาจารย์ผู้ประเมิน ฉันต้องการยืนยันส่งผลการประเมิน เพื่อให้ผลของฉันถูกใช้ในการคำนวณสรุป

**คุณค่าทางธุรกิจ:** เปลี่ยนข้อมูลจากแบบร่างเป็นผลที่ตรวจสอบได้และใช้ในกระบวนการอย่างเป็นทางการ

### Preconditions

- Review Validation ผ่าน
- รอบทุนยัง Open
- บัญชี Evaluator Active
- Evaluation เป็น Draft และเป็นของผู้ใช้

### Acceptance Criteria

#### US-SUB-002-AC-01

- **Given (กำหนดให้):** Evaluator ยืนยันส่งและเงื่อนไขยังผ่าน
- **When (เมื่อ):** Backend ประมวลผล Submit
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยนสถานะเป็น `SUBMITTED` บันทึก `submitted_at` และผู้ส่งภายใน Transaction
#### US-SUB-002-AC-02

- **Given (กำหนดให้):** Submit สำเร็จ
- **When (เมื่อ):** Evaluator กลับมาเปิดรายการ
- **Then (ระบบต้อง):** คะแนนและความคิดเห็นต้องเป็น Read-only และไม่สามารถแก้โดยตรง
#### US-SUB-002-AC-03

- **Given (กำหนดให้):** มีข้อมูล Required ขาดหาย คะแนนผิดช่วง รอบไม่ Open หรือบัญชีไม่ Active
- **When (เมื่อ):** Backend ตรวจซ้ำ
- **Then (ระบบต้อง):** ต้องปฏิเสธ Submit โดยคงสถานะ Draft และส่ง Error Code ที่บอกสาเหตุ
#### US-SUB-002-AC-04

- **Given (กำหนดให้):** Submit สำเร็จเป็นคนที่ 1
- **When (เมื่อ):** ระบบอัปเดตสถานะผู้สมัคร
- **Then (ระบบต้อง):** ผู้สมัครต้องยังไม่มี Result Summary ที่สมบูรณ์และสถานะเป็น `IN_PROGRESS`
#### US-SUB-002-AC-05

- **Given (กำหนดให้):** Submit สำเร็จเป็นคนที่ 2 หรือ 3
- **When (เมื่อ):** Transaction Commit
- **Then (ระบบต้อง):** ระบบต้องเรียกกระบวนการคำนวณ/คำนวณใหม่และอัปเดต Summary/Dashboard/Report Data อย่างสอดคล้องกัน
#### US-SUB-002-AC-06

- **Given (กำหนดให้):** ผู้ใช้ส่งคำขอซ้ำจากการกดหลายครั้ง
- **When (เมื่อ):** Evaluation ถูก Submitted แล้ว
- **Then (ระบบต้อง):** ระบบต้องทำงานแบบ Idempotent หรือปฏิเสธซ้ำโดยไม่สร้าง Submission เพิ่ม
#### US-SUB-002-AC-07

- **Given (กำหนดให้):** Submit สำเร็จ
- **When (เมื่อ):** ระบบบันทึก
- **Then (ระบบต้อง):** ต้องมี Audit Event ที่ระบุ Evaluation, ผู้ส่ง, เวลา และ Criteria Version โดยไม่เก็บ Token/ข้อมูลลับ

---

## US-SUB-003 — ร้องขอเปิดผล Submitted เพื่อแก้ไข
| รายการ | รายละเอียด |
|---|---|
| Actor | อาจารย์ผู้ประเมิน / ผู้ดูแลระบบ / ผู้อนุมัติ |
| Priority | Should have |
| Decision Reference | RD-008 |

### User Story

> ในฐานะผู้ประเมินที่พบข้อผิดพลาดหลังส่ง ฉันต้องการร้องขอ Reopen พร้อมเหตุผล เพื่อแก้ไขอย่างมีการอนุมัติและตรวจสอบย้อนหลังได้

**คุณค่าทางธุรกิจ:** แก้ข้อผิดพลาดโดยไม่ทำลายหลักฐานเดิมหรือเปลี่ยนคะแนนอย่างไม่โปร่งใส

### Preconditions

- Evaluation เป็น Submitted
- รอบทุนยังไม่ Closed หรือมีการเปิดรอบตามกระบวนการที่อนุมัติ

### Acceptance Criteria

#### US-SUB-003-AC-01

- **Given (กำหนดให้):** เจ้าของ Evaluation หรือ Admin สร้างคำขอ
- **When (เมื่อ):** กรอกเหตุผลและข้อมูลอ้างอิงครบ
- **Then (ระบบต้อง):** ระบบต้องสร้าง Reopen Request สถานะ Pending โดยยังไม่ปลดล็อกคะแนน; Head/delegate decision is independent
#### US-SUB-003-AC-02

- **Given (กำหนดให้):** ผู้มีอำนาจอนุมัติอนุมัติคำขอ
- **When (เมื่อ):** ระบบดำเนินการ Reopen
- **Then (ระบบต้อง):** ต้องเก็บ Snapshot/Revision ของคะแนน ความคิดเห็น สถานะ และเวลาเดิมก่อนเปลี่ยนกลับเป็นสถานะที่แก้ไขได้
#### US-SUB-003-AC-03

- **Given (กำหนดให้):** คำขอถูกปฏิเสธ
- **When (เมื่อ):** ผู้อนุมัติบันทึกผล
- **Then (ระบบต้อง):** Evaluation ต้องคง Submitted และบันทึกเหตุผลการปฏิเสธ
#### US-SUB-003-AC-04

- **Given (กำหนดให้):** รอบทุน Closed
- **When (เมื่อ):** มีคำขอ Reopen
- **Then (ระบบต้อง):** ระบบต้องไม่เปิด Evaluation โดยตรงจนกว่าจะผ่านนโยบายเปิดรอบ/อนุมัติที่กำหนด
#### US-SUB-003-AC-05

- **Given (กำหนดให้):** Evaluation ที่ Reopen ถูก Submit ใหม่
- **When (เมื่อ):** Submit สำเร็จ
- **Then (ระบบต้อง):** ระบบต้องสร้าง Revision ใหม่/อัปเดตสถานะตาม Policy และคำนวณ Result Summary, Dashboard และรายงานใหม่
#### US-SUB-003-AC-06

- **Given (กำหนดให้):** ทุกการร้องขอ อนุมัติ ปฏิเสธ และ Submit ใหม่
- **When (เมื่อ):** เหตุการณ์เกิดขึ้น
- **Then (ระบบต้อง):** ต้องบันทึกผู้ดำเนินการ เวลา เหตุผล และความสัมพันธ์ระหว่าง Revision ใน Audit Log

---



<div style="page-break-after: always;"></div>

<a id="score-calculation"></a>
# 10 — คำนวณคะแนนและสรุปผล

## US-SCR-001 — คำนวณคะแนนรวมรายผู้ประเมิน
| รายการ | รายละเอียด |
|---|---|
| Actor | ระบบ / ผู้ดูแลระบบ / อาจารย์ผู้ประเมิน |
| Priority | Must have |
| Decision Reference | RD-010, RD-011 |

### User Story

> ในฐานะผู้ใช้งานที่ได้รับสิทธิ์ ฉันต้องการเห็นคะแนนรวมของผู้ประเมินแต่ละคนที่คำนวณจากคะแนนรายเกณฑ์ เพื่อใช้ตรวจสอบผลก่อนรวมคะแนนผู้สมัคร

**คุณค่าทางธุรกิจ:** ลดการใช้สูตร Excel และทำให้สูตรเดียวกันถูกใช้ทั่วระบบ

### Preconditions

- Evaluation มีคะแนนรายเกณฑ์และ Criteria Version ที่อ้างอิง

### Acceptance Criteria

#### US-SCR-001-AC-01

- **Given (กำหนดให้):** Evaluation ยังเป็น Draft
- **When (เมื่อ):** ระบบแสดงคะแนนรวมชั่วคราว
- **Then (ระบบต้อง):** ระบบอาจแสดง Preview ได้ แต่ต้องติดป้าย Draft และห้ามนำไปใช้ใน Result Summary/Dashboard/Report Final
#### US-SCR-001-AC-02

- **Given (กำหนดให้):** Evaluation เป็น Submitted
- **When (เมื่อ):** ระบบคำนวณคะแนนรายผู้ประเมิน
- **Then (ระบบต้อง):** ต้องใช้คะแนนรายเกณฑ์และกฎจาก Criteria Version ของ Evaluation นั้นเท่านั้น
#### US-SCR-001-AC-03

- **Given (กำหนดให้):** Criterion มีน้ำหนัก
- **When (เมื่อ):** คำนวณ
- **Then (ระบบต้อง):** ระบบต้องใช้ Embedded Point sum and equal-weight 2–3 Submitted arithmetic mean from the bound Criteria Version
#### US-SCR-001-AC-04

- **Given (กำหนดให้):** เกิดคะแนนผิดช่วง ข้อมูลเกณฑ์ไม่ครบ หรือสูตรไม่พร้อม
- **When (เมื่อ):** คำนวณ
- **Then (ระบบต้อง):** ระบบต้องไม่สร้างคะแนนรวมที่ถือว่า Valid และต้องบันทึก Calculation Error ให้ Admin ตรวจสอบ
#### US-SCR-001-AC-05

- **Given (กำหนดให้):** คำนวณสำเร็จ
- **When (เมื่อ):** แสดงผล
- **Then (ระบบต้อง):** ต้องแสดงความละเอียดทศนิยมตาม Display Rule และเก็บค่าคำนวณด้วย Precision ที่เพียงพอก่อนปัดขั้นสุดท้าย

---

## US-SCR-002 — สร้างคะแนนสรุปเมื่อ Submitted ครบ 2 คน
| รายการ | รายละเอียด |
|---|---|
| Actor | ระบบ / ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-004, RD-006, RD-010, RD-011 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการให้ระบบคำนวณคะแนนสรุปเมื่อมีผล Submitted จากผู้ประเมินไม่ซ้ำกันครบ 2 คน เพื่อทราบว่าผู้สมัครครบขั้นต่ำแล้ว

**คุณค่าทางธุรกิจ:** ลดการรวบรวมและเฉลี่ยคะแนนด้วยมือ

### Preconditions

- มี Evaluation ที่ยังไม่ถูกยกเลิกของผู้สมัครในรอบเดียวกัน
- มี Submitted จากผู้ประเมินไม่ซ้ำกัน 2 รายการ

### Acceptance Criteria

#### US-SCR-002-AC-01

- **Given (กำหนดให้):** Submitted น้อยกว่า 2
- **When (เมื่อ):** ระบบประมวลผลสถานะ
- **Then (ระบบต้อง):** ต้องไม่สร้าง Final/Latest Summary ที่สมบูรณ์และสถานะเป็น `NOT_STARTED` หรือ `IN_PROGRESS` ตาม Active Evaluation
#### US-SCR-002-AC-02

- **Given (กำหนดให้):** Submitted ครบ 2 และรอบยัง Open
- **When (เมื่อ):** Submission คนที่ 2 Commit
- **Then (ระบบต้อง):** ระบบต้องคำนวณ Result Summary จาก Submitted ทั้ง 2 และกำหนดสถานะ `MINIMUM_COMPLETE`
#### US-SCR-002-AC-03

- **Given (กำหนดให้):** มี Draft หรือ Cancelled เพิ่มเติม
- **When (เมื่อ):** คำนวณ Summary
- **Then (ระบบต้อง):** ต้องไม่นำรายการเหล่านั้นเข้าฐานการคำนวณ
#### US-SCR-002-AC-04

- **Given (กำหนดให้):** ผู้ประเมินคนเดียวมีข้อมูลซ้ำจากความผิดปกติ
- **When (เมื่อ):** ระบบรวมผล
- **Then (ระบบต้อง):** ต้องตรวจความไม่ซ้ำของ Evaluator และหยุด/แจ้ง Data Integrity Error แทนการนับซ้ำ
#### US-SCR-002-AC-05

- **Given (กำหนดให้):** มี Summary อยู่แล้ว
- **When (เมื่อ):** เกิด Recompute
- **Then (ระบบต้อง):** ผู้สมัครหนึ่งคนต้องมี Result Summary ได้ไม่เกินหนึ่งรายการต่อรอบ และการอัปเดตต้องเป็น Atomic
#### US-SCR-002-AC-06

- **Given (กำหนดให้):** สูตรและการปัดเศษถูกกำหนด
- **When (เมื่อ):** คำนวณ
- **Then (ระบบต้อง):** ใช้สูตรเดียวกันกับ Report/Dashboard, retain full precision, round only applicant summary with `ROUND_HALF_UP`, and keep calculation version/inputs

---

## US-SCR-003 — คำนวณผลใหม่เมื่อผู้ประเมินคนที่ 3 Submit
| รายการ | รายละเอียด |
|---|---|
| Actor | ระบบ / ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-005, RD-010, RD-011 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการให้คะแนนสรุปคำนวณใหม่เมื่อผู้ประเมินคนที่ 3 ส่งผล เพื่อให้ข้อมูลล่าสุดตรงกันทุกหน้าและรายงาน

**คุณค่าทางธุรกิจ:** รองรับผู้ประเมินสูงสุด 3 คนโดยไม่ต้องแก้สูตรหรือไฟล์ด้วยมือ

### Preconditions

- รอบทุนยัง Open
- มี Result Summary จาก Submitted 2 คน
- Submission คนที่ 3 เป็นของผู้ประเมินที่ไม่ซ้ำ

### Acceptance Criteria

#### US-SCR-003-AC-01

- **Given (กำหนดให้):** Submission คนที่ 3 Commit สำเร็จ
- **When (เมื่อ):** ระบบเรียก Recalculation
- **Then (ระบบต้อง):** ต้องคำนวณจาก Submitted ทั้ง 3 รายการและเปลี่ยนสถานะเป็น `FULLY_COMPLETE`
#### US-SCR-003-AC-02

- **Given (กำหนดให้):** มี Summary จาก 2 คน
- **When (เมื่อ):** คำนวณใหม่
- **Then (ระบบต้อง):** ระบบต้องปรับปรุงคะแนน จำนวน Submitted รายชื่อผู้ประเมิน และเวลาคำนวณล่าสุดภายใน Transaction/กระบวนการที่สอดคล้อง
#### US-SCR-003-AC-03

- **Given (กำหนดให้):** Recalculation สำเร็จ
- **When (เมื่อ):** ผู้ใช้เปิด Dashboard Result Summary หรือ Export
- **Then (ระบบต้อง):** ทุกส่วนต้องแสดงค่าใหม่เดียวกันและไม่มีหน้าหนึ่งยังใช้ค่า 2 คน
#### US-SCR-003-AC-04

- **Given (กำหนดให้):** Submission คนที่ 3 ถูก Reopen/ยกเลิกตาม Policy
- **When (เมื่อ):** สถานะที่ใช้คำนวณเปลี่ยน
- **Then (ระบบต้อง):** ระบบต้อง Recompute ตาม Submitted ที่เหลือและอัปเดตสถานะอย่างถูกต้อง
#### US-SCR-003-AC-05

- **Given (กำหนดให้):** Recalculation ล้มเหลว
- **When (เมื่อ):** Submission ถูกบันทึกแล้วแต่ Summary ยังไม่สำเร็จ
- **Then (ระบบต้อง):** ระบบต้องบันทึกสถานะให้ตรวจพบและ Retry/แจ้ง Admin โดยไม่แสดงคะแนนสรุปที่เงียบ ๆ ว่าถูกต้อง

---



<div style="page-break-after: always;"></div>

<a id="close-round"></a>
# 11 — ปิดรอบทุน

## US-CLS-001 — ตรวจสอบและปิดรอบทุน
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการตรวจสถานะผู้สมัครและปิดรอบทุน เพื่อยุติการรับผลเพิ่มเติมและกำหนดผลล่าสุดเป็นผลของรอบ

**คุณค่าทางธุรกิจ:** ทำให้มีจุดตัดที่ชัดเจนสำหรับรายงานและการส่งมอบผล

### Preconditions

- รอบทุนอยู่ในสถานะ Open
- Admin มีสิทธิ์ปิดรอบ

### Acceptance Criteria

#### US-CLS-001-AC-01

- **Given (กำหนดให้):** Admin เปิดหน้าปิดรอบ
- **When (เมื่อ):** ระบบสรุปข้อมูล
- **Then (ระบบต้อง):** ต้องแสดงจำนวนผู้สมัครตาม Submitted 0/1/2/3 และสถานะ `NOT_STARTED`/`IN_PROGRESS`/`MINIMUM_COMPLETE`/`FULLY_COMPLETE` ก่อนยืนยัน
#### US-CLS-001-AC-02

- **Given (กำหนดให้):** มีผู้สมัคร Submitted ไม่ครบ 2
- **When (เมื่อ):** Admin ยืนยันปิด
- **Then (ระบบต้อง):** ระบบต้องแสดงคำเตือนและจำนวน `CLOSED_INCOMPLETE` อย่างชัดเจน แต่การอนุญาตให้ปิดเป็นไปตามนโยบายงานทุน
#### US-CLS-001-AC-03

- **Given (กำหนดให้):** Admin ยืนยันปิดรอบ
- **When (เมื่อ):** Transaction/Close Process สำเร็จ
- **Then (ระบบต้อง):** ระบบต้องเปลี่ยนรอบเป็น `CLOSED` และบันทึกผู้ปิด เวลา และ Summary Snapshot/Version ที่เกี่ยวข้อง
#### US-CLS-001-AC-04

- **Given (กำหนดให้):** รอบถูก Closed
- **When (เมื่อ):** Evaluator พยายามสร้าง Evaluation บันทึกการแก้ไขใหม่ หรือ Submit เพิ่ม
- **Then (ระบบต้อง):** ระบบต้องปฏิเสธทุกคำขอที่เปลี่ยนผล เว้นแต่ผ่าน Reopen Policy
#### US-CLS-001-AC-05

- **Given (กำหนดให้):** มีคำขอ Submit/Select แข่งขันกับการปิดรอบ
- **When (เมื่อ):** ระบบประมวลผลพร้อมกัน
- **Then (ระบบต้อง):** ต้องมีลำดับ Transaction ที่ทำให้สถานะสุดท้ายสอดคล้องและไม่รับ Submission หลังเวลาปิดอย่างเงียบ ๆ
#### US-CLS-001-AC-06

- **Given (กำหนดให้):** ปิดรอบสำเร็จ
- **When (เมื่อ):** ผู้ใช้เปิด Dashboard/Report
- **Then (ระบบต้อง):** ต้องสะท้อนสถานะ Finalized/`CLOSED_INCOMPLETE` ตามกฎเดียวกัน

---

## US-CLS-002 — กำหนดผลหลังปิดรอบ
| รายการ | รายละเอียด |
|---|---|
| Actor | ระบบ / ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-006, RD-007, RD-008 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการให้ระบบกำหนดสถานะผู้สมัครหลังปิดรอบอัตโนมัติ เพื่อแยกผู้ที่มีผลครบจากผู้ที่ไม่มีผลสรุปสุดท้าย

**คุณค่าทางธุรกิจ:** ป้องกันการตีความคะแนนไม่ครบเป็นผลสุดท้าย

### Preconditions

- รอบทุนเปลี่ยนเป็น Closed

### Acceptance Criteria

#### US-CLS-002-AC-01

- **Given (กำหนดให้):** ผู้สมัครมี Submitted อย่างน้อย 2 รายการ
- **When (เมื่อ):** รอบปิด
- **Then (ระบบต้อง):** ระบบต้องกำหนดสถานะ `FINALIZED` และถือ Result Summary ล่าสุดเป็นผลสุดท้ายของรอบ
#### US-CLS-002-AC-02

- **Given (กำหนดให้):** ผู้สมัครมี Submitted 0 หรือ 1 รายการ
- **When (เมื่อ):** รอบปิด
- **Then (ระบบต้อง):** ระบบต้องกำหนดสถานะ `CLOSED_INCOMPLETE` และต้องไม่มี Final Score
#### US-CLS-002-AC-03

- **Given (กำหนดให้):** `CLOSED_INCOMPLETE` มีคะแนนรายผู้ประเมินบางส่วน
- **When (เมื่อ):** Admin เปิดดูตามสิทธิ์
- **Then (ระบบต้อง):** ระบบอาจแสดงคะแนนรายรายการเพื่อ Audit แต่ต้องไม่แสดงเป็นคะแนนสรุปสุดท้าย
#### US-CLS-002-AC-04

- **Given (กำหนดให้):** รอบปิดแล้ว
- **When (เมื่อ):** ผู้ประเมินคนที่ 3 พยายามเริ่มหรือ Submit
- **Then (ระบบต้อง):** ต้องปฏิเสธจนกว่าจะมีการเปิดรอบตามกระบวนการอนุมัติ
#### US-CLS-002-AC-05

- **Given (กำหนดให้):** มี Reopen ที่ได้รับอนุมัติภายหลัง
- **When (เมื่อ):** ข้อมูล Submitted เปลี่ยนและรอบถูกปิดใหม่
- **Then (ระบบต้อง):** ระบบต้องคำนวณและ Finalize ใหม่พร้อมเก็บ immutable Revision/Audit เดิมและ Superseded report history

---



<div style="page-break-after: always;"></div>

<a id="dashboard"></a>
# 12 — Dashboard

## US-DSH-001 — ดูภาพรวมสถานะการประเมิน
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการดูจำนวนผู้สมัครและสถานะการประเมินของรอบทุน เพื่อทราบว่างานค้างอยู่ตรงไหน

**คุณค่าทางธุรกิจ:** ช่วยติดตามความครบถ้วนก่อนปิดรอบโดยไม่ต้องรวม Excel

### Preconditions

- Admin Login
- เลือกรอบทุนหรือระบบกำหนดรอบเริ่มต้นตาม UX

### Acceptance Criteria

#### US-DSH-001-AC-01

- **Given (กำหนดให้):** Admin เลือกรอบทุน
- **When (เมื่อ):** Dashboard โหลด
- **Then (ระบบต้อง):** ต้องแสดงจำนวนผู้สมัครทั้งหมดและจำนวนที่มี Submitted 0, 1, 2 และ 3 คน
#### US-DSH-001-AC-02

- **Given (กำหนดให้):** Dashboard โหลด
- **When (เมื่อ):** ระบบ Aggregate
- **Then (ระบบต้อง):** ต้องแสดงจำนวน `NOT_STARTED`, `IN_PROGRESS`, `MINIMUM_COMPLETE`, `FULLY_COMPLETE`, Finalized และ `CLOSED_INCOMPLETE` ตามสถานะรอบและ Submitted
#### US-DSH-001-AC-03

- **Given (กำหนดให้):** มี Draft หรือ Cancelled
- **When (เมื่อ):** คำนวณกราฟ/ตัวชี้วัดคะแนน
- **Then (ระบบต้อง):** ต้องไม่ใช้คะแนนจาก Draft/Cancelled ใน Visualization ด้านคะแนน
#### US-DSH-001-AC-04

- **Given (กำหนดให้):** ข้อมูลอยู่คนละรอบ
- **When (เมื่อ):** Admin เปลี่ยน Filter รอบทุน
- **Then (ระบบต้อง):** ต้องแยก Aggregate โดย round_id และไม่มีข้อมูลข้ามรอบปะปน
#### US-DSH-001-AC-05

- **Given (กำหนดให้):** Admin ไม่มีสิทธิ์เข้าถึง Dashboard รวม
- **When (เมื่อ):** เรียก API
- **Then (ระบบต้อง):** ระบบต้องตอบ `403` และไม่ส่ง Aggregate ที่อาจเปิดเผยข้อมูล

---

## US-DSH-002 — กรองและเจาะดูรายการจาก Dashboard
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการกดจากตัวเลขสถานะไปยังรายชื่อผู้สมัคร เพื่อดำเนินการติดตามได้ทันที

**คุณค่าทางธุรกิจ:** เปลี่ยน Dashboard จากภาพรวมเป็นเครื่องมือปฏิบัติงาน

### Preconditions

- Dashboard โหลดข้อมูลสำเร็จ

### Acceptance Criteria

#### US-DSH-002-AC-01

- **Given (กำหนดให้):** Admin กดจำนวน Submitted 1 หรือสถานะ `IN_PROGRESS`
- **When (เมื่อ):** ระบบเปิดรายการรายละเอียด
- **Then (ระบบต้อง):** ต้องกรองผู้สมัครตามนิยามเดียวกับตัวเลขบน Dashboard
#### US-DSH-002-AC-02

- **Given (กำหนดให้):** Submission คนที่ 2/3 สำเร็จหรือรอบถูกปิด
- **When (เมื่อ):** Dashboard ถูก Refresh/Reload
- **Then (ระบบต้อง):** ตัวเลขและสถานะต้องอัปเดตจากข้อมูลล่าสุดและตรงกับ Result Summary
#### US-DSH-002-AC-03

- **Given (กำหนดให้):** มีการค้นหา/กรอง
- **When (เมื่อ):** Admin เลือกสถานะ จำนวนผู้ประเมิน หรือช่วงคะแนน
- **Then (ระบบต้อง):** ระบบต้องคืนรายการที่ตรงเงื่อนไขและแสดงจำนวนผลทั้งหมด
#### US-DSH-002-AC-04

- **Given (กำหนดให้):** Aggregate Query ล้มเหลว
- **When (เมื่อ):** หน้าโหลด
- **Then (ระบบต้อง):** ระบบต้องแสดง Error State และทางเลือก Retry โดยไม่แสดงข้อมูลเก่าราวกับเป็นข้อมูลปัจจุบัน
#### US-DSH-002-AC-05

- **Given (กำหนดให้):** ข้อมูลคะแนนยังคำนวณไม่สำเร็จ
- **When (เมื่อ):** แสดงรายการ
- **Then (ระบบต้อง):** ระบบต้องแสดงสถานะ Calculation Error/Pending แทนการใช้ค่าเดิมโดยไม่มีคำเตือน

---



<div style="page-break-after: always;"></div>

<a id="report-export"></a>
# 13 — รายงานและ Export

## US-RPT-001 — ส่งออกรายงาน Excel/CSV
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-021, RD-022 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการส่งออกรายงาน Excel หรือ CSV เพื่อใช้ในกระบวนการของคณะและตรวจสอบผลนอกระบบ

**คุณค่าทางธุรกิจ:** ลดการคัดลอกข้อมูลและสูตรด้วยมือ พร้อมให้ข้อมูลส่งต่ออยู่ในรูปแบบมาตรฐาน

### Preconditions

- Admin Login
- เลือกรอบทุนและรูปแบบรายงาน
- ข้อมูล Result Summary พร้อมตามสถานะ

### Acceptance Criteria

#### US-RPT-001-AC-01

- **Given (กำหนดให้):** Admin เลือกรอบทุนและ Export Excel/CSV
- **When (เมื่อ):** ระบบสร้างไฟล์
- **Then (ระบบต้อง):** ไฟล์ต้องประกอบด้วยข้อมูลผู้สมัคร รายชื่อผู้ประเมินที่ Submitted คะแนนรายเกณฑ์ คะแนนรวมรายผู้ประเมิน จำนวน Submitted สถานะ ความคิดเห็น และคะแนนสรุปตามสิทธิ์/Template
#### US-RPT-001-AC-02

- **Given (กำหนดให้):** Evaluation เป็น Draft หรือ Cancelled
- **When (เมื่อ):** ระบบสร้างคะแนนในรายงาน
- **Then (ระบบต้อง):** ต้องไม่รวมรายการดังกล่าวในคะแนนสรุปและต้องไม่แสดงเป็น Submitted
#### US-RPT-001-AC-03

- **Given (กำหนดให้):** รอบยัง Open และผู้สมัครมี Submitted 2
- **When (เมื่อ):** Export
- **Then (ระบบต้อง):** ต้องแสดง `MINIMUM_COMPLETE` และระบุว่าคะแนนเป็นผลล่าสุดที่อาจเปลี่ยนเมื่อคนที่ 3 Submit
#### US-RPT-001-AC-04

- **Given (กำหนดให้):** รอบ Closed และ Submitted อย่างน้อย 2
- **When (เมื่อ):** Export
- **Then (ระบบต้อง):** ต้องแสดง `FINALIZED` และ Final Score ตาม Result Summary ล่าสุด
#### US-RPT-001-AC-05

- **Given (กำหนดให้):** รอบ Closed และ Submitted น้อยกว่า 2
- **When (เมื่อ):** Export
- **Then (ระบบต้อง):** ต้องแสดง `CLOSED_INCOMPLETE` และช่อง Final Score ต้องว่าง/ไม่มีค่า ไม่ใช้ 0 แทน
#### US-RPT-001-AC-06

- **Given (กำหนดให้):** สร้างทั้ง Excel และ CSV ด้วยตัวกรองเดียวกัน
- **When (เมื่อ):** เปรียบเทียบข้อมูล
- **Then (ระบบต้อง):** ค่าหลักต้องตรงกับฐานข้อมูลและ Result Summary รวมถึงสูตร/การปัดเศษเดียวกัน
#### US-RPT-001-AC-07

- **Given (กำหนดให้):** เกิดข้อผิดพลาดระหว่างสร้างไฟล์
- **When (เมื่อ):** Export ล้มเหลว
- **Then (ระบบต้อง):** ระบบต้องไม่ส่งไฟล์บางส่วนที่ดูเหมือนสมบูรณ์ และต้องแสดง Error/Retry ที่ชัดเจน

---

## US-RPT-002 — ควบคุมข้อมูลส่วนบุคคลและบันทึกประวัติ Export
| รายการ | รายละเอียด |
|---|---|
| Actor | ผู้ดูแลระบบ |
| Priority | Must have |
| Decision Reference | RD-021, RD-022 |

### User Story

> ในฐานะผู้ดูแลระบบ ฉันต้องการให้การ Export จำกัดข้อมูลตามวัตถุประสงค์และถูกบันทึกประวัติ เพื่อคุ้มครองข้อมูลผู้สมัครและตรวจสอบย้อนหลังได้

**คุณค่าทางธุรกิจ:** ลดความเสี่ยงจากการส่งออกข้อมูลละเอียดอ่อนเกินจำเป็น

### Preconditions

- Admin มี Permission สำหรับ Report Template ที่เลือก

### Acceptance Criteria

#### US-RPT-002-AC-01

- **Given (กำหนดให้):** Admin เลือก Template มาตรฐาน
- **When (เมื่อ):** ระบบสร้างไฟล์
- **Then (ระบบต้อง):** ต้องส่งออกเฉพาะคอลัมน์ที่กำหนด; Release 1 ห้ามมีเลขบัตรประชาชนและ standard export ห้ามมี applicant contact information
#### US-RPT-002-AC-02

- **Given (กำหนดให้):** Template มีข้อมูล Contact/Restricted
- **When (เมื่อ):** Admin ขอ Export
- **Then (ระบบต้อง):** ระบบตรวจ profile permission; evaluator cannot export peer data; standard export excludes national ID and applicant contact information
#### US-RPT-002-AC-03

- **Given (กำหนดให้):** Export สำเร็จ
- **When (เมื่อ):** ระบบส่งไฟล์
- **Then (ระบบต้อง):** ต้องบันทึกผู้ Export เวลา รอบทุน Template ตัวกรอง จำนวนแถว และผลลัพธ์ใน Audit Log
#### US-RPT-002-AC-04

- **Given (กำหนดให้):** ผู้ใช้ไม่มีสิทธิ์ Template
- **When (เมื่อ):** เรียก API โดยตรง
- **Then (ระบบต้อง):** ระบบต้องตอบ `403` และไม่สร้างไฟล์ชั่วคราวที่เข้าถึงได้
#### US-RPT-002-AC-05

- **Given (กำหนดให้):** ระบบสร้างไฟล์ชั่วคราว
- **When (เมื่อ):** ครบอายุหรือดาวน์โหลดเสร็จตาม Policy
- **Then (ระบบต้อง):** ต้องลบ/หมดอายุไฟล์ชั่วคราวและไม่ใช้ URL สาธารณะถาวร
#### US-RPT-002-AC-06

- **Given (กำหนดให้):** ชื่อไฟล์ถูกสร้าง
- **When (เมื่อ):** ส่งออก
- **Then (ระบบต้อง):** ควรมีรหัสรอบทุน ประเภท Template และ Timestamp โดยไม่ใส่ข้อมูลส่วนบุคคลของผู้สมัครในชื่อไฟล์

---



<div style="page-break-after: always;"></div>

<a id="traceability"></a>
# 14 — Traceability Matrix

ใช้ไฟล์กลาง [SEMS Traceability Matrix](../SEMS_Traceability_Matrix.md) เป็น Source of Truth เพื่อไม่ทำสำเนาตาราง traceability ซ้ำในเอกสารนี้

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.7 | 2026-08-05 | SEMS Documentation Team | ทำ API Error Response Contract ให้ใช้ `code` และ envelope เดียวกับ SRS, API Specification, Error Code Catalog และ OpenAPI |
| v0.6 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.5 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.4 | 2026-07-24 | SEMS Requirements Team | Added measurable confirmed-response stories for multi-type applications, corrections, reopen/cancel, report lifecycle, account/session/file safety and data minimization. |
| v0.3 | 2026-07-24 | SEMS Requirements Team | Replaced retired/non-canonical import aliases with the central allowed error-code inventory. |
| v0.2 | 2026-07-23 | SEMS Requirements Team | Replaced nonexistent per-module files with stable section anchors, linked the central traceability matrix, limited Release 1 import, and aligned provisional round opening. |
| v0.1 | 2026-07-23 | SEMS Requirements Team | Initial consolidated user stories and acceptance criteria draft. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [Software Requirements Specification (SRS)](../SRS/SEMS-SRS.md)<br>
↑ หมวดเอกสาร: [SEMS User Stories](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [SEMS Traceability Matrix](../SEMS_Traceability_Matrix.md)

<!-- DOC_NAV_END -->
