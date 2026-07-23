# SEMS High Risk Test Cases

| Metadata | Value |
| :--- | :--- |
| Version | **v0.2** |
| Last Updated | **2026-07-23** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

กรณีในไฟล์นี้เป็น P0/P1 และควรถูกทดสอบก่อนกรณีทั่วไป ทุกกรณีต้องตรวจ API, Database และ Audit Event ไม่ใช่ตรวจเฉพาะ UI

---

## HR-SEL-001 ผู้ประเมินคนเดิมเลือกผู้สมัครซ้ำ

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | DB + API + E2E |
| Preconditions | Round `R-OPEN-01` เป็น Open; U-EVA-01 Active; applicant ยังมี slot; U-EVA-01 มี active Evaluation กับ applicant แล้ว |
| Test Data | evaluator=U-EVA-01, applicant=A-D1 |

**Steps**

1. Login เป็น U-EVA-01
2. เปิดหน้ารายชื่อผู้สมัครและกดเลือก applicant เดิมอีกครั้ง
3. เรียก API สร้าง Evaluation ซ้ำโดยตรงเพื่อ bypass UI
4. ตรวจตาราง Evaluation และ Audit Log

**Expected Result**

- UI ไม่สร้างรายการซ้ำและแสดงข้อความเหมาะสม
- API ตอบ `409 DUPLICATE_EVALUATION`
- มี active Evaluation ของ evaluator/applicant/round เพียง 1 รายการ
- unique constraint หรือ business transaction ป้องกันได้แม้ bypass UI
- ไม่มีการนับ evaluator เพิ่ม และไม่มี Result Summary เปลี่ยน
- Audit บันทึก denied/duplicate attempt โดยไม่มีข้อมูลลับ

---

## HR-SEL-002 ผู้ประเมินคนที่ 4 พยายามเลือก

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | DB + API + E2E |
| Preconditions | Applicant มี active Evaluation ครบ 3 จาก U-EVA-01..03; Round Open |

**Steps**

1. Login เป็น U-EVA-04
2. ค้นหา applicant ที่มี 3/3
3. กดเลือกและเรียก API โดยตรง

**Expected Result**

- ปุ่มเลือก disabled/hidden ตาม UX แต่ API ต้องตรวจซ้ำ
- API ตอบ `409 EVALUATOR_LIMIT_REACHED`
- DB ยังคงมี active Evaluation 3 รายการ
- U-EVA-04 ไม่ได้รับสิทธิ์ดูรายละเอียดละเอียดอ่อนหรือเอกสาร
- Audit บันทึก rejected attempt

---

## HR-SEL-003 อาจารย์สองคนเลือก slot ที่ 3 พร้อมกัน

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Concurrency Integration |
| Preconditions | Applicant มี active Evaluation 2 รายการ; U-EVA-03 และ U-EVA-04 ยังไม่เคยเลือก |

**Steps**

1. เตรียม two-request barrier
2. ส่ง `create evaluation` จาก U-EVA-03 และ U-EVA-04 ในเวลาเดียวกัน
3. ทำซ้ำอย่างน้อย 20 รอบหลัง reset dataset
4. ตรวจ response, DB และ Audit ทุกครั้ง

**Expected Result**

- สำเร็จเพียง 1 request
- อีก request ตอบ `409 EVALUATOR_LIMIT_REACHED`
- DB มี active Evaluation เท่ากับ 3 เสมอ ไม่มี 4 ชั่วคราวหรือถาวร
- transaction rollback สมบูรณ์
- ไม่มี duplicate owner/slot และไม่มี orphan permission
- ผลลัพธ์ deterministic ตาม constraint แม้ process/backend มากกว่า 1 instance

---

## HR-SEL-004 ผู้ประเมิน double-click เลือกพร้อมกัน

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Concurrency Integration |
| Preconditions | U-EVA-01 ยังไม่มี Evaluation กับ applicant; มี slot |

**Steps**

1. ส่งคำขอสร้าง Evaluation 2 คำขอพร้อมกันจาก U-EVA-01
2. ตรวจ response และ DB

**Expected Result**

- มี active Evaluation เพียง 1 รายการ
- คำขอที่สองตอบ `409 DUPLICATE_EVALUATION` หรือคืน resource เดิมตาม idempotency contract ที่อนุมัติ
- จำนวน evaluator ไม่เพิ่มสองครั้ง
- Audit ไม่ทำให้เข้าใจผิดว่าเกิด evaluation สองรายการ

---

## HR-EVA-001 มี Draft แต่ยังไม่ Submit

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit + API + E2E + Reconciliation |
| Preconditions | U-EVA-01 มี Draft คะแนนครบหรือไม่ครบ; applicant ไม่มี Submitted อื่น |

**Steps**

1. บันทึกคะแนนเป็น Draft
2. เปิด Dashboard/Result Summary
3. Export Excel/CSV
4. Query aggregation source ใน DB

**Expected Result**

- Evaluation status = Draft
- applicant = In Progress
- submitted count = 0/3
- ไม่มี final/result summary score จาก Draft
- Dashboard score visualization และ Export ไม่ใช้คะแนน Draft
- ผู้ประเมินกลับมาแก้ Draft ของตนได้

---

## HR-SCR-001 Submitted ครบ 2 คน

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit + Integration + E2E |
| Preconditions | U-EVA-01 total=80 Submitted; U-EVA-02 Draft total=90; Round Open |

**Steps**

1. U-EVA-02 Review และ Submit
2. Refresh applicant summary
3. ตรวจ DB Result Summary, Dashboard และ Export

**Expected Result**

- Submitted count = 2/3
- state = Minimum Complete
- Result Summary ถูกสร้าง/อัปเดตเพียง 1 รายการต่อ applicant/round
- ใช้เฉพาะผล Submitted ของ evaluator ที่ไม่ซ้ำกัน 2 คน
- expected score ตรง reference formula/rounding ที่อนุมัติ
- Round ยัง Open และยังอนุญาตคนที่ 3 เลือกได้ถ้ามี slot

---

## HR-SCR-002 ผู้ประเมินคนที่ 3 Submit เพิ่ม

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit + Integration + E2E + Reconciliation |
| Preconditions | Applicant Minimum Complete จาก totals 80, 90; U-EVA-03 มี Draft total=70; Round Open |

**Steps**

1. บันทึกค่า Result Summary เดิมและ `updated_at/version`
2. U-EVA-03 Submit
3. ตรวจ Summary, state, dashboard และ export

**Expected Result**

- Submitted count = 3/3
- state = Fully Complete
- Result Summary เดิมถูก update ไม่สร้างรายการซ้ำ
- คำนวณจากผล Submitted ทั้ง 3 คนใหม่ตามสูตรอนุมัติ
- หากใช้ค่าเฉลี่ย ตัวอย่าง expected เปลี่ยน 85.00 → 80.00
- Dashboard และรายงานสะท้อนค่าใหม่
- Audit ระบุ third evaluator submission และ summary recalculation

---

## HR-RND-001 ปิดรอบเมื่อผู้สมัครครบขั้นต่ำ

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Integration + E2E |
| Preconditions | Round Open; applicant A-S2 และ A-S3 มี Submitted ≥2 |

**Steps**

1. Admin ปิดรอบ
2. ตรวจ state ของ A-S2/A-S3
3. พยายามสร้าง Evaluation/Submit เพิ่ม
4. Export final report

**Expected Result**

- state ของทั้งสองเป็น Finalized
- latest summary ถูกถือเป็น final
- ห้ามสร้าง Evaluation ใหม่และห้าม Submit เพิ่ม (`ROUND_NOT_OPEN`)
- final report ตรง DB และแสดง Finalized
- close action และจำนวน finalized ถูก audit

---

## HR-RND-002 ปิดรอบเมื่อผลไม่ครบ 2 คน

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Integration + E2E |
| Preconditions | Applicant มี 0 หรือ 1 Submitted; อาจมี Draft |

**Steps**

1. Admin ปิดรอบ
2. ตรวจ applicant state และ summary
3. Export report

**Expected Result**

- state = Closed Incomplete
- ไม่มี final summary score
- Draft/Submitted เพียง 1 คนไม่ถูกทำให้เป็น final
- report แสดง Closed Incomplete และช่อง final score ว่าง/null ตาม template
- ห้าม Submit หลังปิดรอบ

---

## HR-IMP-001 Excel มีข้อมูลผิดรูปแบบ

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit parser + API + E2E |
| Test Data | missing student_id, GPA 4.01, invalid date, malformed email/phone, coordinate `95,181` |

**Steps**

1. Upload file และ map columns
2. Run Preview/Validation
3. พยายาม Confirm Import

**Expected Result**

- แสดง row number, column, raw value และ error code แยกรายข้อ
- ได้ `REQUIRED_FIELD_MISSING`, `INVALID_GPA`, `INVALID_DATE`, `INVALID_COORDINATE` ตามกรณี
- ห้าม confirm หาก policy กำหนด all-or-nothing และยังมี blocking error
- ไม่มี invalid applicant/child rows เข้าฐานข้อมูล
- Import Batch เก็บสถานะและสถิติอย่างถูกต้อง

---

## HR-IMP-002 ผู้สมัครหนึ่งคนกินพื้นที่หลายแถว

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit parser + Integration + Reconciliation |
| Test Data | Base row มี applicant; 3 แถวถัดมามีเฉพาะ กยศ./ทุน เช่น `-2565 : 66,000`, `-2567 ทุน ข : 10,000` |

**Steps**

1. Upload และ preview file
2. ตรวจ grouping preview
3. Confirm Import
4. Query applicant, loan_history และ scholarship_history

**Expected Result**

- สร้าง Applicant/ApplicantRound เพียง 1 รายการ
- continuation rows ผูกกับ base row ก่อนหน้าอย่างถูกต้อง
- ปี ชื่อทุน และจำนวนเงินแยกถูกต้อง ไม่เกิด applicant ว่าง
- จำนวน child history ตรงกับแถวทั้งหมด
- row lineage/import source row ตรวจสอบย้อนกลับได้

---

## HR-IMP-003 Orphan continuation row

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Unit + API |
| Preconditions | แถวแรกหรือแถวหลัง separator มีเฉพาะ กยศ./ทุน ไม่มี base applicant ก่อนหน้า |

**Expected Result**

- `ORPHAN_CONTINUATION_ROW`
- ระบุเลขแถวและข้อมูล raw
- ไม่เดาว่าจะผูกกับ applicant ใด
- ไม่สร้าง child history หรือ applicant ว่าง

---

## HR-REP-001 รายงานตรงกับฐานข้อมูล

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | Reconciliation + E2E |
| Preconditions | Dataset มี Not Started, In Progress, Minimum Complete, Fully Complete, Finalized, Closed Incomplete |

**Steps**

1. Capture SQL truth set จาก Evaluation + Result Summary
2. Export Excel และ CSV
3. เทียบ row count, key, evaluator count, submitted count, totals, state และ summary
4. ตรวจ Draft/Cancelled records

**Expected Result**

- ทุก key/value ตรง DB ตาม approved template
- Draft/Cancelled ไม่ถูกนำไปคำนวณ
- ไม่มี row หาย/ซ้ำ
- Excel และ CSV ให้ข้อมูลเชิงสาระเหมือนกัน
- export audit มี user, round, timestamp, format และ row count

---

## HR-SEC-001 ผู้ประเมินเปิดเอกสารของผู้สมัครที่ตนไม่ได้เลือก

| Field | Detail |
|---|---|
| Priority | P0 |
| Level | API Security + E2E |
| Preconditions | U-EVA-01 เลือก Applicant A; Applicant B อยู่ในรอบ Open แต่ U-EVA-01 ไม่ได้เลือก |

**Steps**

1. Login U-EVA-01
2. คัดลอก document ID/URL ของ Applicant B จาก admin/test fixture
3. เรียก metadata, view และ download endpoint โดยตรง
4. ทดลองเปลี่ยน sequential ID/path

**Expected Result**

- ตอบ `403 ACCESS_DENIED` หรือ `404` ตาม security contract
- ไม่คืน metadata, filename, storage path หรือ signed URL
- ไม่มีข้อมูลใน response timing/error ที่ช่วย enumerate
- audit บันทึก access denied โดยไม่บันทึก token
- เอกสาร Applicant A ที่ตนเลือกยังเปิดได้ตามปกติ

---

## HR-SEL-005 Evaluation ถูกยกเลิกแล้วต้องคืน slot

| Field | Detail |
|---|---|
| Priority | P1 |
| Level | DB + API + E2E |
| Preconditions | Applicant มี 3 active evaluations; หนึ่งรายการ Draft และได้รับอนุญาตให้ cancel |

**Steps**

1. Cancel Draft ตามสิทธิ์
2. ตรวจ active count
3. ให้ U-EVA-04 เลือก applicant

**Expected Result**

- cancelled record ถูกเก็บเพื่อ audit แต่ไม่ถูกนับ active
- active count เปลี่ยน 3 → 2
- U-EVA-04 สร้าง evaluation ใหม่ได้และ active count กลับเป็น 3
- cancelled score ไม่เข้า summary/report

---

## HR-EVA-002 มี Draft เดิมและ applicant ครบ 3 slot

| Field | Detail |
|---|---|
| Priority | P1 |
| Level | API + E2E |
| Preconditions | U-EVA-03 มี Draft ของ applicant; active count รวมเป็น 3 |

**Expected Result**

- U-EVA-03 เปิดและแก้ Draft เดิมได้
- ระบบไม่พยายามสร้าง Evaluation ใหม่
- evaluator คนอื่นที่ไม่มี record ถูกปฏิเสธเพราะครบ 3
- Save Draft ไม่เปลี่ยน submitted count หรือ state เป็น Fully Complete

---

## HR-SCR-003 Embedded Point ห้ามคูณ Weight ซ้ำ

| Field | Value |
|---|---|
| Priority | P0 |
| Linked Requirement | FR-SCO-002 |
| Linked Decision | RD-010, RD-012 |

**Expected Result:** คะแนน option ทั้ง 10 ข้อรวม 75 ต้องได้ evaluator total 75 ไม่ใช่ผลจากการคูณ `weight_percent` ซ้ำ

## HR-IMP-004 Transaction Rollback

| Field | Value |
|---|---|
| Priority | P0 |
| Linked Requirement | FR-IMP-013 |
| Linked Decision | RD-018 |

**Expected Result:** เมื่อ Confirm Import ล้มเหลวกลาง transaction ต้องไม่มี Applicant/History บางส่วนค้าง และ batch/audit ระบุ failure โดยไม่เปิดเผยข้อมูลลับ

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2026-07-23 | SEMS QA Team | Canonicalized duplicate error code and added embedded-point and rollback P0 cases. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial high-risk test cases. |
