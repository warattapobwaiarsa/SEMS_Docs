# SEMS Master Test Plan

| รายการ | ค่า |
|---|---|
| Document ID | SEMS-TP-001 |
| Version | **v0.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft for Design Baseline** |
| System | Scholarship Evaluation Management System (SEMS) |
| Test Approach | Risk-based, Requirements-based, API-first และ End-to-End |
| Primary Roles | Admin, Evaluator |
| Target Environments | Development, Testing/UAT, Production-like |

## 1. วัตถุประสงค์

แผนนี้กำหนดขอบเขต วิธีการ ข้อมูลทดสอบ เกณฑ์เริ่ม/จบ การจัดการข้อบกพร่อง และ Test Deliverables ก่อนเริ่มพัฒนา เพื่อให้ Business Rule สำคัญถูกออกแบบให้ทดสอบได้ตั้งแต่ระดับ Database, Service, API และ Browser

เป้าหมายหลักคือ:

1. ป้องกันผู้ประเมินคนเดิมประเมินผู้สมัครซ้ำในรอบเดียวกัน
2. ควบคุม Evaluation ที่ใช้งานอยู่ไม่เกิน 3 รายการต่อผู้สมัครต่อรอบ แม้มีคำขอพร้อมกัน
3. ใช้เฉพาะผล `Submitted` จากผู้ประเมินที่ไม่ซ้ำกันในการคำนวณ
4. คำนวณผลสรุปเมื่อครบ 2 คน และคำนวณใหม่เมื่อคนที่ 3 Submit ก่อนปิดรอบ
5. เปลี่ยนสถานะผู้สมัครและรอบทุนอย่างถูกต้องเมื่อปิดรอบ
6. ตรวจสอบไฟล์นำเข้า 37 คอลัมน์ รวมถึงผู้สมัครหนึ่งคนที่กินพื้นที่หลายแถว
7. ป้องกันการเข้าถึงข้อมูลและเอกสารนอกสิทธิ์
8. ยืนยันว่า Dashboard, Result Summary, Excel และ CSV ตรงกับฐานข้อมูล
9. ยืนยัน multi-scholarship business key, Controlled Correction, reopen/revision, report snapshots, retention, session, quarantine/malware scanning, backup/restore and national-ID absence

## 2. Test Basis

- Proposal: ขอบเขตผู้ใช้ ฟังก์ชัน Core, Business Rule 2–3 Evaluators, Draft/Submitted, State, Import, Report, Security และ Audit
- Import sample: 37 คอลัมน์, วันที่รูปแบบภาษาไทย/พ.ศ., พิกัดแบบ `latitude, longitude`, รายการ กยศ./ทุนหลายปี และ continuation row
- Criteria sample: 10 หัวข้อคะแนนรวมเต็ม 100 คะแนน พร้อมตัวเลือกคะแนนแบบ lookup
- KKU OAuth/OIDC summary: Authorization Code + PKCE S256, `state`, `nonce`, ID Token, `/userinfo`, revocation และ logout
- SRS, User Stories, Permission Matrix, State Transition, API Specification และ Database Schema ฉบับอนุมัติในอนาคต

## 3. Success Criteria

- Test Case ของ Core Function ผ่านไม่น้อยกว่า 90%
- ไม่มี Defect ระดับ Critical ที่ขัดขวาง Core Flow
- ชุดข้อมูลอ้างอิงด้านคะแนนผ่าน 100%
- กรณี Draft, Submitted 2 คน, Submitted 3 คน และผู้ประเมินคนที่ 4 ถูกต้องทุกกรณี
- Import ตรวจพบข้อมูลไม่ครบ ผิดรูปแบบ ซ้ำ และ continuation row ผิดกฎ
- Excel/CSV, Dashboard และ Result Summary ตรงกับฐานข้อมูล
- UAT โดย Evaluator อย่างน้อย 2 คน, Admin/เจ้าหน้าที่อย่างน้อย 2 คน และ IT/Infrastructure อย่างน้อย 1 คนสำหรับ deployment/backup scenario สำเร็จโดยไม่มี Critical Defect

## 4. ขอบเขตการทดสอบ

### 4.1 In Scope

- KKU SSO callback, local account activation, session และ logout
- RBAC ระดับเมนู หน้า API ข้อมูล และ ownership
- User, Scholarship Round และ Criteria Set
- Applicant Import, Column Mapping, Preview, Validation, Confirm และ Import History
- Applicant data, scholarship/loan history และ document access
- Evaluator Selection และ concurrency control
- Draft, Review, Submit, Cancel และ Reopen ตามนโยบาย
- Score validation, evaluator total, result aggregation และ recalculation
- Applicant state และ close-round processing
- Dashboard, Result Summary, Excel/CSV Export และ Audit Log
- Security, regression, basic performance และ recovery ที่เกี่ยวข้องกับ Core Flow

### 4.2 Out of Scope

- ระบบสมัครทุนของนักศึกษา
- การจัดคิว/ห้องสัมภาษณ์และระบบประชุมออนไลน์
- การตัดสินอนุมัติทุนขั้นสุดท้าย การประกาศผล และการโอนเงิน
- Native Mobile Application
- PDF Export และ Custom Report Template หากยังเป็น Optional Scope
- การทดสอบระบบ KKU SSO ภายใน ซึ่งอยู่นอกการควบคุมของ SEMS; ทดสอบเฉพาะ integration contract และ error handling

## 5. Risk-based Priority

| Priority | ความหมาย | แนวทาง |
|---|---|---|
| P0 | ข้อมูลผิด สิทธิ์รั่ว คะแนนผิด หรือ Core Flow ใช้ไม่ได้ | ต้องมี Unit + Integration/API + E2E และรันทุก release |
| P1 | ฟังก์ชันหลักผิดแต่มีทางเลี่ยง | รันทุก Sprint ที่เกี่ยวข้องและก่อน UAT |
| P2 | ฟังก์ชันสนับสนุนหรือ UX | รันก่อน Release Candidate |
| P3 | Optional/Low impact | รันเมื่อฟังก์ชันพร้อมและมีเวลา |

P0 ได้แก่ selection concurrency, uniqueness, authorization, Draft exclusion, aggregation, round closing, import integrity และ report reconciliation

## 6. Test Levels และ Test Types

| ระดับ/ประเภท | เป้าหมาย | เครื่องมือแนะนำ |
|---|---|---|
| Unit Test | Validation, state resolver, scoring, parser และ permission predicate | Jest |
| Database Test | Unique constraint, transaction, lock, one-summary-per-applicant-round | Jest + Test PostgreSQL |
| Integration/API | Request/response, validation, RBAC, error code, audit | Jest/Supertest หรือ Postman/Newman |
| Component/UI | Form validation, state rendering, disabled controls | Testing Library |
| End-to-End | Login → Select → Draft → Review → Submit → Summary → Export | Playwright |
| Concurrency | simultaneous selection/submit, retry และ idempotency | Integration script/k6/custom barrier |
| Security | Broken access control, IDOR, session, file access, log leakage | API tests + OWASP ZAP แบบจำกัดขอบเขต |
| Data Reconciliation | DB ↔ Result Summary ↔ Dashboard ↔ Export | SQL + test script |
| UAT | ผู้ใช้ดำเนิน Core Flow ตามบทบาท | Guided scenario |
| Regression | ป้องกัน defect เดิมกลับมา | Automated smoke + manual checklist |

## 7. Test Environment

### 7.1 Minimum Test Stack

- Next.js Frontend build ใกล้เคียง Production
- NestJS Backend build ใกล้เคียง Production
- PostgreSQL version เดียวกับเป้าหมายติดตั้ง
- Test File Storage แยกจากข้อมูลจริง
- HTTPS หรือ reverse proxy ใน Production-like environment
- KKU SSO Development/Test Client หรือ OIDC Mock ที่รองรับ PKCE, state และ nonce
- Clock synchronized เพื่อทดสอบ token/session expiry และ audit timestamp

### 7.2 Environment Isolation

- ห้ามใช้ข้อมูลจริงโดยไม่ได้รับอนุญาต
- ใช้ synthetic/anonymized data
- แยก Database, File Storage, secrets และ client credentials ของแต่ละ environment
- Resettable seed และ repeatable migration
- เก็บ test artifact โดยไม่รวม token, password หรือข้อมูลส่วนบุคคลละเอียดอ่อน

## 8. Test Data Strategy

ใช้ชุดข้อมูลหลักจาก `SEMS_Test_Data_and_Environment_Plan.md` โดยต้องมี:

- Admin 2 บัญชี, Evaluator Active 4 บัญชี, Evaluator Inactive 1 บัญชี
- Round: Draft, Open, Closed และ Archived
- Applicant ที่มี 0, 1 Draft, 1 Submitted, 2 Submitted และ 3 Submitted
- Applicant ที่มี Evaluation ถูก Cancel เพื่อทดสอบการคืน slot
- Score vectors ที่ให้ผลรวมต่ำสุด กลาง สูงสุด และ boundary
- Import files ทั้ง valid, invalid, duplicate, multi-row, orphan continuation และ malformed coordinates
- Documents: PDF/JPG/PNG ถูกต้อง, MIME mismatch, oversized และ filename เสี่ยง path traversal

## 9. Entry Criteria

### 9.1 Unit/Integration

- Requirement/Acceptance Criteria ของฟังก์ชันผ่าน review
- Database migration และ seed รันได้
- API contract ระบุ method, role, validation และ error code
- Business rule ไม่มีประเด็น Critical ที่ยังไม่ตัดสินใจ

### 9.2 System/E2E

- Core endpoints เชื่อมกันได้
- Test environment stable
- Test accounts และ files พร้อม
- Known blocker ถูกบันทึกและมี owner
- Build มี version/commit hash ที่ตรวจสอบย้อนกลับได้

### 9.3 UAT

- P0/P1 functional tests ผ่าน
- ไม่มี Critical/Open High defect ที่กระทบ UAT flow
- Test data และคู่มือ scenario พร้อม
- ผู้ใช้ UAT ได้รับบัญชีและข้อมูลจำลอง

## 10. Exit Criteria

- Core Test Case Pass ≥ 90%
- P0 ต้องผ่าน 100%
- ไม่มี Critical defect คงค้าง
- High defect ต้องปิดหรือมี documented acceptance จาก Product Owner
- Score reference set และ reconciliation ผ่าน 100%
- Security test ของ ownership/document/API ผ่าน
- Regression suite ผ่านหลังแก้ defect
- UAT sign-off และ Test Summary Report พร้อม

## 11. Defect Severity

| Severity | เกณฑ์ | ตัวอย่าง |
|---|---|---|
| Critical | Core Flow ใช้ไม่ได้ ข้อมูลเสียจำนวนมาก คะแนนผิดหรือข้อมูลรั่ว | ผู้ประเมินคนที่ 4 สร้างได้, เอกสารเปิดข้ามสิทธิ์, Export คะแนนผิด |
| High | ฟังก์ชันหลักผิด กระทบหลายผู้ใช้ ไม่มี workaround ที่เหมาะสม | Draft ถูกนำไปคำนวณ, close-round state ผิด |
| Medium | ฟังก์ชันบางส่วนผิด มี workaround | filter ผิดบางเงื่อนไข, error message ไม่ชัด |
| Low | Cosmetic/wording/layout | label, spacing, typo |

## 12. Defect Workflow

`New → Triaged → Assigned → In Progress → Ready for Retest → Verified → Closed`

กรณีไม่แก้ให้ใช้ `Rejected`, `Duplicate`, `Deferred` หรือ `Accepted Risk` พร้อมเหตุผล ผู้อนุมัติ และ release เป้าหมาย

## 13. Evidence ที่ต้องเก็บ

- Build number / commit hash
- Test Case ID และ test data ID
- Request/response ที่ตัด token และ PII ออก
- Screenshot/recording เมื่อจำเป็น
- SQL query/result สำหรับ constraint และ reconciliation
- Export file hash และ row count
- Audit event ที่เกี่ยวข้อง
- Defect ID และ retest evidence

## 14. Automation Strategy

### 14.1 Must Automate

- score validation และ aggregation
- state resolver
- duplicate evaluator และ max-3 constraint
- concurrent selection
- Draft exclusion
- import parser/validator
- RBAC/ownership API tests
- report reconciliation

### 14.2 E2E Smoke

1. Admin login และเปิดรอบ
2. Import applicant valid file
3. Evaluator 1 เลือก บันทึก Draft และ Submit
4. Evaluator 2 Submit แล้วเกิด Minimum Complete
5. Evaluator 3 Submit แล้วเกิด Fully Complete และคะแนนเปลี่ยน
6. Admin close round แล้วเกิด Finalized
7. Export Excel/CSV และเทียบกับ DB

## 15. Provisional Error Contract

| Error Code | HTTP ที่แนะนำ | ความหมาย |
|---|---:|---|
| AUTH_REQUIRED | 401 | ไม่มี session/token ที่ใช้ได้ |
| USER_INACTIVE | 403 | บัญชี SEMS ไม่ Active |
| ACCESS_DENIED | 403 | Role หรือ ownership ไม่อนุญาต |
| ROUND_NOT_OPEN | 409 | รอบทุนไม่อยู่สถานะ Open |
| DUPLICATE_EVALUATION | 409 | Evaluator เดิมมี active evaluation อยู่แล้ว |
| EVALUATOR_LIMIT_REACHED | 409 | Applicant มี active evaluation ครบ 3 |
| EVALUATION_ALREADY_SUBMITTED | 409 | ส่งผลซ้ำหรือแก้ Submitted โดยไม่ Reopen |
| SCORE_OUT_OF_RANGE | 422 | คะแนนต่ำกว่า min หรือสูงกว่า max |
| REQUIRED_FIELD_MISSING | 422 | ข้อมูลบังคับหาย |
| INVALID_GPA | 422 | GPA นอก 0.00–4.00 หรือแปลงไม่ได้ |
| INVALID_DATE | 422 | วันที่แปลงไม่ได้ |
| DUPLICATE_STUDENT | 409/422 | รหัสนักศึกษาซ้ำตาม import policy |
| INVALID_COORDINATE | 422 | พิกัดผิดรูปแบบหรือเกินช่วง |
| ORPHAN_CONTINUATION_ROW | 422 | continuation row ไม่มี base row ก่อนหน้า |
| UNSUPPORTED_FILE_TYPE | 415 | ชนิดไฟล์ไม่รองรับ |
| IMPORT_FILE_TOO_LARGE | 413 | ไฟล์ Import เกินขนาด |
| DOCUMENT_TOO_LARGE | 413 | Applicant Document เกินขนาด |
| CRITERIA_LOCKED | 409 | เกณฑ์เริ่มถูกใช้งานแล้ว |

## 16. Decision Pending ก่อน Freeze Expected Result

| เรื่อง | ผลกระทบต่อ Test | ต้องยืนยันโดย |
|---|---|---|
| สูตรรวม 2–3 ผู้ประเมิน | Expected score ของ SCR/REP | งานทุน/Product Owner |
| การปัดเศษและจำนวนทศนิยม | boundary และ report | งานทุน/Product Owner |
| ความคิดเห็นบังคับหรือไม่ | submit validation | งานทุน/Product Owner |
| Reopen Policy และผู้อนุมัติ | Submitted → Reopened | งานทุน/Admin Owner |
| Import Atomic หรือ Partial | batch result/rollback | Product Owner/Tech Lead |
| Duplicate policy ข้ามรอบ | import validation | Product Owner |
| ขนาดไฟล์/เอกสารสูงสุด | upload test | Infra/Product Owner |
| Session timeout/refresh | auth test | Security/Tech Lead |
| Report fixed template | column/order/format | งานทุน |
| Cancellation policy | slot counting/audit | Product Owner |

## 17. Deliverables

- Master Test Plan
- Risk and Coverage Matrix
- Test Data and Environment Plan
- Detailed High Risk Test Cases
- Functional Test Case Catalog
- Import, Security/RBAC/SSO, Scoring/State/Report test suites
- Regression Checklist
- Test Execution Evidence
- Defect Log
- Test Summary Report และ UAT Sign-off

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS QA Team | Aligned inactive-user and module-specific size errors with the canonical inventory. |
| v0.2 | 2026-07-23 | SEMS QA Team | Aligned canonical evaluation error code and pre-baseline documentation checks. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial master test plan draft. |
