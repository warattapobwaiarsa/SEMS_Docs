# SEMS Import Test Cases

| Metadata | Value |
| :--- | :--- |
| Version | **v0.2** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

## Import Rule Baseline

- รองรับ Excel และ CSV
- ตัวอย่างมี 37 คอลัมน์
- `student_id` ต้องไม่ซ้ำในรอบทุน
- GPA ต้องอยู่ 0.00–4.00
- วันที่อาจมาในรูป `09 ก.ค. 2569 13:36` และต้องแปลง พ.ศ. เป็น ค.ศ.
- พิกัดเป็น `latitude, longitude`
- กยศ./ทุนสามารถมีหลายรายการและต่อเนื่องหลายแถว
- continuation row ต้องผูกกับ base applicant ก่อนหน้าเท่านั้น
- ต้องแสดงเลขแถว รายละเอียดและ Error Code

## Detailed Cases

### IMP-D-001 Valid Excel 37 Columns

**เงื่อนไขก่อนทดสอบ (Precondition):** Admin, Open/Draft target round ตาม import policy

**ขั้นตอน (Steps):** Upload → map all columns → preview → confirm

**ผลที่คาดหวัง (Expected):** batch success, applicant count ตรง base rows, child histories ตรง, source file metadata/audit ครบ

### IMP-D-002 Valid CSV UTF-8 with Thai Text

**ผลที่คาดหวัง (Expected):** header และข้อมูลภาษาไทยไม่เสีย, comma/quote parsing ถูกต้อง, row count ตรง

### IMP-D-003 Header Alias `ชือ`

**ขั้นตอน (Steps):** Upload sample ที่ใช้หัวคอลัมน์ `ชือ`

**ผลที่คาดหวัง (Expected):** ระบบเสนอ mapping ไป `first_name` หรือให้ Admin map เอง; หลังยืนยันไม่มี field name ผิดสะกดในฐานข้อมูล

### IMP-D-004 Required Field Missing

**Test Values:** `student_id`, first_name, last_name หรือ field ที่ SRS กำหนดเป็น required ว่าง

**ผลที่คาดหวัง (Expected):** `REQUIRED_FIELD_MISSING`, ระบุ row/column, confirm ถูก block

### IMP-D-005 Student ID Format

**Test Values:** valid `663040664-8`; invalid `6630406648`, ตัวอักษร, whitespace รอบค่า

**ผลที่คาดหวัง (Expected):** trim whitespace; valid pattern ผ่าน; invalid ถูก reject; check digit ตาม policy ที่อนุมัติ

### IMP-D-006 GPA Boundaries

| Input | Expected |
|---:|---|
| 0 | valid |
| 0.00 | valid |
| 4 | valid |
| 4.00 | valid |
| -0.01 | `INVALID_GPA` |
| 4.01 | `INVALID_GPA` |
| `สามจุดห้า` | `INVALID_GPA` |

### IMP-D-007 Buddhist Date Conversion

**ข้อมูลนำเข้า (Input):** `09 ก.ค. 2569 13:36`

**ผลที่คาดหวัง (Expected):** 2026-07-09 13:36 ใน timezone ที่กำหนด; raw value เก็บใน import lineage หากออกแบบไว้

### IMP-D-008 Invalid/Ambiguous Date

**Inputs:** `31 ก.พ. 2569`, `09/13/2569`, empty required date

**ผลที่คาดหวัง (Expected):** `INVALID_DATE` หรือ required error; ไม่ fallback แบบเดาผิด

### IMP-D-009 Phone Leading Zero and Scientific Notation

**Inputs:** `0810000001`, numeric Excel cell, `8.10000001E8`

**ผลที่คาดหวัง (Expected):** phone ถูกจัดเก็บเป็น string พร้อม leading zero; scientific notation ต้อง normalize ได้อย่างปลอดภัยหรือถูก reject พร้อม error ที่ชัดเจน ห้ามเปลี่ยนหมายเลขโดยเงียบ

### IMP-D-010 Email Validation

**Inputs:** valid KKU email, general email, missing `@`, whitespace, uppercase

**ผลที่คาดหวัง (Expected):** trim; validate syntax; normalization policy ไม่ทำลาย local part; invalid ถูกแจ้ง

### IMP-D-011 Coordinate Valid

**ข้อมูลนำเข้า (Input):** `16.37929729279832, 104.38542017283481`

**ผลที่คาดหวัง (Expected):** latitude และ longitude แยกเป็น decimal ถูกต้อง

### IMP-D-012 Coordinate Boundaries/Invalid

| Input | Expected |
|---|---|
| `-90,-180` | valid boundary |
| `90,180` | valid boundary |
| `91,100` | invalid latitude |
| `16,181` | invalid longitude |
| `abc,104` | invalid format |
| `16.3` | missing longitude |

### IMP-D-013 Duplicate in Same File

**ขั้นตอน (Steps):** ใส่ base rows 2 แถวที่ student_id เดียวกัน

**ผลที่คาดหวัง (Expected):** `DUPLICATE_STUDENT` ทั้งคู่หรือแถวหลังตาม policy; preview แสดง conflict; ไม่มี duplicate DB rows

### IMP-D-014 Duplicate Existing in Target Round

**ผลที่คาดหวัง (Expected):** reject/update/skip ตาม policy ที่อนุมัติ; ต้อง deterministic และ audit; ห้าม duplicate ApplicantRound

### IMP-D-015 Same Student Across Different Rounds

**ผลที่คาดหวัง (Expected):** person identity อาจ reuse ได้ แต่ ApplicantRound แยกตาม round; ไม่ถือ duplicate ข้ามรอบหาก policy อนุญาต

### IMP-D-016 Multi-row Loan/Scholarship Grouping

**Input Pattern:**

```text
Base row: student_id + applicant data + กยศ `-2565 : 66,000` + ทุน `-2565 ... : 10,000`
Continuation: core columns blank + กยศ `-2566 : 66,000` + ทุน `-2567 ทุน ข : 10,000`
Continuation: core columns blank + กยศ `-2567 : 66,000` + ทุน `-2568 ทุน ข : 10,000`
```

**ผลที่คาดหวัง (Expected):** applicant 1 คน, loan 3 รายการ, scholarship 3 รายการ; order/source row preserved

### IMP-D-017 Orphan Continuation

**ข้อมูลนำเข้า (Input):** row 2 มีเฉพาะ กยศ./ทุน โดยไม่มี base row ก่อนหน้า

**ผลที่คาดหวัง (Expected):** `ORPHAN_CONTINUATION_ROW`, ไม่ผูกกับ applicant ก่อนหน้าอีกกลุ่มโดยข้าม separator/sheet

### IMP-D-018 Continuation Row Contains Conflicting Core Data

**ข้อมูลนำเข้า (Input):** core student_id ว่างแต่ first_name หรือ student_id อื่นบางส่วนปรากฏ พร้อม child history

**ผลที่คาดหวัง (Expected):** reject `AMBIGUOUS_CONTINUATION_ROW` (provisional) หรือบังคับเป็น base row ตาม explicit rule; ห้าม merge โดยเดา

### IMP-D-019 Loan Parsing

**ข้อมูลนำเข้า (Input):** `-2565 : 66,000`

**ผลที่คาดหวัง (Expected):** year=2565 (หรือแปลงเป็น 2022 ตาม data model ที่ยืนยัน), amount=66000; comma ไม่ทำให้ parse ผิด

### IMP-D-020 Scholarship Parsing

**ข้อมูลนำเข้า (Input):** `-2567 ทุน ข : 10,000`

**ผลที่คาดหวัง (Expected):** year=2567, scholarship_name=`ทุน ข`, amount=10000

### IMP-D-021 Blank/Hyphen Meaning

**Inputs:** blank, `-`, whitespace

**ผลที่คาดหวัง (Expected):** map เป็น null/no-history ตาม field policy ไม่เก็บ `-` เป็นค่าจริงโดยไม่ตั้งใจ

### IMP-D-022 File Type/MIME Mismatch

**ข้อมูลนำเข้า (Input):** executable/text renamed `.xlsx`

**ผลที่คาดหวัง (Expected):** reject ก่อน parser, `UNSUPPORTED_FILE_TYPE` หรือ malformed file error; ไม่ execute macro/content

### IMP-D-023 Oversized File/Too Many Rows

**ผลที่คาดหวัง (Expected):** enforce configured limit, clear error, no partial hidden batch, temp file cleanup

### IMP-D-024 Atomic Import Failure

**เงื่อนไขก่อนทดสอบ (Precondition):** policy = all-or-nothing

**ข้อมูลนำเข้า (Input):** valid 99 rows + invalid row 100

**ผลที่คาดหวัง (Expected):** confirm rejected/transaction rollback; imported count=0; error count correct

### IMP-D-025 Partial Import Policy

**เงื่อนไขก่อนทดสอบ (Precondition):** ใช้เฉพาะเมื่อ Product Owner อนุมัติ partial import

**ผลที่คาดหวัง (Expected):** valid rows import, invalid rows skipped; exact success/error counts; rerun ไม่ duplicate; batch status=`CompletedWithErrors`

### IMP-D-026 Concurrent Confirm Same Batch

**ขั้นตอน (Steps):** Admin double-click confirm หรือส่ง 2 requests

**ผลที่คาดหวัง (Expected):** batch processed ครั้งเดียว; second request idempotent/rejected; no duplicate applicant/history

### IMP-D-027 Reconciliation after Import

**Checks:**

- base row count = ApplicantRound created/skipped/errors ตาม policy
- continuation count = child histories created/errors
- no Applicant with missing required identity
- no orphan ApplicantExpense/Parent/History
- ImportBatch totals sum correctly

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.2 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
