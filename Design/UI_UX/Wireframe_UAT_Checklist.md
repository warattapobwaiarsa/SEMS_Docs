# SEMS Formative Prototype Evaluation Checklist

| Metadata | Value |
| :--- | :--- |
| Version | **v0.9** |
| Last Updated | **2026-08-05** |
| Author | **SEMS Design Team** |
| Status | **Draft — Phase 3.6 Authentication Regression / Formative Evaluation** |

[START HERE](../../START_HERE.md) › [Design/UI_UX](./README.md) › SEMS Wireframe UAT Checklist

**วัตถุประสงค์:** ใช้ทำ Stakeholder Review, Prototype Evaluation, Usability Walkthrough และ Formative Evaluation ก่อนเริ่มพัฒนา Frontend
**ผู้ทดสอบที่แนะนำ:** Admin อย่างน้อย 2 คน และ Evaluator อย่างน้อย 2 คน

> ชื่อไฟล์เดิมคงไว้ตาม Repository Convention แต่กิจกรรมนี้ **ไม่ใช่ Formal UAT** ไม่มีผลอนุมัติ Requirement Baseline, System Design หรือ Production Readiness

## วิธีทดสอบ

1. ให้ผู้ทดสอบทำ Task โดยผู้ดำเนินการไม่บอกตำแหน่งปุ่มล่วงหน้า
2. บันทึกเวลาที่ใช้ จุดที่หยุดคิด จุดที่คลิกผิด และคำถามที่ผู้ทดสอบถาม
3. หลังจบแต่ละ Task ให้คะแนนความง่าย 1-5
4. แยกข้อเสนอแนะเป็น Critical, Major, Minor และ Nice-to-have

## Phase 1–2 Evaluation Tasks

### ADMIN

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---|
| P12-A01 | Demo Login เป็น ADMIN | เข้า Admin Dashboard โดยไม่มี KKU connection จริง | | | | | | |
| P12-A02 | เปิดหน้าจัดการผู้ใช้งาน | เห็นเฉพาะข้อมูลบัญชีสังเคราะห์ | | | | | | |
| P12-A03 | ค้นหาบัญชี | แสดงผลตรงคำค้นหรือ Empty Result | | | | | | |
| P12-A04 | เพิ่มบัญชี Simulation | Validation ทำงานและเพิ่มบัญชีใน Demo State | | | | | | |
| P12-A05 | เปลี่ยน Role | มี Confirmation, Success Feedback และ Audit Notice | | | | | | |
| P12-A06 | ปิดสถานะบัญชี | มี Confirmation และแสดง Inactive | | | | | | |
| P12-A07 | ทดลองเข้าหน้าที่ EVALUATOR-only | Route Guard แสดง Permission Denied โดยไม่แสดงข้อมูลหน้าปลายทาง | | | | | | |
| P12-A08 | Logout | ล้าง Demo Session และกลับ Login; ย้อน hash ไม่ได้ | | | | | | |

### EVALUATOR

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---|
| P12-E01 | Demo Login เป็น EVALUATOR | เข้า Select Applicant โดยไม่มี KKU connection จริง | | | | | | |
| P12-E02 | ทดลองเข้าหน้า `#users` | Route Guard แสดง Permission Denied | | | | | | |
| P12-E03 | เลือก Scenario: Session Expired | Protected screen ถูกปิดและแสดง safe expiry dialog | | | | | | |
| P12-E04 | กลับ Login | กลับหน้า Login โดยไม่แสดง protected data | | | | | | |
| P12-E05 | Login ใหม่และ Logout | Session ถูกล้างและ hash route ถูกป้องกัน | | | | | | |

### Prototype Controls

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---|
| P12-C01 | เปลี่ยน Demo Role | Navigation เปลี่ยนตาม Role และ guard ยังคงทำงาน | | | | | | |
| P12-C02 | ทดสอบ Not Provisioned/Inactive/Denied | แสดง safe error โดยไม่สร้าง Session | | | | | | |
| P12-C03 | Reset Demo State | คืน role/session/users/draft/submitted/round/dialog/message เป็นค่าเริ่มต้น | | | | | | |

## Phase 2.5 Stabilization Checks

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---|
| P25-01 | Demo Login เป็น ADMIN แล้วตรวจ Role Switcher | แสดง ADMIN และไป `#dashboard` | | | | | | |
| P25-02 | Demo Login เป็น EVALUATOR แล้วตรวจ Role Switcher | แสดง EVALUATOR และไป `#select-applicant` | | | | | | |
| P25-03 | เปิด User dialog แล้วสลับ Role | Dialog/context ถูกล้างและไป safe route ของ Role ใหม่ | | | | | | |
| P25-04 | สร้าง Toast แล้ว Logout/Reset/Role Switch | Toast เดิมไม่ค้างหรือกลับมาแสดง | | | | | | |
| P25-05 | กด Enter ใน Add User form | Validation หรือเพิ่มบัญชีโดยไม่ reload หน้า | | | | | | |
| P25-06 | ตรวจ Placeholder/Pending controls | Item 3–6 เป็น interaction/state จริง; Item 10–11 และ Pending features ยัง disabled พร้อมเหตุผล | | | | | | |
| P25-07 | Session Expired แล้วลองเปลี่ยน Role | Session ไม่กลับ Active และ protected screen ไม่แสดง | | | | | | |

## Phase 3 — ADMIN Preparation Formative Evaluation Tasks

ตารางนี้ใช้สำหรับ Stakeholder Review, Prototype Evaluation และ Usability Walkthrough เท่านั้น ไม่ใช่ Formal UAT

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Completion Time | Ease 1–5 | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---:|---|---|
| P3-R01 | สร้างรอบทุนใหม่และบันทึก Draft | Validation ผ่านและมี Round DRAFT ใหม่ในรายการ | | | | | | | | |
| P3-R02 | พยายามเปิดรอบที่ยังไม่พร้อม | SYSTEM block และไม่เปลี่ยนเป็น OPEN | | | | | | | | |
| P3-R03 | ตรวจรายการ Readiness | เห็น Ready/Not Ready, detail และ action ไปแก้ | | | | | | | | |
| P3-R04 | แก้ข้อมูลจนพร้อม | Metadata, Application, Active Criteria และ Evaluator พร้อม | | | | | | | | |
| P3-R05 | ยืนยันเปิดรอบ | Confirmation แสดงผลกระทบและเปลี่ยน DRAFT→OPEN พร้อม notice | | | | | | | | |
| P3-I06 | เลือก Valid Dataset | แสดง File Selected และพร้อม Processing โดยไม่อ่านไฟล์จริง | | | | | | | | |
| P3-I07 | Mapping Column | Required mapping ครบและไม่ซ้ำ | | | | | | | | |
| P3-I08 | เปิด Preview | เห็น row/type/normalized value/status/count โดย Applicant State ยังไม่เปลี่ยน | | | | | | | | |
| P3-I09 | Confirm Import | แสดง All-or-Nothing confirmation และเพิ่ม Applicant/Application ใน Demo State | | | | | | | | |
| P3-I10 | เลือก Error Dataset | Preview แสดง Error ราย row/field/code | | | | | | | | |
| P3-I11 | ตรวจ Validation Error | Error Report อธิบายสาเหตุและวิธีแก้ | | | | | | | | |
| P3-I12 | พยายาม Import ขณะมี Error | ปุ่ม/Action ถูก block และไม่มี Partial Import | | | | | | | | |
| P3-A13 | ค้นหา Applicant | พบ Applicant หรือ Empty Result ตามคำค้น/สถานะ | | | | | | | | |
| P3-A14 | เปิดรายละเอียด Application | เห็น Applicant แยกจาก independent Applications ตาม round/type | | | | | | | | |
| P3-A15 | แก้ข้อมูลที่อนุญาต | Semantic form validation และ state mutation; business key ไม่เปลี่ยน | | | | | | | | |
| P3-D16 | Upload Sample Document | ตรวจ type/size และเปลี่ยน security state | | | | | | | | |
| P3-D17 | ตรวจ Scanning State | มี status/reason และเปิด Detail ไม่ได้ | | | | | | | | |
| P3-D18 | ตรวจ Quarantined State | View ถูก block พร้อมเหตุผล โดยไม่มี scanner จริง | | | | | | | | |
| P3-D19 | เปิด Clean Document Detail | เห็น synthetic metadata/privacy notice โดยไม่มีไฟล์หรือ URL จริง | | | | | | | | |
| P3-C20 | แก้ Draft Criteria | Edit/add/delete/expand และ Save Draft เปลี่ยน state | | | | | | | | |
| P3-C21 | สร้าง Validation Error | Validation Summary แสดง rule และตำแหน่งให้กลับไปแก้ | | | | | | | | |
| P3-C22 | พยายาม Activate Criteria ที่ไม่ผ่าน | SYSTEM block และสถานะยัง DRAFT | | | | | | | | |
| P3-C23 | แก้ Criteria ให้ผ่าน | Metadata/range/code/order/total ผ่านตาม Config | | | | | | | | |
| P3-C24 | ยืนยัน Activate | เปลี่ยนเป็น ACTIVE และ editor เป็น read-only พร้อม Audit notice | | | | | | | | |
| P3-C25 | ตรวจ Round Readiness | Active Criteria ที่เชื่อมทำให้ readiness item เปลี่ยนเป็น Ready | | | | | | | | |

## Phase 3.5 — Blocking Fix Regression Tasks

รายการนี้เป็น Formative Prototype Evaluation และไม่ใช่ Formal UAT

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Completion Time | Ease 1–5 | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---:|---|---|
| P35-01 | เรียก Import Commit ตอน Empty Dataset | Shared guard block; Applicant/Application/Round count ไม่เปลี่ยน | | | | | | | | |
| P35-02 | เรียก Import Commit ตอน Unsupported `.xls` | Shared guard block และ state ไม่เป็น IMPORTED | | | | | | | | |
| P35-03 | เรียก Import Commit ตอน Mapping Invalid | Focus mapping error; ไม่มี Business State mutation | | | | | | | | |
| P35-04 | เปิด Applicant ที่มีสอง Applications | Document count/list แยกตาม selected Application | | | | | | | | |
| P35-05 | Upload ให้ Application A แล้วสลับ Application B | Document ใหม่อยู่เฉพาะ A; B ไม่เปลี่ยน | | | | | | | | |
| P35-06 | แก้ Criteria แล้วกดยกเลิก | Edit buffer ถูกทิ้งและ Saved Draft ไม่เปลี่ยน | | | | | | | | |
| P35-07 | แก้ Criteria แล้วเปลี่ยน Route โดยไม่ Save | แสดง Unsaved warning; ไม่ commit จนกด Save | | | | | | | | |
| P35-08 | เลือก Scenario ต่อเนื่อง A→B→A | แต่ละ Scenario เริ่ม Fresh Fixture และ A รอบสองเหมือน A รอบแรก | | | | | | | | |
| P35-09 | เลือก Phase 3 Scenario ก่อน Login แล้ว Login ADMIN | Scenario ถูก apply หลัง Login โดยไม่ข้าม session guard | | | | | | | | |
| P35-10 | ตรวจ Export ใน Phase 3.5 | Opener ถูก disable; direct route/handler ไม่สร้าง CSV หรือเปลี่ยน exportState | | | | | | | | |

## Phase 3.6 — Authentication Invariant Regression Task

รายการนี้เป็น Formative Prototype Evaluation และไม่ใช่ Formal UAT

| ID | Task | Expected Outcome | Task Success | Error | จุดที่ลังเล | ขอความช่วยเหลือ (ครั้ง) | Completion Time | Ease 1–5 | Feedback | Decision Required |
|---|---|---|---|---|---|---:|---|---:|---|---|
| P36-01 | ตั้ง `authenticationState=SIGNED_OUT`, `sessionState=ACTIVE`, `currentRole=ADMIN` แล้วเรียก Import Commit โดยตรง | Import ถูก block; Applicant/Application/Round count ไม่เปลี่ยน และ Import state ไม่เป็น `IMPORTED` | | | | | | | | |

## A. Existing Full-flow Admin Tasks — Later Formative Phases

ส่วน A–B คงไว้เป็น reference สำหรับ Phase ถัดไป ไม่ใช่ขอบเขตการตรวจ Phase 1–2 และไม่ใช่ Formal UAT

| ID | Task | Expected Outcome | ผ่าน/ไม่ผ่าน | เวลา | คะแนน 1-5 | หมายเหตุ |
|---|---|---|---|---|---|---|
| A-01 | Demo Login เป็น ADMIN | เข้าสู่ Admin Dashboard โดยไม่เชื่อม KKU OAuth/OIDC จริง | | | | |
| A-02 | สร้างรอบทุนใหม่ | รอบทุนอยู่สถานะ Draft | | | | |
| A-03 | อัปโหลดไฟล์ Data_import_to_web | ระบบอ่าน Header และไปหน้า Mapping | | | | |
| A-04 | Map คอลัมน์ `ชือ` เป็น `first_name` | Mapping ถูกต้องและแสดง Conversion | | | | |
| A-05 | ตรวจ continuation rows ของ กยศ./ทุน | ระบบรวมแถวต่อเนื่องกับผู้สมัครแถวหลัก | | | | |
| A-06 | ตรวจ Import Error | พบเลขแถว Error Code และวิธีแก้ | | | | |
| A-07 | ยืนยัน Import | เห็นจำนวนผู้สมัครนำเข้าสำเร็จ | | | | |
| A-08 | เปิดรายละเอียดผู้สมัคร | เห็นข้อมูล ครอบครัว ประวัติ และเอกสาร | | | | |
| A-09 | สร้าง/ตรวจชุดเกณฑ์ | คะแนนเต็มและ Required ถูกต้อง | | | | |
| A-10 | เปิดรอบทุน | Evaluator สามารถเห็นรายชื่อผู้สมัคร | | | | |
| A-11 | ตรวจผู้สมัครที่ Submitted 2/3 | สถานะ `MINIMUM_COMPLETE` และมีคะแนนสรุป | | | | |
| A-12 | ตรวจหลังผู้ประเมินคนที่ 3 Submit | สถานะ `FULLY_COMPLETE` และคะแนนสรุปคำนวณใหม่ | | | | |
| A-13 | ปิดรอบทุน | เห็น Finalized และ `CLOSED_INCOMPLETE` ก่อนยืนยัน | | | | |
| A-14 | Export Excel/CSV | ได้รายงานตาม Filter และมีประวัติ Export | | | | |

## B. Existing Full-flow Evaluator Tasks — Preserve and Re-verify

| ID | Task | Expected Outcome | ผ่าน/ไม่ผ่าน | เวลา | คะแนน 1-5 | หมายเหตุ |
|---|---|---|---|---|---|---|
| E-01 | Demo Login เป็น EVALUATOR | เข้าสู่หน้าเลือกผู้สมัครโดยไม่เชื่อม KKU OAuth/OIDC จริง | | | | |
| E-02 | ค้นหาผู้สมัครด้วยรหัส/ชื่อ | พบผู้สมัครและเห็นจำนวนผู้ประเมิน | | | | |
| E-03 | เลือกผู้สมัคร | สร้าง Evaluation สถานะ Draft | | | | |
| E-04 | ดูข้อมูลและเอกสาร | เข้าถึงเฉพาะผู้สมัครที่เลือก | | | | |
| E-05 | ให้คะแนนทุกเกณฑ์ | ระบบตรวจ min/max และ Required | | | | |
| E-06 | บันทึก Draft | เห็นเวลาบันทึกล่าสุดและกลับมาทำต่อได้ | | | | |
| E-07 | Review Before Submit | เห็นคะแนน ความคิดเห็น และคะแนนรวมครบ | | | | |
| E-08 | ยืนยัน Submit | สถานะเป็น Submitted และแก้ไม่ได้ | | | | |
| E-09 | พยายามเลือกผู้สมัครเดิมซ้ำ | ระบบปฏิเสธและพาไป Evaluation เดิม | | | | |
| E-10 | พยายามเลือกผู้สมัคร 3/3 | ปุ่มถูกปิดหรือระบบแจ้งว่าเต็ม | | | | |

## C. Questions After Testing

ให้คะแนน 1-5 และบันทึกเหตุผล

| คำถาม | คะแนน | เหตุผล/ข้อเสนอแนะ |
|---|---|---|
| เมนูและคำศัพท์เข้าใจง่าย | | |
| ขั้นตอน Import ต่อเนื่องและไม่สับสน | | |
| หน้า Column Mapping ใช้งานง่าย | | |
| Error Report บอกวิธีแก้เพียงพอ | | |
| รายชื่อและรายละเอียดผู้สมัครหาได้ง่าย | | |
| หน้าประเมินหน้าเดียวช่วยลดการสลับหน้าจอ | | |
| การบันทึก Draft และ Submit ชัดเจน | | |
| สถานะ 0/3, 1/3, 2/3, 3/3 เข้าใจง่าย | | |
| หน้าสรุปผลตอบคำถามของงานทุน | | |
| Export รายงานมีตัวเลือกเพียงพอ | | |
| ความพึงพอใจโดยรวม | | |

## D. Issue Log

| Issue ID | Screen | รายละเอียด | Severity | ข้อเสนอแก้ไข | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|
| UI-001 | | | Critical/Major/Minor/Nice-to-have | | | Open |

## E. Stakeholder Review Record — Not Formal Approval

- [ ] Admin representative feedback recorded
- [ ] Evaluator representative feedback recorded
- [ ] Decision Required items assigned to an owner
- [ ] Critical และ Major formative-evaluation issues recorded
- [ ] ผู้เข้าร่วมเข้าใจว่ารายการนี้ไม่ใช่ Formal UAT หรือ Requirement approval

## F. Scope and Pending-Decision Checks

- [ ] Same student can be shown under two scholarship types without merging applications.
- [ ] Zero-applicant pre-open validation blocks Open; Open-round import remains available.
- [ ] Incomplete close lists affected applications and requires confirmation/reason.
- [ ] Reopen Submitted Evaluation แสดงเป็น Pending Decision และไม่มี confirmed workflow.
- [ ] Controlled Correction แสดงเป็น Pending Decision และ action ถูก disabled.
- [ ] Custom Score/Amount reason and amount ceiling validations are visible.
- [ ] Evaluator cannot see peer identity, scores, comments or amount recommendation.
- [ ] Dashboard Drill-down และ Advanced Report Lifecycle แสดงเป็น Pending Decision.
- [ ] Audit Search ไม่มี interactive screen; Audit recording แสดงได้เฉพาะ System Notice.
- [ ] Quarantined/Scanning content cannot be opened or downloaded.
- [ ] Idle/absolute session expiry returns safely to login.
- [ ] No national ID appears anywhere in the Release 1 flow.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.9 | 2026-08-05 | SEMS Design Team | Added Phase 3.6 authentication-invariant regression task; this remains formative evaluation, not Formal UAT. |
| v0.8 | 2026-08-05 | SEMS Design Team | Added 10 Phase 3.5 regression tasks for import guards, Application-owned documents, Criteria save boundary, deterministic scenarios and disabled Item 11 export. |
| v0.7 | 2026-08-05 | SEMS Design Team | Added 25 Phase 3 formative-evaluation tasks for Round, Import, Applicant/Document and Criteria workflows with completion time, ease score, feedback and decision capture. |
| v0.6 | 2026-08-05 | SEMS Design Team | Added Phase 2.5 role synchronization, temporary-UI cleanup, semantic-form, disabled-placeholder and expired-session stabilization checks. |
| v0.5 | 2026-08-05 | SEMS Design Team | Reframed the artifact as a formative prototype evaluation, added Phase 1–2 role/user/session/reset tasks and converted Should-have scenarios to pending-decision checks. |
| v0.4 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.3 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.2 | 2026-07-24 | SEMS Design Team | Added confirmed-response UAT scenarios; approval remains pending. |
| v1.1 | 2026-07-23 | SEMS Design Team | Removed trailing whitespace for automated documentation checks; approval remains pending. |
| v1.0 | 2026-07-23 | SEMS Design Team | Initial wireframe UAT checklist draft. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS Wireframe Specification](./SEMS_Wireframe_Specification.md)<br>
↑ หมวดเอกสาร: [Design/UI_UX](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ ขั้นตอนถัดไป: หลังบันทึก feedback และหลักฐานครบแล้ว ให้อัปเดต [SEMS Wireframe Specification](./SEMS_Wireframe_Specification.md) และ [บันทึกการอนุมัติการออกแบบระบบ](../../Requirements/Approvals/System_Design_Approval_Record.md)

<!-- DOC_NAV_END -->
