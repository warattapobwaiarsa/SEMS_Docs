# รายงานการตรวจเอกสาร SEMS

| Metadata | Value |
|---|---|
| Document ID | `SEMS-DOC-REVIEW-001` |
| Version | **v0.8** |
| Last Updated | **2026-08-05** |
| Status | **Ready for Formal Stakeholder Review — Pending Formal Approval** |
| Review Scope | Requirements, API error contract, UI/UX presentation artifacts และ repository indexes |
| Branch | `main` |
| Review-start Commit | `07600b6` |
| Approval Status | **Pending — ยังไม่มีชื่อผู้อนุมัติ วันที่ตัดสินใจ หรือหลักฐานที่ตรวจสอบได้** |

[START HERE](./START_HERE.md) › [Repository Index](./README.md) › รายงานการตรวจเอกสาร SEMS

## 1. สรุปสำหรับผู้บริหาร

เอกสาร Requirement พร้อมใช้ประกอบการนำเสนอและ Formal Review มากขึ้น โดย SRS ใช้ Version/Last Updated ตรงกัน, คำศัพท์ Status ของ Requirement ใช้ `Confirmed`, `Provisional`, `Open`, API Error Response ใช้ `{code, message, details[], traceId, timestamp}` และ Stakeholder Summary แสดง Release 1, MoSCoW, ผู้ใช้งาน และประเด็นรอยืนยันในหน้าเดียว

เอกสารยังเป็น **Baseline Candidate — Pending Formal Approval** และไม่ใช่หลักฐานว่า System Design, Test Execution, UAT หรือ Production Readiness ได้รับการอนุมัติแล้ว

## 2. Files Changed

- `README.md`
- `DOCUMENTATION_REVIEW_REPORT.md`
- `REPOSITORY_TREE.md`
- `Requirements/README.md`
- `Requirements/SRS/SEMS-SRS.md`
- `Requirements/User_Stories/README.md`
- `Requirements/User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md`
- `Requirements/SEMS_MoSCoW_Stakeholder_Summary.md`
- `scripts/check-document-versions.py`

## 3. Changes Made

### `Requirements/SRS/SEMS-SRS.md`

- คง Current Version เป็น `v0.6` และทำตารางภายในเป็น `0.6-draft`
- ทำ Last Updated และ Document History ให้ตรงกับวันที่ 2026-08-05
- ใช้ `Confirmed` แทน `Confirmed Response` เฉพาะคอลัมน์ Status โดยไม่เปลี่ยน Requirement ID หรือ Business Rule
- คงสถานะ `Baseline Candidate — Pending Formal Approval`

### `Requirements/User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md`

- อัปเดตเป็น v0.7
- แก้ API Error Response จาก `error_code` เป็น `code` และระบุ envelope มาตรฐานที่ไม่มี object `error` ครอบ
- ไม่เปลี่ยน User Story ID หรือ Acceptance Criteria ID

### `Requirements/SEMS_MoSCoW_Stakeholder_Summary.md`

- อัปเดตเป็น v0.2 และจัดหัวข้อ 1–11 ตามลำดับสำหรับการนำเสนอ
- เพิ่มตาราง Function พร้อมผู้ใช้งาน Priority, Release, สถานะ และแหล่งอ้างอิง
- แบ่ง Function เป็น `ADMIN`, `EVALUATOR` และระบบอัตโนมัติ
- เพิ่ม Core Workflow, Out of Scope, ช่องว่างความพร้อม และคำถาม 15 ข้อที่มีสถานะ `Pending Formal Review`
- คงการจัดกลุ่มเดิม: Must have 11, Should have 6, Could have 4 และ Won't have 6 รายการระดับสรุป

### Index และเครื่องมือตรวจ

- เพิ่ม Presentation Guide ใน `Requirements/README.md`
- ซิงก์ Version, Last Updated และ Status ใน Requirements/User Stories/Root indexes และ Repository Tree
- ปรับตัวตรวจ Version ให้ยอมรับสถานะมาตรฐานที่ใช้ em dash ตรงกับเอกสารและ Index

## 4. Consistency Checks

| Check | Result |
|---|---|
| Version consistency | PASS — SRS v0.6/0.6-draft และ Index ที่เกี่ยวข้องตรงกัน |
| Status consistency | PASS — ไม่มีการเปลี่ยนเอกสารเป็น `Approved`; baseline ยัง Pending Formal Approval |
| Requirement status vocabulary | PASS — SRS ใช้เฉพาะ `Confirmed`, `Provisional`, `Open` ในคอลัมน์ Status |
| API error contract | PASS — SRS, User Stories, API Specification, Error Catalog และ OpenAPI ใช้ `code`, `message`, `details`, `traceId`, `timestamp` โดยไม่มี wrapper `error` |
| Markdown links | PASS — ตัวตรวจ link รายงาน 68 Markdown files, 0 errors |
| Document navigation | PASS — navigation เดิมยังอยู่และ Presentation Guide เชื่อมไฟล์จริง |
| MoSCoW grouping | PASS — ไม่ย้ายรายการระหว่าง Must/Should/Could/Won't |
| Requirement/User Story/Trace/API ID preservation | PASS — ไม่มีการแก้ ID หรือ `operationId` ใน diff |
| PII and secret-pattern review | REVIEW REQUIRED — ไม่พบ secret value ในชุดนำเสนอ แต่พบข้อมูลที่ต้องให้เจ้าของยืนยันก่อน Public Release ตามหัวข้อ 5 |

## 5. Items Not Changed

- `Design/API/SEMS_API_Specification.md`, `Design/API/SEMS_Error_Code_Catalog.md` และ `Design/API/openapi.yaml` ไม่แก้ เพราะ Error Contract ถูกต้องอยู่แล้ว
- `Requirements/SEMS_Requirement_Decision_Register.md` และ `Requirements/SEMS_Traceability_Matrix.md` ไม่เปลี่ยนคำว่า `Confirmed Response` เพราะใช้เป็นสถานะของคำตอบ/หลักฐาน ไม่ใช่คอลัมน์ Status ของ Requirement
- `START_HERE.md` ไม่แก้ เพราะชื่อไฟล์และลำดับการอ่านหลักไม่เปลี่ยน และหน้าไม่ได้แสดง Version ของเอกสารที่ปรับ
- ไม่แก้ Binary File หรือข้อมูลตัวอย่างโดยอัตโนมัติ
- `Design/UI_UX/SEMS_Wireframe_Prototype.html:75` มีรหัสนักศึกษาที่ตรงกับข้อมูลผู้จัดทำใน `README.md:31`; ต้องยืนยันสิทธิ์เผยแพร่หรือแทนด้วยข้อมูลสังเคราะห์
- `Design/UI_UX/SEMS_Wireframe_Prototype.html:82` มีหมายเลขโทรศัพท์รูปแบบใช้งานจริง; แม้มีลักษณะเป็นข้อมูลตัวอย่าง ควรให้เจ้าของยืนยันก่อนเผยแพร่
- แถวตัวอย่างอื่นใน Wireframe ใช้ชื่อ placeholder และรหัสแบบมี pattern จึงมีแนวโน้มเป็นข้อมูลสังเคราะห์ แต่ควรบันทึกการยืนยันจาก Data Owner
- `README.md:31-32` และ `Requirements/Proposal/SEMS-project-proposal.md:32-37` มีชื่อและรหัสนักศึกษาของผู้จัดทำ; ไม่ลบเพราะเป็นข้อมูล attribution แต่ต้องยืนยันความยินยอมสำหรับ Public Repository

## 6. Pending Stakeholder Decisions

1. ยืนยันผู้ใช้งาน Release 1 และการไม่มีบัญชีนักศึกษาผู้สมัคร
2. ยืนยัน self-selection และผู้ประเมินไม่ซ้ำกัน 2–3 คน
3. ยืนยันการใช้เฉพาะ `SUBMITTED` และการคำนวณใหม่เมื่อคนที่ 3 Submit
4. ตัดสิน Release ของ `Cancel Draft`, `Reopen Submitted Evaluation`, `Controlled Round Reopen` และ `Controlled Correction`
5. ตัดสินความจำเป็นของ Dashboard Drill-down และรูปแบบ/สิทธิ์รายงาน
6. ยืนยันการไม่ใช้ National ID ใน Release 1 Core Flow
7. ระบุผู้มีอำนาจอนุมัติ Requirement Baseline และรูปแบบหลักฐานอนุมัติ
8. ยืนยัน KKU Client Configuration, Infrastructure, Malware Scanner และ Report Template
9. ระบุผู้เข้าร่วม วันที่ และผล UAT จริง
10. ยืนยันหรือทำข้อมูลตัวอย่างให้เป็นข้อมูลสังเคราะห์ก่อน Public Release

## 7. Suggested Commit Message

`docs: prepare SEMS requirements for stakeholder presentation`

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.8 | 2026-08-05 | SEMS Documentation Team | บันทึกการเตรียม SRS, API Error Contract, Stakeholder Summary, Presentation Guide, consistency checks และรายการ PII ที่ต้องยืนยัน โดยคงสถานะ Pending Formal Approval |
| v0.7 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.6 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.5 | 2026-07-24 | SEMS Documentation Team | Added lifecycle navigation and refreshed enhanced version/status and wireframe-manifest validation results. |
| v0.4 | 2026-07-24 | SEMS Documentation Team | Synchronized confirmed responses across requirements/design/data/API/UI/testing, updated workbooks, added test/UAT coverage and retained formal approval boundaries. |
| v0.3 | 2026-07-24 | SEMS Documentation Team | Recorded pre-baseline repository metadata, PII risks and partial validation evidence. |
| v0.2 | 2026-07-23 | SEMS Documentation Team | Recorded link/version/JSON checks and independent validator limitation. |
| v0.1 | 2026-07-23 | SEMS Documentation Team | Initial repository reconciliation report. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [ข้อเสนอโครงการ SEMS](./Requirements/Proposal/SEMS-project-proposal.md)<br>
↑ หมวดเอกสาร: [Scholarship Evaluation Management System (SEMS)](./README.md)<br>
⌂ หน้าหลัก: [START HERE](./START_HERE.md)<br>
→ อ่านต่อ: [SEMS Product Requirements Document](./Requirements/PRD/SEMS-PRD.md)

<!-- DOC_NAV_END -->
