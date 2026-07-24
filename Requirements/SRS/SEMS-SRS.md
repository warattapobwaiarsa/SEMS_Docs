---
document_id: SEMS-SRS-001
title: Software Requirements Specification — Scholarship Evaluation Management System (SEMS)
version: "v0.3"
status: Draft - Pending Requirement Baseline Approval
last_updated: 2026-07-24
owner: SEMS Project Team
author: SEMS Requirements Team
target_path: Requirements/SRS/SEMS-SRS.md
supersedes_on_approval: previous unapproved SEMS_SRS drafts
---

# Software Requirements Specification (SRS)
## Scholarship Evaluation Management System (SEMS)
**ระบบบริหารจัดการการประเมินทุนการศึกษา**

| รายการ | รายละเอียด |
|---|---|
| Version | 0.3-draft |
| วันที่จัดทำ | 24 กรกฎาคม 2026 |
| สถานะ | Baseline Candidate - Pending Formal Approval |
| รูปแบบ | สอดคล้องแนวทาง ISO/IEC/IEEE 29148 ในระดับโครงสร้าง |
| ผลลัพธ์เป้าหมาย | Requirement ที่ออกแบบ พัฒนา และทดสอบได้ |

> เอกสารนี้รวมข้อกำหนดจาก Proposal, Requirement Decision Register, Data Dictionary, Applicant Import Mapping, ไฟล์ Criteria และข้อมูล KKU OAuth/OIDC
> Confirmed stakeholder responses are reflected as testable Release 1 requirements. The document remains a baseline candidate until formal approval evidence is recorded.

## Document History

| Version | Date | Change | Status |
|---|---|---|---|
| 0.3-draft | 2026-07-24 | Synchronized confirmed stakeholder decisions for Release 1 baseline review | Pending Formal Approval |
| 2.2-draft | 2026-07-24 | Aligned all referenced error codes to the canonical allowed inventory and retained embedded-point scoring semantics | Pending Approval |
| 2.1-draft | 2026-07-23 | Reconciled provisional round opening, Release 1 import, embedded-point scoring, canonical error contract/codes and traceability | Pending Approval |
| 2.0-draft | 2026-07-23 | ปรับ SRS ให้ตรงกับ Proposal ล่าสุด: ผู้ประเมิน 2-3 คน, self-selection, KKU SSO, import mapping, criteria versioning, result status และ audit | Pending Approval |

# 1. บทนำ

## 1.1 วัตถุประสงค์

เอกสารนี้แปลงภาพรวมและขอบเขตของ SEMS ให้เป็น Requirement ที่มีรหัส เงื่อนไข ผลลัพธ์ และเกณฑ์ตรวจรับชัดเจน เพื่อใช้เป็นฐานสำหรับ:

- ออกแบบ Architecture, ER Diagram, Prisma Schema, REST API และ UI
- จัดทำ Backlog, Test Case, Integration Test, End-to-End Test และ UAT
- ควบคุม Scope และตรวจสอบ Traceability ระหว่างเอกสารกับระบบจริง
- แยกข้อกำหนดที่ยืนยันแล้วออกจากข้อเสนอที่ยังรอการตัดสินใจ

## 1.2 ขอบเขตระบบ

SEMS เป็น Web Application ภายในคณะวิศวกรรมศาสตร์ มหาวิทยาลัยขอนแก่น สำหรับจัดการกระบวนการประเมินทุน ตั้งแต่การจัดการรอบทุน นำเข้าข้อมูลผู้สมัครและประวัติ อัปโหลดเอกสาร กำหนดเกณฑ์ ให้อาจารย์ค้นหาและเลือกผู้สมัคร บันทึก Draft และ Submit ผล คำนวณคะแนนจากผู้ประเมิน 2-3 คน ติดตามสถานะ แสดง Dashboard และส่งออก Excel/CSV

ผู้ใช้งานหลักมี 2 บทบาท: `ADMIN` และ `EVALUATOR` นักศึกษาผู้สมัครไม่มีบัญชีเข้าใช้ SEMS ในขอบเขตนี้

## 1.3 คำสำคัญ

| คำ | ความหมาย |
|---|---|
| Active Evaluation | Evaluation ที่ยังไม่ถูกยกเลิก; ใช้นับ Capacity สูงสุด 3 คน |
| Draft | ผลประเมินที่ยังไม่ Submit และห้ามใช้คำนวณ |
| Submitted | ผลประเมินที่ยืนยันส่งแล้วและใช้คำนวณได้ |
| Cancelled | Evaluation ที่ยกเลิกแล้ว ไม่นับ Capacity และไม่คำนวณ |
| Criteria Version | ชุดเกณฑ์ที่ถูก Version และผูกกับ Evaluation |
| Result Summary | คะแนนสรุปต่อผู้สมัครต่อรอบทุน |
| Latest Score | คะแนนจาก Submitted 2-3 คนขณะที่รอบยัง Open |
| Final Score | Latest Score ที่ยืนยันเป็นผลสุดท้ายเมื่อรอบ Closed |
| Confirmed | มีหลักฐานชัดใน Proposal/Decision ที่ยืนยันแล้ว |
| Provisional | ข้อเสนอที่ทำให้ Requirement ทดสอบได้ แต่ยังต้องอนุมัติ |
| Open | ยังไม่มีคำตอบและต้องตัดสินใจก่อน Baseline |

## 1.4 เอกสารอ้างอิง

1. [`SEMS-project-proposal.pdf`](../Proposal/SEMS-project-proposal.pdf)
2. [`SEMS_Requirement_Decision_Analysis.md`](../SEMS_Requirement_Decision_Analysis.md)
3. `SEMS_Data_Dictionary.xlsx` และ Data Dictionary/Import Mapping Draft
4. [`SEMS_Applicant_Import_Mapping_Specification.md`](../../Design/Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md) และ workbook ประกอบ
5. [`Criteria.xlsx`](../../Design/Criteria/Criteria.xlsx)
6. `kku-oauth-summary.md`

## 1.5 กติกาการเขียน Requirement

- รหัส Functional Requirement ใช้ `FR-<MODULE>-NNN`
- Priority: `Must have`, `Should have`, `Nice to have`
- Status: `Confirmed`, `Provisional`, `Open`
- API Error ต้องส่ง `{code, message, details[], traceId, timestamp}` ตาม [`SEMS_Error_Code_Catalog.md`](../../Design/API/SEMS_Error_Code_Catalog.md) โดยไม่มี object `error` ครอบ
- Backend เป็นผู้ตัดสิน Validation และ Authorization สุดท้าย
- Requirement `Open` ห้ามนำไป Freeze เป็น Baseline โดยไม่มี Decision Record

# 2. ภาพรวมระบบ

## 2.1 Core Workflow

```text
ADMIN สร้างรอบทุนและเกณฑ์
    -> นำเข้าผู้สมัครและตรวจ Preview
    -> อัปโหลดเอกสาร
    -> เปิดรอบทุน
EVALUATOR Login ผ่าน KKU SSO
    -> ค้นหาและเลือกผู้สมัคร
    -> ระบบสร้าง Evaluation โดยควบคุมไม่เกิน 3 คน
    -> ดูข้อมูล/เอกสาร -> กรอกคะแนน -> Save Draft -> Review -> Submit
ระบบใช้เฉพาะ Submitted
    -> ครบ 2 คน: Minimum Complete + Latest Score
    -> คนที่ 3 Submit: Recalculate + Fully Complete
ADMIN ปิดรอบ
    -> Finalized หรือ Closed Incomplete
    -> Dashboard / Excel / CSV / Audit
```

## 2.2 External Interfaces

| Interface | ข้อกำหนด |
|---|---|
| KKU SSO | OAuth 2.1 + OIDC, Authorization Code, PKCE S256, Discovery, JWKS, UserInfo, Logout/Revocation ตามที่อนุมัติ |
| Frontend | Next.js + TypeScript; Browser เป็น Client |
| Backend | NestJS REST API + TypeScript |
| Database | PostgreSQL ผ่าน Prisma |
| File Storage | Private Server Storage หรือ Object Storage |
| Import | XLSX และ CSV |
| Export | XLSX และ CSV; PDF เป็น Optional |
| Timezone | เก็บ Timestamp แบบ Timestamptz/UTC; แสดง Asia/Bangkok |

## 2.3 ข้อจำกัดและสิ่งที่ไม่อยู่ในขอบเขต

- ไม่มีระบบสมัครทุนออนไลน์สำหรับนักศึกษา
- ไม่มีการพิจารณาอนุมัติทุนขั้นสุดท้ายระดับนโยบาย การประกาศผล หรือการโอนเงิน
- ไม่มีการเชื่อมฐานข้อมูลระบบทุนเดิมโดยตรงใน Release แรก
- ไม่มีการแก้ Submitted โดยไม่มีกระบวนการ Reopen/Approval
- ไม่มี Native Mobile Application และไม่เก็บ Binary Document ใน PostgreSQL
- ไม่มีการจัดคิวสัมภาษณ์หรือจัดการห้องประชุมออนไลน์
- อาจารย์เลือกผู้สมัครที่กำลังสัมภาษณ์ด้วยตนเอง ไม่ใช่การมอบหมายล่วงหน้าเป็น Core Flow

# 3. Functional Requirements


## 3.1 Authentication, SSO และการจัดการผู้ใช้งาน

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-AUT-001 | Must have | Confirmed | เมื่อผู้ใช้กดเข้าสู่ระบบ ระบบต้องเริ่ม OIDC Authorization Code Flow ผ่าน KKU SSO โดยอ่าน Endpoint จาก OIDC Discovery ใช้ `scope=openid profile email`, `state`, `nonce` และ PKCE `S256`. | ผู้ใช้ยังไม่มี Session | Redirect ไป KKU SSO พร้อมพารามิเตอร์ครบ และ SEMS ไม่รับ/เก็บรหัสผ่าน KKU |
| FR-AUT-002 | Must have | Confirmed | ระบบต้องตรวจ `state`, `nonce`, authorization code, PKCE verifier, issuer, audience, signature และอายุ Token ก่อนสร้าง Session. | ได้รับ Callback | Callback ผิดต้องถูกปฏิเสธและไม่มี Session |
| FR-AUT-003 | Must have | Confirmed | ระบบต้องใช้ Claim ที่คงที่ เช่น `sub` เป็นตัวระบุตัวตนหลักสำหรับเชื่อม KKU Identity กับ SEMS User. | Token ผ่านการตรวจ | ผู้ใช้เดิมเชื่อมบัญชีเดิมแม้ชื่อ/email เปลี่ยน |
| FR-AUT-004 | Must have | Confirmed | หลังยืนยันตัวตน ระบบต้องตรวจว่ามี SEMS User ที่เชื่อมและสถานะ `ACTIVE`; ถ้าไม่พบหรือ Inactive ต้องปฏิเสธ. | Identity ถูกต้อง | คืน `USER_NOT_PROVISIONED` หรือ `USER_INACTIVE` และ Audit |
| FR-AUT-005 | Must have | Confirmed | ระบบต้องรองรับ `ADMIN` และ `EVALUATOR` และตรวจสิทธิ์ Menu, Page, API และข้อมูลที่ Backend ทุกคำขอ. | มี Session | เข้าถึงเฉพาะทรัพยากรที่ Role/Ownership อนุญาต |
| FR-AUT-006 | Must have | Confirmed | EVALUATOR ต้องสร้าง แก้ Draft ยกเลิก Draft และ Submit ได้เฉพาะ Evaluation ของตน และห้ามแก้ของคนอื่น. | EVALUATOR | การเข้าถึงข้ามเจ้าของเป็น 403 `EVALUATION_NOT_OWNER` |
| FR-AUT-007 | Must have | Confirmed | ADMIN ต้องเชื่อม KKU Account กับ SEMS User กำหนด Role และเปิด/ปิดสิทธิ์ โดยไม่จัดการรหัสผ่าน KKU. | ADMIN | User/Role/Status/Identity Link ถูกบันทึกพร้อม Audit |
| FR-AUT-008 | Must have | Confirmed Response | Session ใช้ Secure, HttpOnly, appropriate SameSite Cookie; idle 30 นาที, absolute 8 ชั่วโมง และ Admin revoke ได้. | Login สำเร็จ | Session หมดอายุตามกฎและ Token ไม่เปิดแก่ JavaScript |
| FR-AUT-009 | Must have | Confirmed | Logout ต้องยกเลิก Session SEMS และใช้ Revocation/KKU Logout ตามนโยบายที่อนุมัติ. | มี Session | Session เดิมเรียก API ไม่ได้ |
| FR-AUT-010 | Must have | Confirmed | บันทึก `LOGIN_SUCCESS`, `LOGIN_FAILURE`, `LOGOUT`, `ACCESS_DENIED`, Activation/Deactivation โดยห้ามบันทึก Password, Token, Secret หรือ Code. | เกิดเหตุการณ์ | Audit มีผู้ใช้ เวลา ผล และ Request ID โดยไม่มีข้อมูลลับ |

## 3.2 การจัดการรอบทุน

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-RND-001 | Must have | Confirmed | ADMIN ต้องสร้างรอบทุนด้วยรหัส ชื่อ ปีการศึกษา ช่วงเวลา และสถานะเริ่ม `DRAFT`. | ข้อมูลถูกต้อง | สร้างสำเร็จและรหัสไม่ซ้ำ |
| FR-RND-002 | Must have | Confirmed | รองรับ `DRAFT`, `OPEN`, `CLOSED`, `ARCHIVED` และตรวจ State Transition ตาม Validation Rules. | รอบมีอยู่ | Transition ผิดถูกปฏิเสธ `INVALID_ROUND_STATUS_TRANSITION` |
| FR-RND-003 | Must have | Confirmed | ก่อน `OPEN` ต้องมี Criteria Version `ACTIVE` และข้อมูลจำเป็นต่อการประเมินครบ. | รอบ DRAFT | ผ่านจึงเปิด; ไม่ผ่านแสดงรายการที่ขาด |
| FR-RND-004 | Must have | Confirmed | Applicant, Document, Criteria, Evaluation, Result, Dashboard และ Report ต้องแยกตาม `round_id`. | อ่าน/เขียนข้อมูล | ไม่มีข้อมูลข้ามรอบ |
| FR-RND-005 | Must have | Confirmed | รอบ `CLOSED` ห้ามสร้าง Evaluation, บันทึก Draft ใหม่ หรือ Submit เพิ่ม เว้นแต่เปิดใหม่ตามกระบวนการอนุมัติ. | รอบ CLOSED | ปฏิเสธ `ROUND_NOT_OPEN` |
| FR-RND-006 | Must have | Confirmed | เมื่อปิดรอบ ผู้มี Submitted >=2 เป็น `FINALIZED`; น้อยกว่า 2 เป็น `CLOSED_INCOMPLETE` และไม่มี Final Score. | ADMIN ปิดรอบ | สถานะทุก Applicant ถูกประมวลผลถูกต้อง |
| FR-RND-007 | Must have | Confirmed | ห้าม Hard Delete รอบที่มี Evaluation; จำกัดการแก้ข้อมูลที่กระทบผล และใช้ `ARCHIVED` เพื่อเก็บย้อนหลัง. | มี Evaluation | ข้อมูลเดิมยังตรวจสอบได้ |
| FR-RND-008 | Must have | Confirmed Response | การเปิด CLOSED กลับ OPEN เป็น exceptional Controlled Reopen: ต้องมีคำขอ เหตุผล เลขอ้างอิง ผู้อนุมัติ Audit และรายงานเดิมเป็น immutable `Superseded`; `ARCHIVED` เปิดไม่ได้. | รอบ CLOSED | เปิดเฉพาะรายการอนุมัติและสร้างรายงาน Final ใหม่ |
| FR-RND-009 | Must have | Confirmed Response | ก่อน `DRAFT → OPEN` ต้องมี Active Criteria Set, ผ่าน Pre-open Validation และมี Application อย่างน้อย 1 ราย. | รอบ DRAFT | ไม่มี Application เป็น Blocking Error `NO_APPLICANTS` |

## 3.3 การนำเข้าข้อมูลผู้สมัคร

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-IMP-001 | Must have | Confirmed | ADMIN ต้องเลือกรอบและอัปโหลด `.xlsx`/`.csv`; ชนิดอื่นและรอบ CLOSED/ARCHIVED ต้องถูกปฏิเสธ. | ADMIN; รอบ DRAFT/OPEN | สร้าง Import Batch พร้อม metadata |
| FR-IMP-002 | Must have | Confirmed Response | `student_id` และโทรศัพท์ต้องอ่านเป็น Text และตรวจ Scientific Notation; national ID ต้องถูกปฏิเสธจาก Release 1 standard import. | อ่านไฟล์ | เลขศูนย์ไม่หาย; national ID ไม่ถูก persist/log |
| FR-IMP-003 | Must have | Confirmed | ตรวจ Header และจับคู่คอลัมน์ด้วยชื่อจริง Alias และ Mapping ที่ผู้ดูแลแก้ได้. | มี Header | Required Header ครบ; Missing/Duplicate ถูกแจ้ง |
| FR-IMP-004 | Must have | Confirmed | จำแนกแถวเป็น `APPLICANT`, `CONTINUATION`, `BLANK`, `INVALID`. | อ่านแถว | ทุกแถวมี row_type และ source row |
| FR-IMP-005 | Must have | Confirmed | CONTINUATION ต้องไม่มี student_id มีเฉพาะ กยศ./ทุน และผูก Applicant Valid ก่อนหน้า; ห้ามข้าม Invalid Context. | แถวไม่มี student_id | ผูก Child Record หรือ `ORPHAN_CONTINUATION_ROW` |
| FR-IMP-006 | Must have | Confirmed | Normalize: Trim, Blank/Whitespace/`-` ทั้ง Cell -> NULL โดยคง 0, แปลง พ.ศ.-ค.ศ., Decimal และพิกัด. | Mapping เสร็จ | Preview แสดง Raw และ Normalized |
| FR-IMP-007 | Must have | Confirmed | ตรวจ Field/Row/Cross-row/Duplicate และสร้าง `{row, field, code, severity, message}`. | Normalize เสร็จ | ข้อผิดพลาดระบุแถวและฟิลด์ |
| FR-IMP-008 | Must have | Confirmed | Duplicate ภายในไฟล์ตาม Business Key เป็น Blocking Error. | พบ Key ซ้ำ | ปิด Confirm และ `DUPLICATE_STUDENT_IN_FILE` |
| FR-IMP-009 | Must have | Confirmed Response | Duplicate กับฐานข้อมูลให้ Skip ค่าเริ่มต้น; never auto-Upsert; explicit Update เฉพาะก่อนมี Evaluation; หลังจากนั้นใช้ Controlled Correction. | พบ Existing Application | หลังเริ่มประเมินปฏิเสธ normal update `IMPORT_STATE_INVALID` |
| FR-IMP-010 | Must have | Confirmed | Preview ต้องไม่สร้าง/แก้ข้อมูลธุรกิจ. | Validation เสร็จ | ยกเลิก Preview แล้วข้อมูลไม่เปลี่ยน |
| FR-IMP-011 | Must have | Confirmed | ถ้ามี severity ERROR ต้องปิด Confirm; Warning อนุญาตตาม Policy. | มี Validation Result | Blocking Error Import ไม่ได้ |
| FR-IMP-012 | Must have | Confirmed | Confirm ต้องบันทึก Applicant/Child Records ใน Transaction; DB Error ต้อง Rollback ทั้ง Batch ที่ยืนยัน. | Batch ผ่าน | ไม่มีข้อมูลครึ่งชุด |
| FR-IMP-013 | Must have | Confirmed | บันทึก Counts total/applicant/continuation/valid/warning/error/skipped/imported และรายละเอียดรายแถว. | Import จบ | ตรวจย้อนหลังได้ |
| FR-IMP-014 | Must have | Confirmed | ส่งออก Import Error CSV ที่มี source_row, student, field, code, severity, raw_value, message. | มี Error/Warning | ไฟล์ตรง Preview |
| FR-IMP-015 | Must have | Confirmed Response | รองรับไฟล์ประวัติทุนแยก เชื่อม application business key และบันทึก source เป็น Snapshot ต่อ application/round. | ADMIN อัปโหลด History | ข้อมูลเชื่อมไม่ได้ไม่สร้าง Orphan |

## 3.4 ข้อมูลผู้สมัครและเอกสาร

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-APP-001 | Must have | Confirmed | ADMIN ต้องดู ค้นหา กรอง และเรียง Applicant ตามรอบ รหัส ชื่อ สาขา ชั้นปี และสถานะ. | ADMIN เลือกรอบ | ผลถูกจำกัดตามรอบและมี Pagination |
| FR-APP-002 | Must have | Confirmed | EVALUATOR ต้องค้นหาผู้สมัครในรอบ OPEN ด้วยรหัส/ชื่อ/นามสกุล โดยก่อนสร้าง Evaluation แสดงเฉพาะข้อมูลขั้นต่ำ. | EVALUATOR Active | ไม่ส่งข้อมูลละเอียดอ่อนก่อนมี Evaluation |
| FR-APP-003 | Must have | Confirmed | หลังสร้าง Evaluation ผู้ประเมินต้องดูข้อมูลผู้สมัคร เอกสาร ประวัติทุน และข้อมูลประกอบที่จำเป็นได้. | มี Active Evaluation ของผู้ใช้ | Backend ตรวจ Ownership ก่อนคืนข้อมูล |
| FR-APP-004 | Must have | Confirmed Response | Application อ้าง round/type/student ชัดเจน; business key คือ `round_id + scholarship_type_id + student_id`; UUID เป็น internal PK. | บันทึก Application | Unique triplet |
| FR-APP-005 | Must have | Confirmed Response | ADMIN แก้ mutable data ได้ก่อนมี Evaluation; หลัง Draft/Submitted ฟิลด์ที่กระทบคะแนน/รายงานใช้ Controlled Correction พร้อม reason, approval, before/after and audit. | ADMIN แก้ Application | identity triplet เปลี่ยนไม่ได้และไม่มีการเปลี่ยนสำคัญโดยไร้ประวัติ |
| FR-APP-006 | Must have | Confirmed | แสดงประวัติ กยศ./ทุนแบบหลายรายการ มีปี ชื่อ/ประเภท จำนวนเงิน และแหล่งที่มา. | มี History | รายการไม่ถูกทับ |
| FR-APP-007 | Must have | Confirmed | Applicant ต้องมี Result Summary ไม่เกินหนึ่งรายการต่อรอบ. | คำนวณผล | Unique Constraint ป้องกัน Summary ซ้ำ |
| FR-DOC-001 | Must have | Confirmed | ADMIN อัปโหลดเอกสารได้เฉพาะ PDF/JPG/PNG และขนาดสูงสุดจาก Configuration. | Applicant มีอยู่ | ชนิด/ขนาดไม่ผ่านถูกปฏิเสธ |
| FR-DOC-002 | Must have | Confirmed | Binary เก็บ Private File/Object Storage; PostgreSQL เก็บ metadata เช่น name, MIME, size, storage_key, checksum, uploader/time. | อัปโหลดผ่าน | ไม่มี Binary ใหญ่ใน DB ธุรกิจ |
| FR-DOC-003 | Must have | Confirmed | เปิด/ดาวน์โหลดต้องผ่าน Backend Authorization; ห้ามเปิด Storage Path/Public URL ถาวร. | ขอไฟล์ | ผู้ไม่มีสิทธิ์ได้ 403 |
| FR-DOC-004 | Must have | Confirmed | EVALUATOR เข้าถึงเอกสารเฉพาะ Applicant ที่มี Active Evaluation ของตน; ADMIN ตามหน้าที่. | ขอเอกสาร | สิทธิ์ระดับไฟล์ตรงสิทธิ์ Applicant |
| FR-DOC-005 | Must have | Confirmed | รองรับ Preview PDF/JPG/PNG และ Download เมื่อ Preview ไม่ได้. | ไฟล์/สิทธิ์ถูกต้อง | Content-Type/Disposition ถูกต้อง |
| FR-DOC-006 | Must have | Confirmed Response | ตรวจ signature/MIME/extension/size, ทำชื่อปลอดภัย และ Malware Scan ทุก production file; scanner unavailable คง Quarantine. | อัปโหลด | ไฟล์ไม่ Clean ไม่ถูกดู/ดาวน์โหลด |

## 3.5 การจัดการเกณฑ์คะแนน

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-CRI-001 | Must have | Confirmed | ADMIN ต้องสร้าง Criteria Set แยกตามรอบและกำหนด criterion_code, ชื่อ, คำอธิบาย, คะแนนต่ำสุด/เต็ม, น้ำหนัก, ลำดับ, required, version และ round. | ADMIN; รอบ DRAFT | Item ถูกบันทึกครบ |
| FR-CRI-002 | Must have | Confirmed | ภายใน Version เดียว code และ display_order ห้ามซ้ำ และ min_score <= max_score. | บันทึก Item | ข้อมูลผิดถูกปฏิเสธ |
| FR-CRI-003 | Must have | Confirmed Response | Template เริ่มต้นมี 10 scoring criteria รวม 100; ใช้ชื่อที่ RD-014 ยืนยันและ unique immutable `criterion_code`. | สร้าง Template | ได้ 10 Items, Total=100 และ code ไม่ซ้ำ |
| FR-CRI-004 | Must have | Open | Scoring Rule ต้องระบุ `weight_type` ว่า POINT หรือ PERCENT; ห้าม Activate หากกฎน้ำหนักไม่ชัดหรือผลรวมผิด. | Activate Criteria | ผ่าน Weight Validation เท่านั้น |
| FR-CRI-005 | Must have | Confirmed | ก่อน Activate ต้องมี >=1 Item; ทุก Item มี Code/Name/Min/Max/Order/Required และ Total Full Score ตรง Rule. | Criteria DRAFT | ผ่านจึง ACTIVE |
| FR-CRI-006 | Must have | Confirmed | หนึ่งรอบมี Active Criteria Version สำหรับ Evaluation ใหม่ได้ไม่เกินหนึ่ง Version. | Activate | ไม่มี Active ซ้ำ |
| FR-CRI-007 | Must have | Confirmed | เมื่อมี Evaluation ที่ยังไม่ยกเลิกอ้าง Version แล้ว ต้องล็อกฟิลด์ที่กระทบคะแนน. | มี Evaluation | ปฏิเสธ `CRITERIA_LOCKED` |
| FR-CRI-008 | Must have | Confirmed | การเปลี่ยนเกณฑ์ที่กระทบคะแนนต้องสร้าง Version ใหม่และรักษา Version เดิม. | สร้าง Revision | Evaluation เดิมยังใช้ Version เดิม |
| FR-CRI-009 | Must have | Confirmed | Evaluation ทุกตัวต้องเก็บ criteria_version_id และ Snapshot กฎที่จำเป็นต่อ Audit/Recalculation. | สร้าง Evaluation | ระบุ Version ที่ใช้ได้ |
| FR-CRI-010 | Must have | Confirmed Response | คะแนนดุลพินิจเป็นจำนวนเต็ม 0-10; ค่านอก standard options ต้องมีเหตุผล. | กรอกคะแนน | decimal/out-of-range/reason missing ถูกปฏิเสธ |
| FR-CRI-011 | Must have | Confirmed Response | ทุนต่อเนื่อง มูลค่าทุน และความเห็นเพิ่มเติมเป็น Outcome Fields แยกจาก 100 points; Custom Amount requires reason and ceiling. | กำหนดแบบฟอร์ม | Outcome ไม่ถูกรวมคะแนน |
| FR-CRI-012 | Nice to have | Confirmed | อาจคัดลอก Criteria รอบเดิมเป็น DRAFT ใหม่ โดยไม่แก้ต้นทาง. | ADMIN เลือกรอบต้นทาง | สร้างชุดใหม่แก้ได้ก่อน Activate |

## 3.6 การเลือกผู้สมัครและ Workflow การประเมิน

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-EVA-001 | Must have | Confirmed | อนุญาตสร้าง Evaluation เมื่อรอบ OPEN, บัญชี ACTIVE, Applicant อยู่ในรอบ, มี Active Criteria, คนเดิมไม่มี Active Evaluation และ Active Count <3. | EVALUATOR เลือก Applicant | สร้าง DRAFT อ้าง Applicant/Round/Evaluator/Criteria Version |
| FR-EVA-002 | Must have | Confirmed | หากคนเดิมมี Evaluation ที่ยังไม่ยกเลิกสำหรับ Applicant/Round เดิม ต้องปฏิเสธ. | มีรายการเดิม | 409 `DUPLICATE_EVALUATION` |
| FR-EVA-003 | Must have | Confirmed | ต้องปฏิเสธคนที่ 4 โดยนับ Draft และ Submitted ที่ยังไม่ยกเลิก. | Active Count=3 | 409 `EVALUATOR_LIMIT_REACHED` |
| FR-EVA-004 | Must have | Confirmed | การตรวจเงื่อนไขและเพิ่ม Evaluation ต้องใช้ Transaction + Lock/Serializable หรือเทียบเท่า ป้องกัน Race. | คำขอพร้อมกัน | หลัง Commit Active Count <=3 |
| FR-EVA-005 | Must have | Confirmed | เมื่อ Submitted ครบ 2 คน ยังอนุญาตคนที่ 3 เริ่ม/Submit ก่อนปิดรอบ ถ้า Capacity ยังมี. | Submitted=2; OPEN | คนที่ 3 ทำ Flow ได้ |
| FR-EVA-006 | Must have | Confirmed | เจ้าของ Draft เดิมต้องกลับมาแก้ได้แม้ภายหลัง Active Count=3. | มี Draft เดิม | เปิด Draft เดิม ไม่สร้างใหม่ |
| FR-EVA-007 | Must have | Confirmed | หน้า Evaluation ต้องแสดงข้อมูล ผู้สมัคร เอกสาร ประวัติ เกณฑ์ คะแนน และความคิดเห็นอย่างต่อเนื่อง. | มี Active Evaluation | ทำ Core Flow โดยไม่ใช้ Excel คะแนน |
| FR-EVA-008 | Must have | Confirmed | กรอกคะแนนตาม min/max/step และตรวจทั้ง Client/Server; Server เป็นตัวตัดสิน. | กรอกคะแนน | นอกช่วงเป็น `SCORE_OUT_OF_RANGE` |
| FR-EVA-009 | Must have | Confirmed | บันทึก Draft ได้แม้ไม่ครบ โดยค่าที่กรอกต้อง valid และ Draft ห้ามใช้คำนวณ. | Evaluation DRAFT | บันทึก updated_at; Summary ไม่เปลี่ยน |
| FR-EVA-010 | Must have | Confirmed | ก่อน Submit ต้องแสดง Review Summary ของคะแนน ความคิดเห็น Outcome และ Total ที่คาด. | ข้อมูลพร้อม | ผู้ประเมินเห็นและยืนยันอีกครั้ง |
| FR-EVA-011 | Must have | Confirmed | Submit ได้เมื่อ Required Criteria และข้อมูลบังคับครบและถูกต้อง. | ยืนยัน Submit | สถานะ SUBMITTED และ submitted_at |
| FR-EVA-012 | Must have | Open | ระบบต้องรองรับ comment_required; หาก Rule บังคับแต่ความคิดเห็นว่างต้องปฏิเสธ `EVALUATION_INCOMPLETE`. | Rule บังคับ | Submit ไม่สำเร็จเมื่อว่าง |
| FR-EVA-013 | Must have | Confirmed | หลัง Submit ผู้ประเมินแก้โดยตรงไม่ได้ และผลต้องเข้าสู่การคำนวณทันที. | SUBMITTED | UI Read-only/API Update ปฏิเสธ |
| FR-EVA-014 | Must have | Confirmed Response | เจ้าของยกเลิก Draft ได้โดยยืนยันและเหตุผล; `CANCELLED` ไม่ลบจริง คืน Slot ใน Transaction และ Audit. | เจ้าของ Draft | ไม่นับ Capacity และมี Audit |
| FR-EVA-015 | Must have | Confirmed Response | แก้ Submitted ผ่าน request/on-behalf + independent Head/delegate approval; normally before close; technical Admin cannot self-approve; preserve immutable revision and recalculate after Resubmit. | Submitted | Revision เดิมไม่สูญหาย |
| FR-EVA-016 | Must have | Confirmed | Cancelled ไม่นับ Capacity และไม่อยู่ใน Calculation/Dashboard/Report. | CANCELLED | Slot เปิดทันที |
| FR-EVA-017 | Must have | Confirmed | ผู้ประเมินหนึ่งคนประเมินหลาย Applicant ได้; Unique เฉพาะคู่ Evaluator-Applicant-Round. | เลือกหลายคน | สร้างได้ตาม Capacity แต่ละ Applicant |
| FR-EVA-018 | Must have | Confirmed | SEMS ไม่จัดคิวสัมภาษณ์ สร้างห้อง หรือดึงผู้ใช้เข้า Zoom/ระบบประชุม. | ใช้งานระบบ | ไม่มีฟังก์ชันดังกล่าวใน Core |

## 3.7 การคำนวณคะแนน สถานะ และผลสรุป

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-SCO-001 | Must have | Confirmed | ใช้เฉพาะ SUBMITTED ที่ยังไม่ยกเลิกและผู้ประเมินไม่ซ้ำในการคำนวณ. | Submit/Reopen/Close | Draft/Cancelled/Reopened ที่ยังไม่ Resubmit ไม่ถูกใช้ |
| FR-SCO-002 | Must have | Confirmed Response | Total รายผู้ประเมินเป็นผลรวม `EMBEDDED_POINT` ทั้ง 10 เกณฑ์ สูงสุด 100; ห้ามคูณ `weight_percent` ซ้ำ. | พร้อม Submit | Total ตรง Reference Dataset |
| FR-SCO-003 | Must have | Confirmed Response | Summary เป็นค่าเฉลี่ยเลขคณิตแบบ equal weight ของ evaluator total จากผู้ประเมินไม่ซ้ำ 2–3 คนที่ `SUBMITTED`; คนที่ 3 trigger recalculate. | Submitted 2/3 | ตรง Reference Calculation |
| FR-SCO-004 | Must have | Confirmed Response | เก็บค่าคำนวณเต็ม Precision และปัดเฉพาะ applicant summary 2 ตำแหน่ง `ROUND_HALF_UP`; ห้ามปัดระหว่างทาง. | คำนวณ | ผ่าน Boundary Test |
| FR-SCO-005 | Must have | Confirmed | Submitted <2 ต้องไม่มี Latest/Final Summary Score แม้แสดงคะแนนรายคนได้. | Count 0/1 | Summary score NULL |
| FR-SCO-006 | Must have | Confirmed | คนที่ 2 Submit ต้องสร้าง/อัปเดต Summary และสถานะ `MINIMUM_COMPLETE` ขณะ OPEN. | คนที่ 2 Submit | count=2 และมี Latest Score |
| FR-SCO-007 | Must have | Confirmed | คนที่ 3 Submit ต้องคำนวณทั้ง 3 คนใหม่และเป็น `FULLY_COMPLETE` ขณะ OPEN. | คนที่ 3 Submit | Summary/Dashboard/Report ค่าใหม่ตรงกัน |
| FR-SCO-008 | Must have | Confirmed | แสดง Submitted 0/3,1/3,2/3,3/3 และสถานะ 6 ค่า ตาม State Table. | อ่านรายการ | สถานะตรง Round/Count |
| FR-SCO-009 | Must have | Confirmed | ปิดรอบ: Submitted>=2 เป็น FINALIZED/Final Score; <2 เป็น CLOSED_INCOMPLETE/Final Score NULL. | Close Round | ไม่มี Closed Incomplete ที่มี Final Score |
| FR-SCO-010 | Must have | Confirmed | Result Summary หนึ่งรายการต่อ Applicant/Round เก็บ evaluator_count, criteria_version, rule_version, unrounded/rounded score, calculated_at. | คำนวณ | Audit Input/Rule ได้ |
| FR-SCO-011 | Must have | Confirmed | เมื่อ Reopen/Resubmit/เปลี่ยนสถานะ Input ต้องทำ Summary Stale หรือคำนวณใหม่ ไม่แสดงค่าเก่า. | Input เปลี่ยน | ค่าล่าสุดถูกต้อง |
| FR-SCO-012 | Must have | Confirmed | UI, Export และ DB ต้องใช้ชุด Input/Rule เดียวกันสำหรับคะแนน Count Comment และสถานะ. | อ่าน/Export | ค่าตรง 100% |

## 3.8 รายงาน Dashboard และ Audit

| ID | Priority | Status | Requirement ที่ทดสอบได้ | Precondition / Trigger | Expected Result |
| --- | --- | --- | --- | --- | --- |
| FR-RPT-001 | Must have | Confirmed | ADMIN ดูผลตามรอบ ค้นหา/กรอง/เรียงตามรหัส ชื่อ Count สถานะ คะแนน. | เลือก Round | รายการมี Pagination/ไม่ข้ามรอบ |
| FR-RPT-002 | Must have | Confirmed | รายละเอียดผลแสดง Submitted Evaluators, scores, totals, comments, outcomes, count, status, summary ตามสิทธิ์. | เปิด Result | Draft คนอื่นไม่เป็นผลสุดท้าย |
| FR-RPT-003 | Must have | Confirmed | ส่งออก Excel/CSV Fixed Template และค่าต้องตรง Result Summary/DB. | ADMIN Export | ไฟล์เปิดได้และตรง 100% |
| FR-RPT-004 | Must have | Confirmed | Export ใช้เฉพาะ Submitted ที่ยังไม่ยกเลิก; Draft/Cancelled ไม่คำนวณ. | สร้าง Report | ตรง Scoring Rule |
| FR-RPT-005 | Must have | Confirmed | Report แสดง Minimum/Fully ขณะ OPEN และ Finalized/Closed Incomplete หลัง CLOSED ตามกฎเดียวกัน. | Export | สถานะตรง UI |
| FR-RPT-006 | Must have | Confirmed Response | Excel มี `Summary` และ `Evaluator Detail`; CSV แยกสองไฟล์และอาจ ZIP; profile เป็น INTERNAL_FULL/SUMMARY_MASKED. | Export | ข้อมูลหลายระดับไม่กำกวมและ evaluator isolation ถูกต้อง |
| FR-RPT-007 | Must have | Confirmed | Standard Export ใช้ Least Privilege และไม่รวมเลขบัตร/Contact/Restricted Field โดย Default. | Export | ไม่มี Restricted PII |
| FR-RPT-008 | Must have | Confirmed | ทุก Export บันทึกผู้ใช้ รอบ Template Filter จำนวน เวลา และผล. | Export | Audit `REPORT_EXPORTED` |
| FR-RPT-009 | Nice to have | Confirmed | PDF/Custom Template เป็น Optional ไม่ใช่ Core Acceptance. | ทดสอบ Core | ไม่มี PDF ไม่ทำให้ Core Fail |
| FR-DSH-001 | Must have | Confirmed | Dashboard แสดง Applicant ทั้งหมด Submitted 0/1/2/3 และจำนวนตาม 6 สถานะ. | เลือก Round | Counts ตรง DB |
| FR-DSH-002 | Must have | Confirmed | Visualization คะแนนใช้เฉพาะ Submitted ไม่รวม Draft/Cancelled. | โหลด Dashboard | กราฟตรง Reference |
| FR-DSH-003 | Must have | Confirmed | หลัง Submit 2/3, Reopen, Resubmit หรือ Close Dashboard ต้องสะท้อนค่าล่าสุดอัตโนมัติ. | เกิดเหตุการณ์ | อัปเดตตาม SLA |
| FR-AUD-001 | Must have | Confirmed | Audit Append-only สำหรับ User/Role, Round, Import, Applicant, Document, Criteria, Selection, Cancel, Submit, Reopen, Calculation, Close และ Export. | เกิดเหตุการณ์ | มี Event แก้ย้อนหลังผ่าน UI ไม่ได้ |
| FR-AUD-002 | Must have | Confirmed | Audit มี event_type, actor, occurred_at, entity, round, result, reason, trace_id และ before/after ที่ Mask. | สร้าง Event | ตอบว่าใครทำอะไรเมื่อใด |
| FR-AUD-003 | Must have | Confirmed | Audit ห้าม Password/Token/Secret/Code/Session เต็ม/Binary/Document Content. | บันทึก Event | Secret Scan ไม่พบ |
| FR-AUD-004 | Must have | Confirmed | ADMIN ดู Audit พื้นฐานตามเวลา ผู้ใช้ Event Round Entity ได้. | เปิด Audit | ค้นเหตุการณ์หลักได้ |

# 4. Non-functional Requirements

| ID | Category | Status | Requirement |
| --- | --- | --- | --- |
| NFR-PERF-001 | Performance | Provisional | หน้า List/Search มาตรฐานที่มีผู้สมัครไม่เกิน 500 รายต่อรอบต้องตอบสนอง p95 ไม่เกิน 2 วินาที ไม่รวม Download File. |
| NFR-PERF-002 | Performance | Provisional | Result Summary หลัง Submit ต้องอ่านค่าล่าสุดได้ภายใน 3 วินาที p95. |
| NFR-PERF-003 | Performance | Provisional | Validate/Preview 500 Applicant Rows และ Continuation ที่เกี่ยวข้องต้องเสร็จภายใน 60 วินาทีใน Test Environment. |
| NFR-PERF-004 | Performance | Provisional | Export 500 Applicant เป็น Excel/CSV ต้องเสร็จภายใน 60 วินาที หรือเป็น Background Job พร้อม Status. |
| NFR-REL-001 | Reliability | Confirmed | ธุรกรรมสร้าง Evaluation, Submit, Recalculation และ Confirm Import ต้อง Atomic และไม่สร้างข้อมูลครึ่งชุด. |
| NFR-REL-002 | Reliability | Confirmed | ต้องมี Database Migration ที่ทำซ้ำได้และคู่มือ Restore/Rollback. |
| NFR-REL-003 | Reliability | Confirmed Response | Production backup DB daily/full weekly, RPO ≤24h, RTO ≤8 business hours, consistent file backup, restore quarterly and before go-live. |
| NFR-AVL-001 | Availability | Provisional | เป้าหมาย Availability ช่วงประเมินอย่างน้อย 99.5% ไม่รวม Maintenance ที่แจ้งล่วงหน้า. |
| NFR-USA-001 | Usability | Confirmed | Core Flow ของ EVALUATOR ตั้งแต่ค้นหา เลือก ดูข้อมูล Draft Review Submit ต้องทำผ่าน Browser โดยไม่ใช้ Excel บันทึกคะแนน. |
| NFR-USA-002 | Usability | Confirmed | Validation Error ต้องระบุฟิลด์/แถว ปัญหา และวิธีแก้ภาษาไทย; Error Code คงที่สำหรับ QA/API. |
| NFR-USA-003 | Usability | Provisional | UI รองรับ Desktop >=1280px และ Tablet แนวนอน; Native Mobile ไม่อยู่ใน Scope. |
| NFR-ACC-001 | Accessibility | Provisional | ฟอร์ม Core ต้องมี Label, Keyboard Navigation, Focus Indicator และ Contrast ตาม WCAG 2.1 AA ในส่วนหลัก. |
| NFR-COMP-001 | Compatibility | Provisional | รองรับ Chrome/Edge ปัจจุบันและย้อนหลัง 2 Major Versions; Safari รอยืนยัน. |
| NFR-MNT-001 | Maintainability | Confirmed | Frontend/Backend ใช้ TypeScript แยก Module ตาม Domain และมี Automated Test สำหรับ Business Rule สำคัญ. |
| NFR-MNT-002 | Maintainability | Confirmed | สูตรคะแนนและสถานะต้องอยู่ใน Domain/Service เดียว ไม่ทำซ้ำใน UI, Export และ Dashboard. |
| NFR-MNT-003 | Maintainability | Confirmed | Configuration/Environment/Secret แยก Source Code และห้าม Commit Public Repository. |
| NFR-OBS-001 | Observability | Provisional | มี Structured Log พร้อม `traceId` และ Health Check โดยไม่ Log PII เกินจำเป็น. |
| NFR-LOC-001 | Localization | Confirmed | แสดงเวลา Asia/Bangkok; เก็บ Timestamp แบบ UTC/Timestamptz. |
| NFR-DEL-001 | Delivery | Confirmed | Source Code, Database Schema, Migration, Test Report, คู่มือติดตั้ง และคู่มือใช้งานครบก่อนส่งมอบ. |

# 5. Security Requirements

| ID | Requirement |
| --- | --- |
| SEC-001 | Production ต้องใช้ HTTPS เท่านั้นและ TLS 1.2 หรือสูงกว่า. |
| SEC-002 | Authentication ใช้ KKU OAuth 2.1/OIDC Authorization Code + PKCE S256; ห้าม Implicit Flow. |
| SEC-003 | ตรวจ `state` ป้องกัน CSRF และ `nonce` ป้องกัน Replay ใน OIDC Callback. |
| SEC-004 | ID Token ต้องตรวจ JWKS Signature, issuer, audience, expiration และ nonce. |
| SEC-005 | Authorization ตรวจ Backend ทุก API ด้วย Least Privilege, Role, Round และ Ownership. |
| SEC-006 | State-changing Request ที่ใช้ Cookie Session ต้องมี CSRF Protection. |
| SEC-007 | Session Cookie เป็น Secure/HttpOnly/SameSite และ Invalidate เมื่อ Logout/Privilege Change. |
| SEC-008 | Validate/Normalize Input ฝั่ง Server และใช้ ORM/Parameterized Query ป้องกัน Injection. |
| SEC-009 | ไฟล์อัปโหลดตรวจ Extension, MIME, Magic Bytes, Size, Filename และเก็บนอก Web Root/Private Storage. |
| SEC-010 | เอกสารให้บริการผ่าน Backend หรือ Signed URL อายุสั้นหลังตรวจสิทธิ์. |
| SEC-011 | Applicant/ครอบครัว/รายได้/พิกัด/เอกสารต้องจัดชั้นความอ่อนไหวและ Mask/จำกัดสิทธิ์. |
| SEC-012 | ห้ามเก็บ Password KKU, Token, Client Secret, Environment Secret หรือข้อมูลจริงใน Source/Public Repo/Audit. |
| SEC-013 | Dev/Test ใช้ข้อมูลจำลองหรือปกปิดตัวตน; ข้อมูลจริงต้องได้รับอนุญาต. |
| SEC-014 | ป้องกัน Mass Assignment ด้วย DTO/Allowed Fields สำหรับ Mutation. |
| SEC-015 | Error Response ห้ามเปิด Stack Trace, SQL, Storage Path, Token หรือรายละเอียดภายใน. |
| SEC-016 | Restricted PII Export ต้องมี Permission แยกและ Audit. |
| SEC-017 | Deactivate Account ต้องห้าม Session ใหม่ และควรยกเลิก Session เดิมตามเวลาที่กำหนด. |
| SEC-018 | กำหนด Retention/Secure Deletion ตามนโยบายก่อน Production. |

# 6. Data Requirements

## 6.1 หลักการข้อมูล

1. Primary Key ใช้ UUID เป็นหลัก และ Business Key ใช้ Unique Constraint แยก
2. Identifier เก็บเป็น Text; Score/Amount ใช้ Decimal ไม่ใช้ Floating Point
3. Evaluation/Result อ้าง Criteria และ Calculation Rule Version
4. Raw Import แยกจาก Normalized Data และกำหนด Retention
5. Entity สำคัญมี timestamps และผู้ดำเนินการเมื่อเหมาะสม
6. ห้าม Hard Delete ข้อมูลที่ใช้ Audit เว้นแต่นโยบาย Retention/PDPA กำหนด

## 6.2 Entity ขั้นต่ำ

| Entity | หน้าที่ | ฟิลด์/Constraint ขั้นต่ำ |
| --- | --- | --- |
| users | บัญชี SEMS | UUID PK; kku_subject Unique; display_name; email; role; status; timestamps |
| scholarship_rounds | รอบทุน | UUID PK; round_code Unique; name; academic_year; dates; status |
| applicants / round_applications | ผู้สมัครในรอบ | round_id FK; student_id Text; ข้อมูลส่วนบุคคล/การศึกษา; Business Unique Key |
| applicant_expenses | ค่าใช้จ่าย | application_id; expense_type; amount Decimal; period; ค่าอุปกรณ์ต่อภาค ที่พัก/ส่วนตัวต่อเดือน |
| parent/supporter/siblings | ครอบครัว | application_id; relation; status; occupation; income; order |
| student_loan_histories | ประวัติ กยศ. | year; amount; source_import_id; applicant/application FK |
| scholarship_histories | ประวัติทุน | year; scholarship_name; amount; source_import_id |
| address_coordinates | พิกัด | latitude Decimal(9,7); longitude Decimal(10,7); raw; source |
| applicant_documents | เอกสาร | document_type; filename; storage_key Unique; mime; size; checksum; uploader/time |
| criteria_sets / versions | ชุดเกณฑ์ | round_id; version; status; rule_version; total_full_score |
| criteria_items | หัวข้อประเมิน | code; name; description; min/max; weight; order; required; version_id |
| evaluations | รายการประเมิน | round/application/evaluator/criteria_version; status; revision; timestamps |
| evaluation_scores | คะแนนรายเกณฑ์ | evaluation_id; criterion_id; score Decimal; comment; Unique(evaluation,criterion) |
| evaluation_outcomes | ผลประกอบ | continuing_support; recommended_amount; overall_comment |
| result_summaries | ผลสรุป | Unique(round,application); evaluator_count; rule_version; unrounded/rounded; status |
| import_batches / rows | การนำเข้า | file metadata/counts/status; raw/normalized row; validation messages |
| audit_events | ประวัติ | event_type; actor; entity; round; before/after masked; reason; trace_id; time |

## 6.3 Enumeration ขั้นต่ำ

| กลุ่ม | ค่า |
|---|---|
| User Status | `ACTIVE`, `INACTIVE` |
| User Role | `ADMIN`, `EVALUATOR` |
| Round Status | `DRAFT`, `OPEN`, `CLOSED`, `ARCHIVED` |
| Criteria Status | `DRAFT`, `ACTIVE`, `RETIRED` |
| Evaluation Status | `DRAFT`, `SUBMITTED`, `REOPEN_REQUESTED`/`REOPENED` or Revision Pending, `CANCELLED`; approved reopen returns editable work to Draft |
| Applicant Status | `NOT_STARTED`, `IN_PROGRESS`, `MINIMUM_COMPLETE`, `FULLY_COMPLETE`, `FINALIZED`, `CLOSED_INCOMPLETE` |
| Import Row Type | `APPLICANT`, `CONTINUATION`, `BLANK`, `INVALID` |
| Import Validation | `VALID`, `WARNING`, `ERROR`, `SKIPPED` |

## 6.4 Precision และการปัดเศษ

- คะแนนกรอกเป็น Decimal ตาม `score_step`
- ค่าคำนวณระหว่างทางเก็บอย่างน้อย 4 ตำแหน่งหรือ Precision เพียงพอ
- Final Score เป็น Decimal 2 ตำแหน่ง
- Draft Rule ใช้ `ROUND_HALF_UP` เฉพาะ Final Score
- ห้ามใช้ค่าที่ Format แล้วกลับมาคำนวณ


# 7. Validation Rules

| Rule ID | ข้อมูล/กระบวนการ | Rule |
| --- | --- | --- |
| VR-ID-001 | รหัสนักศึกษา | Trim แล้วตรง `^\d{9}-\d$`; ยังไม่ตรวจ Check Digit จนได้สูตรยืนยัน; เก็บ Text. |
| VR-ID-002 | Identifier | ห้าม Scientific Notation และรักษาเลขศูนย์นำหน้า. |
| VR-GPA-001 | GPA | Decimal 0.00-4.00; Required หรือไม่ตาม Baseline. |
| VR-DATE-001 | วันที่ | Template ใหม่ ISO; Legacy เช่น `09 ก.ค. 2569 13:36` แปลง พ.ศ.-543 ตามรูปแบบที่ประกาศ. |
| VR-PHONE-001 | โทรศัพท์ | เก็บ Text; รูปแบบทางการเป็น RD-020. |
| VR-COORD-001 | พิกัด | latitude -90..90, longitude -180..180; มีครบคู่หรือว่างคู่. |
| VR-NULL-001 | NULL | Blank/Whitespace/`-` ทั้ง Cell -> NULL; 0 คงเป็น 0; Prefix `-` ใน History ไม่ใช่ NULL. |
| VR-IMP-001 | Applicant Row | มี student_id และ Hard Required ตาม Baseline. |
| VR-IMP-002 | Continuation | student_id ว่าง; มีเฉพาะ กยศ./ทุน; มี Applicant Owner Valid ก่อนหน้า. |
| VR-DUP-001 | Duplicate ในไฟล์ | Business Key ซ้ำ -> Blocking Error. |
| VR-DUP-002 | Duplicate ใน DB | Default Skip; never auto-Upsert; explicit Update เฉพาะก่อน Evaluation. |
| VR-CRI-001 | Criterion | code/name ไม่ว่าง; min<=max; max>0; order ไม่ซ้ำ; required Boolean. |
| VR-CRI-002 | Criteria Activate | มี Item; Total/Weight ตรง Rule; Active Version ไม่ซ้ำ. |
| VR-EVA-001 | Capacity | Active = ยังไม่ Cancelled; ต่อ Applicant/Round ไม่เกิน 3. |
| VR-EVA-002 | Uniqueness | Evaluator คนเดิมมี Active Evaluation ต่อ Applicant/Round <=1. |
| VR-SCORE-001 | คะแนน | อยู่ min..max และตรง step/allowed option. |
| VR-SUBMIT-001 | Submit | Required Criteria/Comment/Outcome ครบ; รอบ OPEN; Owner Active. |
| VR-STATUS-001 | Applicant Status | ใช้ State Table ในเอกสารนี้. |
| VR-FILE-001 | Document | PDF/JPEG/PNG; Size Config; Magic Bytes ตรง MIME. |

## 7.1 Round State Transition

| Current | Allowed Next | เงื่อนไข |
|---|---|---|
| DRAFT | OPEN | OPEN ต้องมี Active Criteria, ผ่าน Pre-open Validation และมี Application ≥1; ไม่มี Application เป็น Blocking Error |
| OPEN | CLOSED | ADMIN ปิดและประมวลผลสถานะสุดท้าย |
| CLOSED | ARCHIVED | เก็บอ่านย้อนหลัง |
| CLOSED | OPEN | เฉพาะ exceptional Controlled Reopen ที่อนุมัติ; prior Final snapshot becomes Superseded |
| ARCHIVED | - | Read-only; application workflow cannot reopen. Disaster-recovery restore follows RD-041, not a round state transition. |

## 7.2 Applicant Status State Table

| Round | Active Evaluation | Submitted | Status | Summary Score |
|---|---:|---:|---|---|
| DRAFT/OPEN | 0 | 0 | NOT_STARTED | NULL |
| OPEN | >=1 | 0-1 | IN_PROGRESS | NULL |
| OPEN | >=2 | 2 | MINIMUM_COMPLETE | Latest Score |
| OPEN | 3 | 3 | FULLY_COMPLETE | Latest Score |
| CLOSED | any | >=2 | FINALIZED | Final Score |
| CLOSED | any | 0-1 | CLOSED_INCOMPLETE | NULL |


# 8. Error Handling

## 8.1 รูปแบบ Error Response

```json
{
  "code": "EVALUATOR_LIMIT_REACHED",
  "message": "ผู้สมัครมีรายการประเมินครบ 3 คนแล้ว",
  "details": [{"field": "applicantId", "reason": "ACTIVE_EVALUATION_COUNT_IS_3"}],
  "traceId": "trace-id",
  "timestamp": "2026-07-23T12:00:00Z"
}
```

## 8.2 HTTP Status

| Status | ใช้เมื่อ |
|---:|---|
| 400 | Request Structure/Parameter ผิด |
| 401 | ไม่มี/Session หรือ Token ไม่ถูกต้อง |
| 403 | ยืนยันตัวตนแล้วแต่ไม่มีสิทธิ์ |
| 404 | ไม่พบ Resource |
| 409 | Conflict กับ State/Unique/Capacity |
| 413 | ไฟล์ใหญ่เกิน |
| 415 | ชนิดไฟล์ไม่รองรับ |
| 422 | Validation เชิงข้อมูลไม่ผ่าน |
| 429 | Rate Limit |
| 500 | Internal Error |
| 503 | Dependency เช่น KKU SSO/Storage ไม่พร้อม |

## 8.3 หลักการ

1. ห้ามแสดง Stack Trace, SQL, Secret, Internal Path หรือ Token
2. ทุก Error มี `traceId`
3. Validation หลายรายการควรรวมส่งครั้งเดียวเมื่อปลอดภัย
4. Transaction Error ต้อง Rollback
5. Frontend ใช้ Error Code ไม่ใช้การ Parse ข้อความเพื่อควบคุม Logic
6. Error Code ที่เผยแพร่แล้วห้ามเปลี่ยนความหมายโดยไม่มี Version/Change Log

## 8.4 Error Code Catalog ขั้นต่ำ

Source of Truth: [`SEMS_Error_Code_Catalog.md`](../../Design/API/SEMS_Error_Code_Catalog.md)

| Code | HTTP | Meaning |
| --- | --- | --- |
| AUTH_REQUIRED | 401 | ไม่มี Session/หมดอายุ |
| TOKEN_VALIDATION_FAILED | 401 | Callback/Token KKU ไม่ผ่าน |
| USER_NOT_PROVISIONED | 403 | ยังไม่เชื่อม SEMS |
| USER_INACTIVE | 403 | บัญชีปิด |
| ACCESS_DENIED | 403 | ไม่มีสิทธิ์ |
| ROUND_NOT_FOUND | 404 | ไม่พบรอบ |
| ROUND_NOT_OPEN | 409 | รอบไม่ OPEN |
| INVALID_ROUND_STATUS_TRANSITION | 409 | Transition ผิด |
| ACTIVE_CRITERIA_REQUIRED | 409 | ไม่มี Active Criteria |
| CRITERIA_LOCKED | 409 | เกณฑ์ถูกใช้ |
| DUPLICATE_EVALUATION | 409 | ผู้ประเมินซ้ำ |
| EVALUATOR_LIMIT_REACHED | 409 | ครบ 3 คน |
| EVALUATION_NOT_OWNER | 403 | ไม่ใช่เจ้าของ |
| EVALUATION_ALREADY_SUBMITTED | 409 | ส่งแล้ว |
| SCORE_OUT_OF_RANGE | 422 | คะแนนนอกช่วง |
| EVALUATION_INCOMPLETE | 422 | คะแนนหรือความคิดเห็นบังคับไม่ครบ |
| SUMMARY_NOT_AVAILABLE | 409 | Submitted ไม่ครบ 2 |
| REQUIRED_FIELD_MISSING | 422 | ข้อมูลบังคับหาย |
| INVALID_STUDENT_ID | 422 | รหัสผิด |
| VALIDATION_ERROR | 422 | รูปแบบข้อมูลไม่ผ่านกฎ เช่น Scientific Notation หรือ Continuation Row ผิดรูปแบบ |
| INVALID_GPA | 422 | GPA ผิด |
| INVALID_DATE | 422 | วันที่ผิด |
| INVALID_PHONE | 422 | เบอร์โทรศัพท์ผิด |
| INVALID_EMAIL | 422 | อีเมลผิด |
| INVALID_COORDINATE | 422 | พิกัดผิด |
| DUPLICATE_STUDENT_IN_FILE | 422 | ซ้ำในไฟล์ |
| DUPLICATE_STUDENT_IN_ROUND | 409 | ซ้ำในรอบ |
| ORPHAN_CONTINUATION_ROW | 422 | Continuation ไม่มีเจ้าของ |
| IMPORT_STATE_INVALID | 409 | สถานะ Import หรือข้อมูลปลายทางไม่อนุญาตให้ดำเนินการ |
| UNSUPPORTED_FILE_TYPE | 415 | ชนิดไฟล์ไม่รองรับ |
| IMPORT_FILE_TOO_LARGE | 413 | ไฟล์ Import ใหญ่เกิน |
| DOCUMENT_TYPE_UNSUPPORTED | 415 | ชนิด Applicant Document ไม่รองรับ |
| DOCUMENT_TOO_LARGE | 413 | Applicant Document ใหญ่เกิน |
| REPORT_FORMAT_UNSUPPORTED | 415 | รูปแบบ Report Export ไม่รองรับ |
| IMPORT_HAS_BLOCKING_ERRORS | 409 | Batch ยังมี Error |
| FILE_STORAGE_ERROR | 500 | จัดเก็บไฟล์ Import/Document/Report ไม่สำเร็จ |

# 9. Audit Requirements

1. Audit เป็น Append-only และผู้ใช้ทั่วไปแก้/ลบไม่ได้
2. Event สำคัญต้องมี Success/Failure
3. Before/After เก็บเฉพาะจำเป็นและ Mask PII
4. Reopen, Cancel, Override, Restricted Export และ Close Round ต้องมี Reason
5. เชื่อม `trace_id`; System Job ใช้ Actor `SYSTEM`
6. เวลาใช้ Timestamptz และแสดง Asia/Bangkok
7. Retention Audit ต้องยืนยันก่อน Production
8. Minimal Audit Viewer เป็น Core; Advanced Viewer เป็น Optional

# 10. Import / Export Requirements

## 10.1 Import Pipeline

```text
Upload -> Read & Detect -> Header Mapping -> Row Classification
-> Normalize -> Validate -> Preview -> Duplicate Policy
-> Confirm -> Transactional Import -> Audit / Error Report
```

### Import Invariants

- Preview ห้ามแก้ฐานข้อมูลธุรกิจ
- Blocking Error ห้าม Confirm
- Confirm ใช้ Transaction
- Identifier ห้ามถูกแปลงเป็น Number
- Continuation ห้ามสร้าง Applicant ใหม่
- Batch/Row Result ต้องตรวจย้อนหลังได้

## 10.2 Export Invariants

- ใช้ Query/Calculation Rule เดียวกับ Result Summary
- ใช้เฉพาะ Submitted ที่ยังไม่ยกเลิก
- Excel/CSV ตรงฐานข้อมูล 100%
- Standard Export ไม่รวม Restricted PII
- ทุก Export มี Audit
- Filename มี Round Code, Template Code, Generated Timestamp
- CSV ใช้ UTF-8; ใช้ BOM เมื่อจำเป็นสำหรับ Excel ภาษาไทย


# 11. Acceptance Criteria

| AC ID | Scenario | Given / When / Then | Linked Requirements |
| --- | --- | --- | --- |
| AC-AUT-001 | Login ผ่าน KKU SSO | Given KKU ถูกต้องและ SEMS Active; When Login; Then ได้ Session และเมนูตาม Role. | FR-AUT-001..009 |
| AC-AUT-002 | บัญชี Inactive | Given KKU Auth สำเร็จแต่ SEMS Inactive; When Callback; Then 403 `USER_INACTIVE` และไม่มี Session. | FR-AUT-004 |
| AC-AUT-003 | RBAC | Given EVALUATOR; When เรียก Admin API; Then 403 และ ACCESS_DENIED Audit. | FR-AUT-005..006 |
| AC-RND-001 | เปิดรอบไม่มีเกณฑ์ | Given DRAFT ไม่มี Active Criteria; When Open; Then `ACTIVE_CRITERIA_REQUIRED`. | FR-RND-003 |
| AC-IMP-001 | นำเข้าถูกต้อง | Given XLSX/CSV Mapping/Required ถูก; When Preview+Confirm; Then Applicant/Child/Counts ถูกต้อง. | FR-IMP-001..013 |
| AC-IMP-002 | Missing Required | Given แถวขาดฟิลด์บังคับ; When Validate; Then `REQUIRED_FIELD_MISSING`, Reject และ Blocking. | FR-IMP-007,011 |
| AC-IMP-003 | Scientific Notation | Given student_id `6.6304E+09`; When Validate; Then `INVALID_STUDENT_ID`. | FR-IMP-002 |
| AC-IMP-004 | Continuation ถูกต้อง | Given Continuation หลัง Applicant Valid; When Import; Then History ผูก Applicant ก่อนหน้า. | FR-IMP-004..005 |
| AC-IMP-005 | Orphan Continuation | Given แถวแรกมีเฉพาะทุน; When Validate; Then `ORPHAN_CONTINUATION_ROW`. | FR-IMP-005 |
| AC-IMP-006 | Duplicate ในไฟล์ | Given Key เดิม 2 Applicant Rows; When Validate; Then `DUPLICATE_STUDENT_IN_FILE`. | FR-IMP-008 |
| AC-IMP-007 | Rollback | Given DB Error ระหว่าง Confirm; When Import; Thenไม่มีข้อมูลครึ่งชุดและ Batch FAILED. | FR-IMP-012 |
| AC-DOC-001 | สิทธิ์เอกสาร | Given EVALUATOR ไม่มี Evaluation; When ขอไฟล์; Then 403 และไม่เปิด Storage Path. | FR-DOC-003..004 |
| AC-CRI-001 | ล็อกเกณฑ์ | Given Version มี Active Evaluation; When แก้ max_score; Then `CRITERIA_LOCKED`. | FR-CRI-007 |
| AC-CRI-002 | Versioning | Given ต้องเปลี่ยนเกณฑ์ที่ใช้แล้ว; When สร้าง Version ใหม่; Thenเดิมยังอ้าง Version เดิม. | FR-CRI-008..009 |
| AC-EVA-001 | สร้าง Evaluation | Given Open+Active+Capacity<3+ไม่ซ้ำ; When เลือก Applicant; Thenสร้าง Draft 1 รายการ. | FR-EVA-001 |
| AC-EVA-002 | ผู้ประเมินซ้ำ | Givenมี Draft; When เลือก Applicant เดิม; Then 409 `DUPLICATE_EVALUATION`. | FR-EVA-002 |
| AC-EVA-003 | คนที่ 4 | Given Active=3; Whenคนที่ 4 เลือก; Then 409 `EVALUATOR_LIMIT_REACHED`. | FR-EVA-003 |
| AC-EVA-004 | เลือกพร้อมกัน | Given Active=2; When 2 คนสร้างพร้อมกัน; Thenสำเร็จได้ 1 และสุดท้าย=3. | FR-EVA-004 |
| AC-EVA-005 | คนที่ 3 หลังครบ 2 | Given Submitted=2 และ OPEN; Whenคนที่ 3 Submit; Thenทำได้และ Summary Recalculate. | FR-EVA-005, FR-SCO-007 |
| AC-EVA-006 | กลับมาแก้ Draft | Givenมี Draft แล้ว Active=3; Whenเปิด Draft เดิม; Thenแก้/Submit ได้. | FR-EVA-006 |
| AC-EVA-007 | คะแนนนอกช่วง | Given Criterion 0-10; Whenส่ง 11; Then `SCORE_OUT_OF_RANGE`. | FR-EVA-008 |
| AC-EVA-008 | Draft ไม่คำนวณ | Given Submitted=1 Draft=2; Whenดู Summary; Then score NULL/count=1. | FR-EVA-009, FR-SCO-001,005 |
| AC-EVA-009 | Submit ไม่ครบ | Given Required ว่าง; When Submit; Then `EVALUATION_INCOMPLETE` และยัง DRAFT. | FR-EVA-011 |
| AC-SCO-001 | ครบ 2 คน | Givenคนแรก Submitted; Whenคนที่ 2 Submit; Then Count=2, MINIMUM_COMPLETE, มี Latest Score. | FR-SCO-006 |
| AC-SCO-002 | ครบ 3 คน | Given MINIMUM_COMPLETE; Whenคนที่ 3 Submit; Thenคำนวณ 3 คนและ FULLY_COMPLETE. | FR-SCO-007 |
| AC-SCO-003 | ปัดเศษ | Given Boundary Score; Whenคำนวณ; Then ROUND_HALF_UP เฉพาะ Final 2 ตำแหน่ง. | FR-SCO-004 |
| AC-SCO-004 | ปิดรอบครบ | Given Submitted>=2; When Close; Then FINALIZED และ Final Score ล่าสุด. | FR-RND-006, FR-SCO-009 |
| AC-SCO-005 | ปิดรอบไม่ครบ | Given Submitted<2; When Close; Then CLOSED_INCOMPLETE และ Final Score NULL. | FR-RND-006, FR-SCO-009 |
| AC-EVA-010 | ยกเลิก Draft | Givenเจ้าของ Draft; When Cancel; Then CANCELLED, คืน Slot และมี Audit. | FR-EVA-014 |
| AC-RPT-001 | Export ถูกต้อง | Given Result; When Export; Thenคะแนน/สถานะ/Count ตรง DB 100%. | FR-RPT-003..005 |
| AC-RPT-002 | Export PII | Given Standard Template; When Export; Thenไม่มีเลขบัตร/Restricted Contact. | FR-RPT-007 |
| AC-RPT-003 | Export Audit | When Export สำเร็จ/ล้มเหลว; Thenมี Template/Filter/Count/Result ใน Audit. | FR-RPT-008 |
| AC-DSH-001 | Dashboard consistency | Whenเทียบ Counts/Statuses กับ Reference Query; Thenตรง 100%. | FR-DSH-001..003 |
| AC-SEC-001 | ไม่มี Secret ใน Log | Whenสแกน Log/Audit; Thenไม่พบ Token/Password/Client Secret/Storage Path ลับ. | SEC-012, SEC-015 |
| AC-UAT-001 | UAT Core | EVALUATOR >=2 และ ADMIN/งานทุน >=2 ทำ Core Flow สำเร็จ ไม่มี Critical Defect. | Core FR |
| AC-QA-001 | Core Test Gate | Core Test ผ่าน >=90% และไม่มี Critical Defect ขัดขวาง Core Flow. | Core FR |
| AC-QA-002 | Scoring Accuracy | Test 2/3 Evaluators, Draft Exclusion, Third Recalc, Rounding ตรง Reference 100%. | FR-SCO-* |
| AC-QA-003 | ความพึงพอใจ | คะแนนเฉลี่ยผู้ทดลองใช้ >=4.00/5.00. | NFR-USA-* |

## 11.1 Project Acceptance Gate

1. Core Functional Test ผ่านไม่น้อยกว่า 90%
2. ไม่มี Critical Defect ขัดขวาง Login, Import, Selection, Draft, Submit, Calculation, Close Round หรือ Export
3. Reference Calculation สำหรับ 2/3 Evaluators, Draft Exclusion, Third Submit Recalculation และ Rounding ผ่าน 100%
4. Import ตรวจข้อมูลไม่ครบ ผิดรูปแบบ ซ้ำ และ Continuation ตาม Test Case
5. Excel/CSV ตรง Result Summary และฐานข้อมูล
6. RBAC, Ownership และ Document Access Test ผ่าน
7. UAT โดย EVALUATOR อย่างน้อย 2 คนและ ADMIN/งานทุนอย่างน้อย 2 คนสำเร็จ
8. ความพึงพอใจเฉลี่ยไม่น้อยกว่า 4.00/5.00
9. Source Code, Schema, Migration, Test Report และคู่มือครบ


# 12. Confirmed Release 1 requirements added for baseline review

| ID | Priority | Requirement / measurable acceptance criterion | Decision |
|---|---|---|---|
| FR-APP-008 | Must have | One student may have separate applications for multiple scholarship types in one round; uniqueness is `(scholarship_round_id, scholarship_type_id, student_id)` and each has independent status, documents, Evaluations and Result Summary. Duplicate same-triplet creation returns conflict. | RD-015, RD-024–RD-025 |
| FR-APP-009 | Must have | Before any Evaluation, Admin may update mutable application fields. After any Draft/Submitted Evaluation, score-affecting change requires Controlled Correction with authorization, reason, before/after snapshot and audit; normal update cannot change student, round or scholarship type. | RD-027 |
| FR-EVA-017 | Must have | Evaluation owner may request reopen; staff may request on behalf with actor/reason. Head or official delegate approves; technical Admin cannot self-approve. Reopen returns work to Draft, retains immutable submitted revision and recalculates only after resubmit. | RD-008 |
| FR-EVA-018 | Must have | Owner may cancel Draft with reason; cancellation is soft, audited and atomically releases the active slot. | RD-009 |
| FR-SCO-013 | Must have | `evaluator_total = SUM(10 embedded-point scores)`, maximum 100, with no second `weight_percent` multiplication. `raw_summary = SUM(2–3 distinct Submitted totals)/count`; equal weights; third submission recalculates. | RD-010 |
| FR-SCO-014 | Must have | Preserve full precision and apply `ROUND_HALF_UP(raw_summary, 2)` only to applicant summary. Draft, Reopened and Cancelled records are excluded. | RD-011 |
| FR-SCO-015 | Must have | Custom discretion score is integer 0–10; reason required only when outside standard options or criterion config requires it. Custom Amount is outside the 100 points, requires reason and cannot exceed round/type ceiling. | RD-013, RD-047 |
| FR-CRI-013 | Must have | First Evaluation creation, including Draft, locks the Criteria Version; every Evaluation retains its original version. `criterion_code` is immutable and unique. | RD-012, RD-014 |
| FR-RND-010 | Must have | Close with fewer than two Submitted results shows affected applications, requires explicit Admin confirmation and reason, creates `Closed Incomplete`, and assigns no Final Score. | RD-007 |
| FR-RND-011 | Must have | Closed-round reopen is exceptional and audited; Archived is read-only. A replacement final report never overwrites the old immutable snapshot and marks it `Superseded`. | RD-048–RD-049 |
| FR-IMP-016 | Must have | Duplicate file rows are errors; existing application defaults Skip; never auto-Upsert. Legacy continuation rows end after UAT/first production transition round. Blank/`-`→NULL, zero stays zero, ISO new dates and normalized Preview for declared legacy dates. | RD-017–RD-020 |
| FR-IMP-017 | Must have | Hard Import fields: student ID, names, faculty, program/major, year level and scholarship type in multi-type rounds. Before Evaluation: title, application date, GPA, phone or email, criteria data/documents and Admin validation. Optional fields follow RD-028; config may add pre-evaluation fields without code change. | RD-028 |
| FR-DOC-007 | Must have | Release 1 limits: PDF 20 MB, JPG/PNG 10 MB, 10 applicant files, XLSX/CSV import 20 MB. Reject executable/archive/macro and MIME/extension/signature mismatch. Production files remain Quarantined and unavailable until malware scan passes. | RD-038–RD-039 |
| FR-RPT-010 | Must have | Excel has Summary and Evaluator Detail; CSV has two files, optionally ZIP. Profiles are `INTERNAL_FULL` and `SUMMARY_MASKED`; standard exports exclude national ID and contacts. Interim file expires ≤30 days; final snapshot is immutable for six years. | RD-021–RD-022, RD-031–RD-032 |
| FR-COD-001 | Must have | Admin manages versioned CodeList/CodeListValue; inactive values remain readable historically and every mutation is audited. | RD-046 |
| FR-AUT-011 | Must have | Admin pre-provisions account/role; first login binds KKU `sub`; missing account returns `USER_NOT_PROVISIONED`; inactive account is denied on next API request. Evaluator sees only own Evaluation plus slot/Submitted/minimum-completion counts. | RD-036–RD-037 |
| NFR-SEC-010 | Must have | Idle timeout 30 minutes, absolute lifetime 8 hours, revocable secure session; storage encryption, authorized short-lived file download, data minimization and no national ID in Core Flow, schema, UI, export, logs or tests. | RD-029, RD-034–RD-035 |
| NFR-RET-001 | Must have | Core records retain six years from round close; interim exports 30 days; final snapshots six years; rotating backups at least 90 days; secure deletion except Legal Hold/policy. | RD-030–RD-033 |
| NFR-BCP-001 | Must have | RPO ≤24h, RTO ≤8 business hours; daily DB and weekly full backup; storage consistent with DB; restore test quarterly and before go-live. | RD-041 |
| NFR-CAP-001 | Must have | Load-test design baseline uses RD-040 targets and labels them targets, not measurements. Capture operational measurements before asserting achieved capacity or performance. | RD-040 |

Formal approver names, approval date/signature/evidence, actual production assignments and RD-040/RD-045 measurements remain pending external records. They are not Open business-logic decisions.

# 13. Traceability Summary

| Source | SRS Section |
|---|---|
| Proposal: ผู้ใช้ SSO/RBAC รอบทุน Import Applicant Document Criteria Evaluation 2-3 คน Scoring Report Audit | Sections 2-11 |
| Requirement Decision Register RD-001 ถึง RD-049 | FR-EVA, FR-SCO, FR-CRI, FR-IMP, FR-RPT, FR-RND, FR-APP, FR-AUT, FR-DOC and NFRs in Section 12 |
| Traceability Matrix | [`SEMS_Traceability_Matrix.md`](../SEMS_Traceability_Matrix.md) |
| Applicant Import Mapping | FR-IMP, Validation, Error Codes, Import Acceptance |
| Data Dictionary | Section 6, Validation, Security/PII |
| Criteria Workbook | FR-CRI, FR-EVA, FR-SCO, RD-012-014 |
| KKU OAuth/OIDC Summary | FR-AUT และ SEC-002..004 |

# 14. Definition of Ready

Requirement พร้อม Development เมื่อ:

- Status เป็น `Confirmed`
- Acceptance Criteria, Data/Validation/Error Code, Permission และ Audit ชัดเจน
- ไม่มี Open Decision ที่เปลี่ยน Business Logic
- UI/API/Database Owner เข้าใจผลลัพธ์ตรงกัน

# 15. Definition of Done

- Code Review ผ่าน
- Unit/Integration/API Authorization/Validation Test ผ่าน
- Audit และ Error Code ทำงานตาม SRS
- Migration/Seed/Config ครบ
- Acceptance Criteria ผ่านใน Test Environment
- เอกสารและ Traceability อัปเดต
