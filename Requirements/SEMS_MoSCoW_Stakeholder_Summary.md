# สรุปการจัดกลุ่มความสามารถของระบบด้วย MoSCoW สำหรับผู้พิจารณา — SEMS

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-MOSCOW-STAKEHOLDER-001` |
| Version | **v0.2** |
| Last Updated | **2026-08-05** |
| Status | **Draft — Pending Review** |
| Author | **SEMS Requirements Team** |
| Audience | อาจารย์ ผู้พิจารณา และผู้มีส่วนได้ส่วนเสีย |
| Source Document | [การจัดลำดับความสำคัญของความสามารถด้วยวิธี MoSCoW — SEMS](./SEMS_MoSCoW_Feature_Prioritization.md) |

[START HERE](../START_HERE.md) › [📋 Requirements](./README.md) › สรุปการจัดกลุ่มความสามารถของระบบด้วย MoSCoW สำหรับผู้พิจารณา — SEMS

## 1. วัตถุประสงค์

ใช้เป็นเอกสารหลักสำหรับนำเสนอขอบเขต Release 1 และประเด็นที่ต้องตัดสินใจ โดยสรุปจากเอกสารต้นทางและไม่เปลี่ยน Business Rule, Requirement ID หรือกลุ่ม MoSCoW เดิม

## 2. ขอบเขตและข้อจำกัดของเอกสาร

- เอกสารนี้เป็นสรุปเพื่อการพิจารณา ไม่แทน PRD, SRS, User Stories หรือเอกสาร MoSCoW ฉบับละเอียด
- Requirement Baseline และ System Design ยังเป็น **Pending Formal Approval**
- Test Case ถูกกำหนดแล้ว แต่ยังไม่ถือว่า Test Executed; UAT ยังไม่มีรายชื่อผู้เข้าร่วม วันที่ และผลจริง
- Traceability ระดับ Core Flow มีแล้ว แต่ Screen ID และ UAT ID ระดับแถวยังไม่ครบทั้งหมด
- KKU Client Configuration, Infrastructure, Malware Scanner และ Report Template ยังต้องได้รับการยืนยัน
- Public Repository ต้องใช้ข้อมูลสังเคราะห์และไม่มี PII
- สถานะนี้ไม่หมายความว่าระบบพร้อม Production

## 3. ระบบ SEMS ทำอะไร

SEMS รองรับการเตรียมรอบทุน นำเข้าข้อมูลผู้สมัครและเอกสาร กำหนดเกณฑ์ ให้ผู้ประเมินเลือกผู้สมัคร บันทึก `DRAFT` ตรวจทานและส่งผล `SUBMITTED` จากนั้นระบบรวมผลของผู้ประเมินไม่ซ้ำกัน 2–3 คน ติดตามความครบถ้วน ปิดรอบ และส่งออกรายงานตามสิทธิ์

## 4. ผู้ใช้งานและบทบาท

### 4.1 ผู้ดูแลระบบ — `ADMIN`

| ความสามารถ | อ้างอิงเดิม |
| :--- | :--- |
| จัดการบัญชีและบทบาท | `FR-AUT-007..010`, `US-USR-001..003` |
| สร้างและเตรียมรอบทุน | `FR-RND-001..005`, `US-RND-001..002` |
| นำเข้าข้อมูลผู้สมัครจาก XLSX/CSV รวม Preview และ Validation ก่อน Import | `FR-IMP-001..015`, `US-IMP-001..003` |
| จัดการข้อมูลและเอกสารผู้สมัคร | `FR-APP-001..009`, `FR-DOC-001..006`, `US-APP-004`, `US-DOC-001..002` |
| จัดการ Criteria และ Criteria Version | `FR-CRI-001..012`, `US-CRI-001..003` |
| ติดตามสถานะผ่าน Dashboard | `FR-DSH-001..003`, `US-DSH-001..002` |
| ตรวจความครบถ้วนและปิดรอบ | `FR-RND-006..008`, `FR-SCO-009..012`, `US-CLS-001..002` |
| ส่งออกรายงาน | `FR-RPT-001..010`, `US-RPT-001..003` |
| ตรวจ Audit Trail ตามสิทธิ์ | `FR-AUD-001..004`, Cross-cutting AC |

### 4.2 ผู้ประเมิน — `EVALUATOR`

| ความสามารถ | อ้างอิงเดิม |
| :--- | :--- |
| Login ผ่าน KKU OAuth/OIDC | `FR-AUT-001..005`, `US-AUTH-001` |
| ค้นหาและเลือกผู้สมัคร | `FR-EVA-001..003`, `US-SEL-001..002` |
| ดูข้อมูลและเอกสารตามสิทธิ์ | `FR-EVA-004`, `FR-DOC-004..005`, `US-DRF-001` |
| กรอกคะแนนและความคิดเห็น | `FR-EVA-005..008`, `US-DRF-002..003` |
| Save Draft | `FR-EVA-006..008`, `US-DRF-002..003` |
| Review | `FR-EVA-009..011`, `US-SUB-001` |
| Submit | `FR-EVA-012..013`, `US-SUB-002` |
| ดูสถานะงานของตน | `FR-DSH-002`, `US-DSH-002` |

### 4.3 ระบบทำงานอัตโนมัติ

| ความสามารถ | อ้างอิงเดิม |
| :--- | :--- |
| ป้องกันผู้ประเมินซ้ำและจำกัดไม่เกิน 3 คนต่อผู้สมัคร | `FR-EVA-001..003`, `TRC-008` |
| ใช้เฉพาะ `SUBMITTED` และคำนวณเมื่อครบผู้ประเมินขั้นต่ำ 2 คน | `FR-SCO-001..006`, `TRC-012` |
| คำนวณใหม่เมื่อผู้ประเมินคนที่ 3 Submit | `FR-SCO-003`, `FR-SCO-006..008`, `TRC-013` |
| แยกข้อมูลตามรอบทุน | SRS §2.1, `FR-RND-001..011` |
| ตรวจ Authorization ที่ Backend | SRS §1.5, `NFR-SEC-001..010` |
| บันทึก Audit | `FR-AUD-001..004`, `TRC-017` |
| ป้องกันการแก้ Final Report โดยตรง | `FR-RPT-004..010`, `RD-049`, `TRC-016` |
| จำกัดข้อมูลส่วนบุคคลใน Export และ Error | `FR-RPT-001..010`, `NFR-SEC-001..010`, `RD-022` |

## 5. วิธีอ่าน MoSCoW

| กลุ่ม | ความหมาย |
| :--- | :--- |
| **Must have** | จำเป็นต่อ Core Flow หรือความปลอดภัยของ Release 1 |
| **Should have** | สำคัญ แต่ยังต้องตัดสินว่าจะอยู่ Release 1 หรือ Release ถัดไป |
| **Could have** | เพิ่มความสะดวกและวางไว้สำหรับ Future Release |
| **Won't have** | ไม่อยู่ในขอบเขต Release 1 |

## 6. สรุปความสามารถตาม MoSCoW

ตารางนี้คงการรวมกลุ่มจาก [เอกสาร MoSCoW ฉบับละเอียด](./SEMS_MoSCoW_Feature_Prioritization.md#5-ตารางความสามารถของระบบตาม-moscow) โดยไม่ได้ย้าย Function ระหว่างกลุ่ม

| ลำดับ | ความสามารถ | ผู้ใช้งานหลัก | Priority | Release | สถานะการยืนยัน | เอกสารอ้างอิง |
| ----: | ---------- | ------------- | -------- | ------- | -------------- | ------------- |
| 1 | เข้าสู่ระบบ ออกจากระบบ และจำกัดสิทธิ์ผู้ใช้ | ADMIN, EVALUATOR | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-AUT-001..006` |
| 2 | จัดการบัญชีและบทบาทผู้ใช้งาน | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-AUT-007..010` |
| 3 | สร้าง เตรียม และเปิดรอบทุน | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-RND-001..005` |
| 4 | นำเข้าและตรวจสอบข้อมูลผู้สมัคร | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-IMP-001..015` |
| 5 | จัดการข้อมูลและเอกสารผู้สมัคร | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-APP-001..009`, `FR-DOC-001..006` |
| 6 | กำหนด ตรวจสอบ และเปิดใช้เกณฑ์การประเมิน | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-CRI-001..012` |
| 7 | ค้นหาและเลือกผู้สมัครเพื่อสร้างแบบประเมิน | EVALUATOR | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-EVA-001..003` |
| 8 | กรอก บันทึก ตรวจทาน และส่งผลประเมิน | EVALUATOR | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-EVA-004..013` |
| 9 | คำนวณและสรุปคะแนนจากผู้ประเมิน | ระบบอัตโนมัติ | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-SCO-001..008` |
| 10 | ตรวจความครบถ้วนและปิดรอบ | ADMIN, ระบบอัตโนมัติ | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-RND-006..008`, `FR-SCO-009..012` |
| 11 | ติดตามสถานะและส่งออกรายงานตามสิทธิ์ | ADMIN | Must have | Release 1 | Confirmed for Baseline Candidate | `FR-DSH-001..003`, `FR-RPT-001..010` |
| 12 | เก็บรอบที่เสร็จแล้วและเปิดรอบที่ปิดในกรณีพิเศษ | ADMIN | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2, `FR-RND-008` |
| 13 | แก้ไขข้อมูลและรายการมาตรฐานอย่างควบคุม | ADMIN | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2, `FR-APP-005` |
| 14 | ยกเลิกแบบประเมินฉบับร่าง | EVALUATOR | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2, `FR-EVA-014` |
| 15 | เปิดผลประเมินที่ส่งแล้วให้แก้ไข | EVALUATOR, ผู้อนุมัติ | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2, `FR-EVA-015` |
| 16 | ดูรายละเอียดจาก Dashboard และใช้รายงานหลายระดับ | ADMIN | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2 |
| 17 | ดูและค้นหาประวัติการดำเนินงาน | ADMIN | Should have | Release 1 / Release ถัดไป — Pending Decision | Pending Release Decision | MoSCoW §5.2, `FR-AUD-001..004` |
| 18 | เครื่องมือช่วยลดขั้นตอนซ้ำในการใช้งาน | ADMIN, EVALUATOR | Could have | Future Release | Pending Stakeholder Review | MoSCoW §5.3 |
| 19 | เครื่องมือช่วยค้นหาและจดบันทึกสำหรับผู้ดูแลระบบ | ADMIN | Could have | Future Release | Pending Stakeholder Review | MoSCoW §5.3 |
| 20 | รูปแบบและการจัดชุดไฟล์รายงานเพิ่มเติม | ADMIN | Could have | Future Release | Pending Stakeholder Review | MoSCoW §5.3 |
| 21 | เครื่องมือเสริมสำหรับติดตามงานและตรวจสอบรายละเอียด | ADMIN | Could have | Future Release | Pending Stakeholder Review | MoSCoW §5.3 |
| 22 | บริการสมัครทุนและประกาศผลสำหรับนักศึกษาโดยตรง | นักศึกษา | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4 |
| 23 | การอนุมัติทุนขั้นสุดท้ายและการจ่ายเงิน | ผู้มีอำนาจเชิงนโยบาย | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4 |
| 24 | เชื่อมแทนระบบข้อมูลกลางหรือใช้ National ID | — | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4, `RD-016`, `RD-029` |
| 25 | จัดการรหัสผ่านบัญชีมหาวิทยาลัย | — | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4 |
| 26 | Native Mobile Application | — | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4 |
| 27 | มอบหมายล่วงหน้า นัดสัมภาษณ์ หรือไฟล์ Excel รุ่นเก่า | — | Won't have | Out of Scope — Release 1 | Out of Scope | MoSCoW §5.4 |

### 6.1 Must have

รายการ 1–11 เป็น Core Flow ของ Release 1 และยังมีสถานะ Baseline Candidate จนกว่าจะมีหลักฐานอนุมัติจริง

### 6.2 Should have

รายการ 12–17 คงกลุ่ม Should have เดิมและรอการตัดสิน Release

### 6.3 Could have

รายการ 18–21 คงกลุ่ม Could have เดิมสำหรับ Future Release

### 6.4 Won't have

รายการ 22–27 คงกลุ่ม Won't have เดิมและไม่อยู่ใน Release 1

### 6.5 สิ่งที่ไม่อยู่ในขอบเขต Release 1

- ระบบสมัครทุนออนไลน์และบัญชีผู้ใช้งานสำหรับนักศึกษา
- การอนุมัติทุนขั้นสุดท้ายเชิงนโยบาย การประกาศผลโดยตรงแก่นักศึกษา และการจ่ายเงินทุน
- Native Mobile Application และการแทนระบบทะเบียนกลาง
- การจัดคิวสัมภาษณ์หรือห้องประชุมออนไลน์
- การเก็บ National ID ใน Release 1 Core Flow
- การเชื่อมต่อระบบภายนอกที่ยังไม่มีการยืนยันอย่างเป็นทางการ

## 7. Core Workflow สำหรับ Release 1

1. `ADMIN` เตรียมบัญชี รอบทุน ข้อมูลผู้สมัคร เอกสาร และ Criteria Version
2. ระบบตรวจความพร้อมก่อนเปิดรอบ
3. `EVALUATOR` Login ค้นหาและเลือกผู้สมัคร โดยระบบป้องกันผู้ประเมินซ้ำและจำกัด 3 คน
4. `EVALUATOR` กรอกคะแนน Save Draft, Review และ Submit
5. ระบบใช้เฉพาะ `SUBMITTED` จากผู้ประเมินไม่ซ้ำกัน 2–3 คน และคำนวณใหม่เมื่อคนที่ 3 Submit
6. `ADMIN` ตรวจความครบถ้วน ปิดรอบ ติดตามผล และส่งออกรายงานตามสิทธิ์

## 8. สิ่งที่ต้องการให้อาจารย์ยืนยัน

| ลำดับ | คำถาม | สถานะ |
| ----: | :--- | :--- |
| 1 | ยืนยันหรือไม่ว่าผู้ใช้งาน Release 1 มีเพียง `ADMIN` และ `EVALUATOR` | Pending Formal Review |
| 2 | ยืนยันหรือไม่ว่านักศึกษาผู้สมัครไม่มีบัญชีเข้าใช้ SEMS | Pending Formal Review |
| 3 | ยืนยันหรือไม่ว่าผู้ประเมินเลือกผู้สมัครด้วยตนเอง | Pending Formal Review |
| 4 | ยืนยันหรือไม่ว่าผู้สมัครหนึ่งรายมีผู้ประเมินไม่ซ้ำกัน 2–3 คน | Pending Formal Review |
| 5 | ยืนยันหรือไม่ว่าใช้เฉพาะผล `SUBMITTED` ในการคำนวณ | Pending Formal Review |
| 6 | ยืนยันหรือไม่ว่าเมื่อผู้ประเมินคนที่ 3 Submit ระบบต้องคำนวณผลใหม่ | Pending Formal Review |
| 7 | `Cancel Draft` ต้องอยู่ใน Release 1 หรือ Release ถัดไป | Pending Formal Review |
| 8 | `Reopen Submitted Evaluation` ต้องอยู่ใน Release 1 หรือ Release ถัดไป | Pending Formal Review |
| 9 | `Controlled Round Reopen` ต้องอยู่ใน Release 1 หรือ Release ถัดไป | Pending Formal Review |
| 10 | `Controlled Correction` ต้องอยู่ใน Release 1 หรือ Release ถัดไป | Pending Formal Review |
| 11 | Dashboard แบบ Drill-down จำเป็นสำหรับ Release 1 หรือไม่ | Pending Formal Review |
| 12 | รูปแบบรายงานและข้อมูลที่แต่ละบทบาทสามารถเห็นต้องเป็นอย่างไร | Pending Formal Review |
| 13 | ยืนยันหรือไม่ว่าไม่ใช้ National ID ใน Release 1 Core Flow | Pending Formal Review |
| 14 | ใครเป็นผู้มีอำนาจอนุมัติ Requirement Baseline | Pending Formal Review |
| 15 | ต้องใช้หลักฐานรูปแบบใดในการบันทึกการอนุมัติ | Pending Formal Review |

## 9. ผลกระทบหากมีการเปลี่ยนขอบเขต

การย้ายรายการระหว่าง MoSCoW หรือ Release อาจกระทบ PRD, SRS, User Stories, API, Database, UI, Test Case, Traceability และแผนส่งมอบ จึงต้องมี Decision Record และอัปเดตเอกสารที่เชื่อมโยงก่อนเปลี่ยน Baseline Candidate

## 10. เอกสารอ้างอิง

1. [เอกสาร MoSCoW ฉบับละเอียด](./SEMS_MoSCoW_Feature_Prioritization.md) — แหล่งข้อมูลหลักของการจัดกลุ่ม
2. [PRD](./PRD/SEMS-PRD.md)
3. [SRS](./SRS/SEMS-SRS.md)
4. [User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
5. [Requirement Decision Register](./SEMS_Requirement_Decision_Register.md)
6. [Traceability Matrix](./SEMS_Traceability_Matrix.md)
7. [ข้อเสนอโครงการ SEMS](./Proposal/SEMS-project-proposal.md)

## 11. Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.2 | 2026-08-05 | SEMS Requirements Team | จัดลำดับหัวข้อ เพิ่มตารางสรุปสำหรับนำเสนอ แบ่ง Function ตามบทบาท ระบุ Core Workflow, Out of Scope, ช่องว่าง และคำถาม Pending Formal Review โดยคงกลุ่ม MoSCoW และ Business Rule เดิม |
| v0.1 | 2026-07-30 | SEMS Requirements Team | สร้างเอกสารสรุป MoSCoW สำหรับอาจารย์และผู้มีส่วนได้ส่วนเสีย โดยรวมความสามารถเป็นระดับภาพรวมและรักษาการจัดกลุ่มจากเอกสารฉบับละเอียด |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)<br>
↑ หมวดเอกสาร: [📋 Requirements](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../START_HERE.md)<br>
→ อ่านต่อ: [เอกสาร MoSCoW ฉบับละเอียด](./SEMS_MoSCoW_Feature_Prioritization.md)<br>
→ ตรวจสอบการเชื่อมโยง: [SEMS Traceability Matrix](./SEMS_Traceability_Matrix.md)

<!-- DOC_NAV_END -->
