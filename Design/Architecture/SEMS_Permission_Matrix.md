# SEMS Permission Matrix

| Metadata | Value |
| :--- | :--- |
| Version | **v1.2** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Design Team** |
| Status | **Draft** |
| Primary Roles | `ADMIN`, `EVALUATOR` |

> เอกสารนี้ใช้สำหรับออกแบบ RBAC, Route Guard, API Authorization, Row-level Access Control และ Test Case ด้านสิทธิ์ โดยอ้างอิงขอบเขตใน SEMS Project Proposal หมวด 5.1, 5.2.1, 5.2.8, 5.2.9, 5.2.11 และ 5.5

---

## 1. คำอธิบายสัญลักษณ์

| สัญลักษณ์ | ความหมาย |
|---|---|
| ✅ | อนุญาต |
| 🔎 | ดูได้อย่างเดียว ไม่สามารถแก้ไขหรือดำเนินการแทนได้ |
| ⚠️ | อนุญาตแบบมีเงื่อนไข ต้องผ่าน Role, Ownership, Round Status, Account Status หรือ Evaluation Status |
| ❌ | ไม่อนุญาต |

---

## 2. หลักการควบคุมสิทธิ์

1. ผู้ใช้ทุกคนต้องยืนยันตัวตนผ่าน KKU SSO และต้องมีบัญชี SEMS สถานะ `Active`
2. Frontend ใช้สิทธิ์เพื่อซ่อนเมนูและป้องกันการเข้าหน้า แต่ Backend ต้องตรวจสอบสิทธิ์ซ้ำทุก API
3. สิทธิ์ของผู้ประเมินต้องตรวจสอบทั้งบทบาทและความเป็นเจ้าของ Evaluation
4. ผู้ประเมินเห็นรายละเอียดและเอกสารของผู้สมัครได้หลังจากเลือกผู้สมัครและระบบสร้าง Evaluation ให้แล้ว
5. ผู้ประเมินแก้ไขและ Submit ได้เฉพาะ Evaluation ของตนเอง
6. Admin ตรวจสอบ Evaluation ได้ แต่ต้องไม่แก้คะแนน ความคิดเห็น หรือ Submit แทนผู้ประเมิน
7. การ Reopen ผลหลัง Submit เป็นสิทธิ์ของ Admin ตามนโยบายที่ได้รับอนุมัติ และผู้ประเมินเจ้าของผลเป็นผู้แก้ไขและ Submit ใหม่
8. เมื่อรอบทุน `Closed` หรือ `Archived` ห้ามสร้าง Evaluation ใหม่และห้าม Submit เพิ่ม เว้นแต่มีการเปิดรอบหรือ Reopen ตามขั้นตอนที่กำหนด
9. การเข้าถึงไฟล์เอกสารต้องผ่าน Backend Authorization ห้ามเปิด File Path หรือ Object URL แบบสาธารณะ
10. การปฏิเสธสิทธิ์และการดำเนินการสำคัญต้องบันทึก Audit Log ตามขอบเขตที่กำหนด

---

## 3. Permission Matrix ระดับหน้าจอและฟังก์ชัน

| รหัส | หน้าจอ/ฟังก์ชัน | Admin | Evaluator | เงื่อนไขและขอบเขตข้อมูล |
|---|---|---:|---:|---|
| PM-001 | Login ด้วย KKU SSO | ✅ | ✅ | ต้องมี SEMS User และสถานะ `Active` จึงสร้าง Session ได้ |
| PM-002 | Logout | ✅ | ✅ | ยกเลิก SEMS Session ตาม Logout Policy |
| PM-003 | ดูข้อมูลบัญชีตนเอง | ✅ | ✅ | เห็นเฉพาะข้อมูลบัญชีที่จำเป็นต่อการใช้งาน |
| PM-004 | Dashboard ผู้ดูแลระบบ | ✅ | ❌ | แสดงจำนวนผู้สมัคร สถานะ และผลสรุปตามรอบทุน |
| PM-005 | Dashboard งานประเมินของตนเอง | ⚠️ | ✅ | Admin ไม่จำเป็นต้องมีหน้าประเมินส่วนตัว; Evaluator เห็นเฉพาะรายการของตน |
| PM-006 | จัดการผู้ใช้งาน SEMS | ✅ | ❌ | เชื่อม KKU Identity, กำหนดบทบาท, เปิด/ปิดสิทธิ์; ไม่จัดการรหัสผ่าน KKU |
| PM-007 | ดูรายชื่อผู้ใช้งาน | ✅ | ❌ | จำกัดข้อมูลเท่าที่จำเป็นต่อการบริหารสิทธิ์ |
| PM-008 | สร้างรอบทุน | ✅ | ❌ | รอบใหม่เริ่มต้นเป็น `Draft` |
| PM-009 | แก้ไขรอบทุน | ⚠️ | ❌ | จำกัดตามสถานะ และห้ามแก้ไขข้อมูลที่กระทบผลเมื่อมีการประเมินแล้ว |
| PM-010 | เปลี่ยนสถานะรอบทุน | ⚠️ | ❌ | ใช้ State Transition ที่กำหนด เช่น Draft → Open → Closed → Archived |
| PM-011 | ดูรายการรอบทุน | ✅ | ⚠️ | Evaluator เห็นเฉพาะรอบที่เกี่ยวข้อง โดยปกติคือรอบ `Open` และรายการของตนในรอบที่ผ่านมา |
| PM-012 | Import ผู้สมัคร | ✅ | ❌ | รองรับ CSV/Excel, Preview, Mapping, Validation และ Confirm Import |
| PM-013 | ดูประวัติการ Import | ✅ | ❌ | เห็นชื่อไฟล์ ผู้ดำเนินการ เวลา จำนวนสำเร็จและผิดพลาด |
| PM-014 | แก้ไขข้อมูลผู้สมัคร | ⚠️ | ❌ | Admin แก้ได้ตามสถานะรอบและต้องไม่ทำลายความสอดคล้องของผลประเมิน |
| PM-015 | ดูรายชื่อผู้สมัครในรอบเปิด | ✅ | ✅ | Evaluator เห็นเฉพาะข้อมูลขั้นต่ำสำหรับค้นหาและเลือก เช่น รหัส ชื่อ นามสกุล และสถานะที่จำเป็น |
| PM-016 | ดูรายละเอียดผู้สมัคร | ✅ | ⚠️ | Evaluator ดูได้เฉพาะผู้สมัครที่ตนเลือกและมี Evaluation ที่ยังใช้งานอยู่ |
| PM-017 | ค้นหา/กรองผู้สมัคร | ✅ | ⚠️ | Evaluator ค้นหาได้เฉพาะรอบที่ `Open` และข้อมูลที่อนุญาต |
| PM-018 | อัปโหลดเอกสารผู้สมัคร | ✅ | ❌ | ตรวจชนิดไฟล์ ขนาดไฟล์ และบันทึกผู้ Upload |
| PM-019 | ลบ/แทนที่เอกสารผู้สมัคร | ⚠️ | ❌ | ต้องตรวจผลกระทบและเก็บ Audit; อาจจำกัดเมื่อเริ่มประเมินแล้ว |
| PM-020 | เปิดดู/ดาวน์โหลดเอกสารผู้สมัคร | ✅ | ⚠️ | Evaluator เฉพาะผู้สมัครที่ตนเลือก; ตรวจสิทธิ์ทุกครั้งผ่าน Backend |
| PM-021 | จัดการประวัติทุนย้อนหลัง | ✅ | ❌ | นำเข้าและแก้ไขตามขอบเขตข้อมูล |
| PM-022 | ดูประวัติทุนย้อนหลัง | ✅ | ⚠️ | Evaluator เฉพาะผู้สมัครที่ตนเลือก |
| PM-023 | สร้างชุดเกณฑ์คะแนน | ✅ | ❌ | แยกตามรอบทุนและเวอร์ชัน |
| PM-024 | แก้ไขเกณฑ์คะแนน | ⚠️ | ❌ | ห้ามแก้ Version ที่ถูกใช้ประเมินแล้ว; ให้สร้าง Version ใหม่เมื่อกระทบคะแนน |
| PM-025 | เปิดใช้งานเกณฑ์ | ⚠️ | ❌ | ต้องผ่าน Criteria Validation ก่อนเปิดรอบ |
| PM-026 | ดูเกณฑ์คะแนน | ✅ | ⚠️ | Evaluator เห็นชุดเกณฑ์ของรอบและ Evaluation ที่ตนกำลังประเมิน |
| PM-027 | เลือกผู้สมัครเพื่อเริ่มประเมิน | ❌ | ⚠️ | บัญชี Active, รอบ Open, ไม่เลือกซ้ำ, จำนวน Evaluation ที่ใช้งานอยู่ < 3 |
| PM-028 | ยกเลิกการเลือกก่อน Submit | 🔎 | ⚠️ | Evaluator ยกเลิกเฉพาะของตนตาม Policy; Admin ตรวจสอบได้และอาจดำเนินการเชิงบริหารตามสิทธิ์ที่อนุมัติ |
| PM-029 | เปิดแบบประเมินของตน | ❌ | ⚠️ | ต้องเป็นเจ้าของ Evaluation และรายการยังไม่ถูกยกเลิก |
| PM-030 | บันทึก Draft | ❌ | ⚠️ | เฉพาะของตนเอง และสถานะต้องเป็น `Draft` หรือ `Reopened/Draft` ตามโมเดลที่ใช้ |
| PM-031 | แก้ไขคะแนน/ความคิดเห็น Draft | ❌ | ⚠️ | เฉพาะของตนเอง; ตรวจช่วงคะแนนและกฎ Required Field |
| PM-032 | Review Before Submit | ❌ | ⚠️ | เฉพาะของตนเองและต้องผ่าน Validation |
| PM-033 | Submit ผลการประเมิน | ❌ | ⚠️ | เฉพาะของตนเอง, รอบ Open, สถานะ Draft, ข้อมูลครบถ้วน |
| PM-034 | ดูผล Draft ของผู้ประเมิน | 🔎 | ⚠️ | Admin ดูเพื่อติดตามได้; Evaluator ดูเฉพาะ Draft ของตนเอง |
| PM-035 | ดูผล Submitted ของตนเอง | 🔎 | ✅ | Evaluator ดูได้แต่แก้ไม่ได้จนกว่าจะได้รับ Reopen |
| PM-036 | ดูผลของผู้ประเมินคนอื่น | 🔎 | ❌ | Evaluator sees only own Evaluation, slot count, Submitted count and minimum-completion status; never peer identity, score, comment or amount recommendation. |
| PM-037 | แก้ไขผลของผู้ประเมินคนอื่น | ❌ | ❌ | ห้ามทุกบทบาทแก้แทนเจ้าของผล |
| PM-038 | Reopen ผล Submitted | ⚠️ | ⚠️ | Owner may request; staff may request on behalf with reason; Head/delegate approves; technical Admin cannot self-approve; owner alone edits/resubmits. |
| PM-039 | คำนวณคะแนนรวมรายผู้ประเมิน | ⚙️ ระบบ | ❌ | ระบบคำนวณจากผล Submitted ตามกฎคะแนน; ผู้ใช้ไม่แก้ค่าคำนวณโดยตรง |
| PM-040 | คำนวณ Result Summary | ⚙️ ระบบ | ❌ | ใช้เฉพาะ Submitted จากผู้ประเมินไม่ซ้ำกัน 2–3 คน |
| PM-041 | ดู Result Summary | ✅ | ⚠️ | Evaluator เห็นเฉพาะขอบเขตที่ได้รับอนุมัติ; ค่าเริ่มต้นแนะนำให้เห็นเฉพาะผลของตนและสถานะความครบถ้วน ไม่เห็นผลรายคนอื่น |
| PM-042 | ปิดรอบทุน | ⚠️ | ❌ | Admin เท่านั้น; ต้องแสดงผลกระทบต่อ Finalized/Closed Incomplete ก่อนยืนยัน |
| PM-043 | เปิดรอบทุนที่ปิดแล้ว | ⚠️ | ❌ | ต้องเป็นกระบวนการพิเศษ มีเหตุผล ผู้อนุมัติ และ Audit |
| PM-044 | Export Excel/CSV | ✅ | ❌ | บันทึกผู้ส่งออก เวลา รอบทุน และเงื่อนไขการกรอง |
| PM-045 | ดู Audit Log | ⚠️ | ❌ | Admin ตามหน้าที่; Audit Viewer แบบละเอียดอาจเป็นฟังก์ชันเสริม |
| PM-046 | ลบข้อมูลหรือทำลายผลประเมิน | ⚠️ | ❌ | ใช้ Soft Delete/Cancel ตามนโยบาย ห้ามลบผล Submitted โดยไม่มีขั้นตอนอนุมัติ |

> `⚙️ ระบบ` หมายถึงเป็นกระบวนการอัตโนมัติของ Backend ไม่ใช่สิทธิ์ที่ผู้ใช้กดแก้ไขค่าได้โดยตรง

---

## 4. Permission Matrix ระดับ API

> ชื่อ Endpoint ด้านล่างเป็นข้อเสนอสำหรับใช้ใน API Specification สามารถปรับชื่อ URI ให้ตรงกับมาตรฐานของโครงการได้ แต่กฎ Authorization ต้องคงเดิม

| รหัส | Method | API/Resource | Admin | Evaluator | Authorization Rule |
|---|---|---|---:|---:|---|
| API-001 | GET | `/auth/login` | ✅ | ✅ | Redirect ไป KKU SSO |
| API-002 | GET | `/auth/callback` | ✅ | ✅ | Verify state, nonce, PKCE/OIDC result และตรวจ SEMS User Active |
| API-003 | POST | `/auth/logout` | ✅ | ✅ | ยกเลิก SEMS Session |
| API-004 | GET | `/me` | ✅ | ✅ | คืนข้อมูลบัญชีของ Session ปัจจุบันเท่านั้น |
| API-005 | GET | `/users` | ✅ | ❌ | `role=ADMIN` |
| API-006 | POST | `/users` หรือ `/users/link-kku` | ✅ | ❌ | สร้าง/เชื่อม SEMS User กับ KKU Identity |
| API-007 | PATCH | `/users/:id/role` | ✅ | ❌ | ห้ามแก้รหัสผ่าน KKU; Audit ทุกครั้ง |
| API-008 | PATCH | `/users/:id/status` | ✅ | ❌ | เปิด/ปิดสิทธิ์ SEMS; ห้ามผู้ใช้ทั่วไปแก้เอง |
| API-009 | GET | `/rounds` | ✅ | ⚠️ | Evaluator ได้เฉพาะรอบที่อนุญาตและข้อมูลเท่าที่จำเป็น |
| API-010 | POST | `/rounds` | ✅ | ❌ | Admin เท่านั้น |
| API-011 | PATCH | `/rounds/:roundId` | ⚠️ | ❌ | ตรวจสถานะรอบและผลกระทบต่อข้อมูลที่มีอยู่ |
| API-012 | POST | `/rounds/:roundId/open` | ⚠️ | ❌ | เกณฑ์และข้อมูลที่จำเป็นต้องพร้อม |
| API-013 | POST | `/rounds/:roundId/close` | ⚠️ | ❌ | Finalize ผู้สมัครที่ Submitted ≥ 2 และกำหนด Closed Incomplete เมื่อ < 2 |
| API-014 | POST | `/rounds/:roundId/archive` | ⚠️ | ❌ | รอบต้อง Closed และผ่านเงื่อนไขการเก็บรักษา |
| API-015 | POST | `/rounds/:roundId/imports/preview` | ✅ | ❌ | Admin, ตรวจไฟล์และ Column Mapping |
| API-016 | POST | `/rounds/:roundId/imports/validate` | ✅ | ❌ | Admin, คืน Row Error และ Error Code |
| API-017 | POST | `/rounds/:roundId/imports/confirm` | ✅ | ❌ | Admin, ใช้ Transaction และ Audit |
| API-018 | GET | `/rounds/:roundId/imports` | ✅ | ❌ | Admin เท่านั้น |
| API-019 | GET | `/rounds/:roundId/applicants` | ✅ | ⚠️ | Evaluator: `round.status=OPEN`, คืนเฉพาะ Search/List Fields |
| API-020 | GET | `/applicants/:applicantId` | ✅ | ⚠️ | Evaluator ต้องมี Active Evaluation ของตนสำหรับผู้สมัครรายนี้ |
| API-021 | PATCH | `/applicants/:applicantId` | ⚠️ | ❌ | Admin, ตรวจ Round Status และผลกระทบ |
| API-022 | POST | `/applicants/:applicantId/documents` | ✅ | ❌ | Admin, Validate type/size |
| API-023 | GET | `/documents/:documentId/content` | ✅ | ⚠️ | Evaluator ต้องเป็นเจ้าของ Active Evaluation ที่เชื่อมกับผู้สมัครเจ้าของเอกสาร |
| API-024 | DELETE | `/documents/:documentId` | ⚠️ | ❌ | Admin, ใช้ Soft Delete และ Audit ตาม Policy |
| API-025 | GET | `/rounds/:roundId/criteria` | ✅ | ⚠️ | Evaluator ได้เฉพาะ Criteria Version ที่ Evaluation ของตนอ้างอิง |
| API-026 | POST | `/rounds/:roundId/criteria` | ✅ | ❌ | Admin เท่านั้น |
| API-027 | PATCH | `/criteria/:criteriaId` | ⚠️ | ❌ | ห้ามแก้ Version ที่ถูกใช้แล้ว |
| API-028 | POST | `/criteria/:criteriaId/activate` | ⚠️ | ❌ | Admin, ผ่าน Validation ก่อน Activate |
| API-029 | POST | `/rounds/:roundId/applicants/:applicantId/evaluations` | ❌ | ⚠️ | Active Account + Open Round + no duplicate + active count < 3; ใช้ Transaction/Lock |
| API-030 | GET | `/evaluations/my` | ❌ | ✅ | กรองด้วย `evaluator_id = current_user.id` เท่านั้น |
| API-031 | GET | `/evaluations/:evaluationId` | 🔎 | ⚠️ | Admin ดูได้; Evaluator ต้องเป็นเจ้าของรายการ |
| API-032 | PATCH | `/evaluations/:evaluationId/draft` | ❌ | ⚠️ | Owner เท่านั้น และสถานะ Draft/Reopened ที่แก้ไขได้ |
| API-033 | POST | `/evaluations/:evaluationId/review` | ❌ | ⚠️ | Owner เท่านั้น; Validation แบบไม่เปลี่ยนสถานะสุดท้าย |
| API-034 | POST | `/evaluations/:evaluationId/submit` | ❌ | ⚠️ | Owner + Open Round + Draft + Valid; เปลี่ยนเป็น Submitted แบบ Atomic |
| API-035 | POST | `/evaluations/:evaluationId/cancel` | ⚠️ | ⚠️ | ก่อน Submit ตาม Policy; หลัง Submit ต้องใช้ Reopen/Cancel Workflow และ Audit |
| API-036 | POST | `/evaluations/:evaluationId/reopen-requests` | ⚠️ | ⚠️ | Owner or staff-on-behalf; reason/reference; object ownership enforced |
| API-036A | POST | `/evaluation-reopen-requests/:requestId/decision` | ⚠️ | ❌ | Head/delegate only; separation of duties |
| API-036B | POST | `/evaluations/:evaluationId/resubmit` | ❌ | ⚠️ | Owner only; approved reopen Draft; recalculates after commit |
| API-036C | POST | `/applications/:applicationId/controlled-corrections` | ✅ | ❌ | Admin with application access; identity triplet immutable; before/after audit |
| API-036D | POST | `/scholarship-rounds/:roundId/reopen-requests` | ⚠️ | ❌ | Head/System Owner; Closed only; Archived denied |
| API-036E | GET | `/scholarship-rounds/:roundId/report-snapshots` | ✅ | ❌ | Round-scoped Admin; immutable Final/Superseded snapshots |
| API-036F | GET | `/documents/:documentId/scan-status` | ✅ | ⚠️ | Evaluator needs active owned Evaluation for the application; no file bytes |
| API-037 | GET | `/admin/evaluations` | ✅ | ❌ | Admin ดูรายการทุกผู้ประเมินตามหน้าที่ |
| API-038 | GET | `/admin/evaluations/:evaluationId` | ✅ | ❌ | Read-only ต่อคะแนนและความคิดเห็น |
| API-039 | PATCH | `/admin/evaluations/:evaluationId/scores` | ❌ | ❌ | ห้ามแก้คะแนนแทนเจ้าของผล |
| API-040 | POST | `/admin/evaluations/:evaluationId/submit` | ❌ | ❌ | ห้าม Submit แทนเจ้าของผล |
| API-041 | GET | `/rounds/:roundId/results` | ✅ | ⚠️ | Evaluator ต้องไม่เห็นผลรายบุคคลของผู้อื่น; ใช้ Response DTO แยกบทบาท |
| API-042 | GET | `/applicants/:applicantId/result-summary` | ✅ | ⚠️ | Evaluator ได้เฉพาะข้อมูลที่ Policy อนุญาต ไม่คืนคะแนน/ความคิดเห็นของผู้ประเมินอื่น |
| API-043 | POST | `/rounds/:roundId/results/recalculate` | ⚠️ | ❌ | Admin ใช้สำหรับ Recovery/Support; ปกติระบบคำนวณอัตโนมัติ |
| API-044 | GET | `/rounds/:roundId/dashboard` | ✅ | ❌ | Admin Dashboard |
| API-045 | GET | `/rounds/:roundId/exports.xlsx` | ✅ | ❌ | Admin, Audit Export |
| API-046 | GET | `/rounds/:roundId/exports.csv` | ✅ | ❌ | Admin, Audit Export |
| API-047 | GET | `/audit-logs` | ⚠️ | ❌ | Admin ตามขอบเขตหน้าที่และนโยบายข้อมูล |

---

## 5. Data Scope และ Field-level Permission

| ข้อมูล | Admin | Evaluator ก่อนเลือกผู้สมัคร | Evaluator หลังเลือกผู้สมัคร |
|---|---:|---:|---:|
| รหัสนักศึกษา ชื่อ นามสกุล | ✅ | ✅ | ✅ |
| สถานะจำนวนผู้ประเมิน เช่น 0/3–3/3 | ✅ | ⚠️ แสดงเท่าที่จำเป็นต่อการเลือก | ✅ |
| ข้อมูลติดต่อ | ✅ | ❌ | ⚠️ เฉพาะที่จำเป็นต่อการประเมิน |
| GPA และข้อมูลการศึกษา | ✅ | ❌ | ✅ |
| รายได้ ค่าใช้จ่าย และข้อมูลครอบครัว | ✅ | ❌ | ✅ |
| ประวัติ กยศ. และทุนย้อนหลัง | ✅ | ❌ | ✅ |
| เอกสารประกอบ | ✅ | ❌ | ✅ ผ่าน Backend Authorization |
| Draft ของผู้ประเมินคนอื่น | 🔎 | ❌ | ❌ |
| Submitted ของผู้ประเมินคนอื่น | 🔎 | ❌ | ❌ |
| ความคิดเห็นของผู้ประเมินคนอื่น | 🔎 | ❌ | ❌ |
| Result Summary | ✅ | ❌ | ⚠️ ตาม Policy; ไม่ควรเผยผลรายผู้ประเมินอื่น |
| Audit Log | ⚠️ | ❌ | ❌ |

### ข้อเสนอด้านความเป็นส่วนตัว

- API รายชื่อผู้สมัครสำหรับ Evaluator ควรใช้ `ApplicantSearchDTO` ซึ่งไม่มีข้อมูลละเอียดอ่อน
- API รายละเอียดผู้สมัครควรตรวจ Ownership ก่อน Query หรือก่อน Serialize Response
- Result API ควรแยก DTO ระหว่าง Admin และ Evaluator เพื่อป้องกันข้อมูลผู้ประเมินคนอื่นรั่วไหล
- Document API ควรคืนไฟล์ผ่าน Stream หรือ Signed URL อายุสั้นหลังตรวจสิทธิ์แล้ว

---

## 6. เงื่อนไข Authorization สำหรับ Evaluation

ระบบต้องอนุญาตการสร้าง Evaluation เมื่อทุกเงื่อนไขต่อไปนี้เป็นจริง

```text
currentUser.role == EVALUATOR
AND currentUser.status == ACTIVE
AND round.status == OPEN
AND noActiveEvaluation(currentUser, applicant, round)
AND activeEvaluationCount(applicant, round) < 3
```

ระบบต้องอนุญาตการแก้ไข Draft เมื่อทุกเงื่อนไขต่อไปนี้เป็นจริง

```text
currentUser.role == EVALUATOR
AND evaluation.evaluatorId == currentUser.id
AND evaluation.status IN (DRAFT, REOPENED)
AND evaluation.isCancelled == false
AND round.status permits editing
```

ระบบต้องอนุญาต Submit เมื่อทุกเงื่อนไขต่อไปนี้เป็นจริง

```text
currentUser.role == EVALUATOR
AND evaluation.evaluatorId == currentUser.id
AND evaluation.status == DRAFT
AND round.status == OPEN
AND evaluation passes validation
AND currentUser.status == ACTIVE
```

> ควรตรวจเงื่อนไขสร้าง Evaluation ภายใน Database Transaction เพื่อป้องกันกรณีผู้ประเมินหลายคนเลือกผู้สมัครพร้อมกันจนเกิน 3 คน

---

## 7. การตอบกลับเมื่อไม่ผ่านสิทธิ์

| กรณี | HTTP Status | Error Code ที่แนะนำ |
|---|---:|---|
| ไม่มี Session หรือ Session หมดอายุ | 401 | `AUTHENTICATION_REQUIRED` |
| บัญชี SEMS ไม่ Active | 403 | `USER_INACTIVE` |
| บทบาทไม่อนุญาต | 403 | `ROLE_FORBIDDEN` |
| ไม่ใช่เจ้าของ Evaluation | 403 | `EVALUATION_NOT_OWNER` |
| พยายามเปิดเอกสารผู้สมัครที่ไม่ได้เลือก | 403 หรือ 404 | `DOCUMENT_ACCESS_DENIED` |
| รอบทุนไม่ Open | 409 | `ROUND_NOT_OPEN` |
| ผู้ประเมินเลือกผู้สมัครซ้ำ | 409 | `DUPLICATE_EVALUATION` |
| ผู้สมัครมีผู้ประเมินครบ 3 คนแล้ว | 409 | `EVALUATOR_LIMIT_REACHED` |
| Evaluation ไม่อยู่ในสถานะที่แก้ไขได้ | 409 | `INVALID_EVALUATION_STATE` |
| ข้อมูลก่อน Submit ไม่ครบ | 422 | `EVALUATION_VALIDATION_FAILED` |
| Admin พยายาม Submit แทน | 403 | `SUBMIT_ON_BEHALF_FORBIDDEN` |

> สำหรับข้อมูลละเอียดอ่อน อาจตอบ `404 Not Found` แทน `403 Forbidden` เพื่อไม่เปิดเผยว่าทรัพยากรนั้นมีอยู่จริง ทั้งนี้ต้องใช้แนวทางเดียวกันอย่างสม่ำเสมอ

---

## 8. Audit Events ที่ควรบันทึก

| Event Code | เหตุการณ์ | ผู้กระทำ |
|---|---|---|
| `LOGIN_SUCCESS` | Login สำเร็จ | Admin/Evaluator |
| `LOGIN_FAILURE` | Login หรือ Account Authorization ไม่สำเร็จ | ระบบ |
| `ACCESS_DENIED` | พยายามเข้าหน้า/API/เอกสารนอกสิทธิ์ | Admin/Evaluator |
| `USER_ROLE_CHANGED` | เปลี่ยนบทบาท | Admin |
| `USER_STATUS_CHANGED` | เปิด/ปิดบัญชี SEMS | Admin |
| `ROUND_STATUS_CHANGED` | เปลี่ยนสถานะรอบทุน | Admin |
| `APPLICANT_IMPORTED` | ยืนยัน Import | Admin |
| `DOCUMENT_UPLOADED` | อัปโหลดเอกสาร | Admin |
| `EVALUATION_CREATED` | เลือกผู้สมัครและสร้าง Evaluation | Evaluator |
| `EVALUATION_DRAFT_SAVED` | บันทึก Draft | Evaluator |
| `EVALUATION_SUBMITTED` | Submit ผล | Evaluator |
| `EVALUATION_REOPENED` | เปิดผลให้แก้ไข | Admin |
| `EVALUATION_CANCELLED` | ยกเลิกรายการตาม Policy | Admin/Evaluator |
| `ROUND_CLOSED` | ปิดรอบทุน | Admin |
| `REPORT_EXPORTED` | Export Excel/CSV | Admin |

Audit Log ต้องไม่บันทึกรหัสผ่าน, Access Token, Refresh Token, Client Secret หรือข้อมูลลับอื่น

---

## 9. Guard/Policy ที่แนะนำสำหรับ NestJS

| Guard/Policy | หน้าที่ |
|---|---|
| `SessionAuthGuard` | ตรวจ Session และผู้ใช้จาก KKU SSO |
| `ActiveUserGuard` | ตรวจ SEMS User สถานะ Active |
| `RolesGuard` | ตรวจ `ADMIN` หรือ `EVALUATOR` |
| `RoundStatusGuard` | ตรวจสถานะรอบทุนตาม Action |
| `EvaluationOwnershipGuard` | ตรวจว่า Evaluator เป็นเจ้าของ Evaluation |
| `ApplicantAccessPolicy` | ตรวจสิทธิ์รายละเอียดผู้สมัครตาม Active Evaluation |
| `DocumentAccessPolicy` | ตรวจผู้สมัครเจ้าของเอกสารและสิทธิ์ผู้เรียก |
| `EvaluationStateGuard` | ตรวจ Draft/Submitted/Reopened ก่อนแก้ไขหรือ Submit |
| `MaxEvaluatorPolicy` | ป้องกันเกิน 3 คนและผู้ประเมินซ้ำ |
| `AdminReadOnlyEvaluationPolicy` | ให้ Admin ตรวจผลได้ แต่ห้ามแก้คะแนน/Submit แทน |

ลำดับการตรวจโดยทั่วไป

```text
Authentication
→ Active Account
→ Role
→ Resource Scope/Round
→ Ownership
→ Resource State
→ Business Validation
→ Execute Transaction
→ Audit
```

---

## 10. Acceptance Criteria ด้านสิทธิ์

1. Evaluator ที่ไม่มี Evaluation ต้องเปิดรายละเอียดหรือเอกสารละเอียดอ่อนของผู้สมัครไม่ได้
2. Evaluator สามารถค้นหาและเลือกผู้สมัครในรอบ Open ได้จากข้อมูลขั้นต่ำที่กำหนด
3. Evaluator คนเดิมเลือกผู้สมัครคนเดิมซ้ำในรอบเดียวกันไม่ได้
4. Evaluator คนที่ 4 สร้าง Evaluation ไม่ได้ แม้ส่ง Request ตรงไปยัง API
5. Evaluator แก้ไข Draft ของผู้ประเมินคนอื่นไม่ได้
6. Evaluator Submit ผลของผู้ประเมินคนอื่นไม่ได้
7. Evaluator ดูคะแนนและความคิดเห็นของผู้ประเมินคนอื่นไม่ได้
8. Admin ตรวจดู Draft/Submitted ได้ แต่แก้คะแนนหรือ Submit แทนไม่ได้
9. เมื่อรอบทุน Closed ผู้ประเมินสร้าง Evaluation ใหม่หรือ Submit เพิ่มไม่ได้
10. การ Reopen ต้องดำเนินการโดย Admin มีเหตุผล และมี Audit Log
11. หลัง Reopen ผู้ประเมินเจ้าของผลเท่านั้นที่แก้และ Submit ใหม่ได้
12. Evaluator เรียก Export API ไม่ได้
13. การเข้าถึงเอกสารทุกครั้งต้องผ่าน Backend Authorization
14. การซ่อนเมนูบน Frontend เพียงอย่างเดียวไม่ถือว่าผ่านการทดสอบ ต้องทดสอบ API โดยตรงด้วย
15. การปฏิเสธสิทธิ์ต้องคืน HTTP Status และ Error Code ที่สอดคล้องกัน

---

## 11. ประเด็นที่ต้องยืนยันกับเจ้าของระบบ

| Decision ID | ประเด็น | ข้อเสนอเริ่มต้น |
|---|---|---|
| PERM-DEC-001 | Evaluator เห็นคะแนนสรุปของผู้สมัครหรือไม่ | เห็นเฉพาะสถานะความครบถ้วนและผลของตน ไม่เห็นคะแนน/ความคิดเห็นของผู้อื่น |
| PERM-DEC-002 | Admin ยกเลิก Draft ของผู้ประเมินได้หรือไม่ | อนุญาตเฉพาะกรณีบริหารระบบ มีเหตุผล และ Audit; ห้ามแก้เนื้อหา |
| PERM-DEC-003 | Admin เปิดรอบ Closed กลับเป็น Open ได้หรือไม่ | **Confirmed Response:** exceptional request/approval only; Archived denied; prior Final snapshot becomes Superseded |
| PERM-DEC-004 | Reopen เปลี่ยนสถานะเป็น `Reopened` หรือกลับ `Draft` ทันที | แนะนำให้มี `Reopened` ใน Audit/Workflow แล้วเปลี่ยนเป็น Draft ที่แก้ไขได้ |
| PERM-DEC-005 | ผู้ประเมินดูรายการของตนหลัง Archived ได้หรือไม่ | แนะนำให้ดูแบบ Read-only ได้ตามระยะเวลาเก็บข้อมูล |
| PERM-DEC-006 | Access Denied ต่อข้อมูลละเอียดอ่อนใช้ 403 หรือ 404 | แนะนำ 404 สำหรับทรัพยากรที่ไม่ควรเปิดเผยการมีอยู่ และใช้มาตรฐานเดียวกันทั้งระบบ |

---

## 12. สรุปสิทธิ์หลัก

- **Admin:** บริหารผู้ใช้ รอบทุน Import ผู้สมัคร เอกสาร เกณฑ์ ติดตามผล ดูผลรายผู้ประเมิน ปิดรอบ Export และตรวจ Audit ตามหน้าที่ แต่ **ห้ามแก้คะแนนหรือ Submit แทนผู้ประเมิน**
- **Evaluator:** ค้นหาและเลือกผู้สมัครในรอบ Open ดูรายละเอียดเฉพาะผู้สมัครที่เลือก บันทึก Draft Review และ Submit **เฉพาะ Evaluation ของตนเอง** และ **ห้ามดูหรือแก้ผลของผู้ประเมินคนอื่น**
- **Backend:** ต้องบังคับใช้ Role + Active Status + Round Status + Ownership + Evaluation Status ทุกครั้ง ไม่พึ่งการซ่อนเมนูจาก Frontend

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Design Team | Confirmed evaluator isolation, reopen separation of duties, correction/round/report/scan endpoint permissions. |
| v1.2 | 2026-07-24 | SEMS Design Team | Replaced the inactive-account alias with canonical `USER_INACTIVE`; audit-event names remain unchanged. |
| v1.1 | 2026-07-23 | SEMS Design Team | Aligned canonical evaluation error codes and made controlled reopen explicitly provisional. |
| v1.0 | 2026-07-23 | SEMS Design Team | Initial permission matrix draft. |
