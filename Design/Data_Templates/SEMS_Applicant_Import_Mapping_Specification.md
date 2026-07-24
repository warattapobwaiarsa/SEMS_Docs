# SEMS — Applicant Import Mapping Specification

| รายการ | รายละเอียด |
|---|---|
| Version | **v0.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Design Team** |
| Scope | Applicant Import จาก [`Data_import_to_web.xlsx`](./Data_import_to_web.xlsx) |
| Source Structure | 37 คอลัมน์; รองรับ Legacy Continuation Row |
| Target Database | PostgreSQL / Prisma Schema ของ SEMS |
| Status | **Confirmed Response — Pending Formal Approval** |

## 1. วัตถุประสงค์

กำหนดการจับคู่คอลัมน์จาก Excel/CSV ไปยังฟิลด์ในฐานข้อมูล กฎการแปลงข้อมูล การตรวจสอบความถูกต้อง การจัดการข้อมูลหลายแถวต่อผู้สมัคร และ Error Code ที่ระบบ Import ต้องส่งกลับในหน้า Preview และรายงานข้อผิดพลาด

## 2. กฎกลางของการนำเข้า

1. ผู้ดูแลต้องเลือกรอบทุน (`round_id`) ก่อน Import; ไม่ต้องมีคอลัมน์รอบทุนในไฟล์
2. Release 1 Business Key คือ `round_id + scholarship_type_id + student_id`; one student may have independent applications for multiple scholarship types in the same round.
3. ช่องว่าง, Whitespace และค่าที่เท่ากับ `-` ทั้ง Cell ให้แปลงเป็น `NULL`; ค่า `0` ต้องเก็บเป็นศูนย์ ไม่ใช่ `NULL`
4. รหัสนักศึกษาและโทรศัพท์ต้องอ่านเป็น Text เพื่อคงเลขศูนย์นำหน้าและป้องกัน Scientific Notation
5. แถวที่มี `student_id` เป็น Applicant Row; แถวที่ไม่มี `student_id` แต่มีเฉพาะ `กยศ`/`ทุน` เป็น Continuation Row
6. Continuation Row ต้องผูกกับ Applicant Row ก่อนหน้าที่ผ่าน Validation และต้องแสดงเจ้าของในหน้า Preview
7. ข้อมูล กยศ. และทุนต้องสร้างเป็น Child Record แยก ไม่เก็บเป็นข้อความรวมในตารางผู้สมัคร
8. ข้อมูลซ้ำภายในไฟล์เป็น Error; ข้อมูลซ้ำกับรอบทุนให้ Skip เป็นค่าเริ่มต้น และ Update ได้เฉพาะกรณีที่ผู้ดูแลเลือกและยังไม่มี Evaluation
9. การ Import จริงต้องทำใน Transaction และบันทึก Import Batch, Raw Row, Validation Message และผลลัพธ์เพื่อ Audit

## 3. Column Mapping

| No. | Excel | หัวคอลัมน์ | Target | Field | Requirement | Conversion / Validation | Continuation |
|---|---|---|---|---|---|---|---|
| 1 | A | ลำดับ | `applicants` | `sequence_no` | Optional | Trim; Integer; > 0 เมื่อมีค่า | ต้องว่าง |
| 2 | B | รหัส | `applicants` | `student_id` | Hard Required | อ่านเป็น Text; Trim; คงเครื่องหมายขีดกลาง; ^\d{9}-\d$; Unique ภายในรอบทุน; ยังไม่ตรวจ check digit | ว่างได้เฉพาะ Continuation Row และสืบทอดจาก Applicant Row ก่อนหน้า |
| 3 | C | คำนำหน้า | `applicants` | `title` | Required before Evaluation | Trim; Map กับ Code List; ต้องอยู่ในชุดค่าที่อนุญาต เช่น นาย/นาง/นางสาว/อื่น ๆ | ต้องว่าง |
| 4 | D | ชือ | `applicants` | `first_name` | Hard Required | Trim; รองรับ Alias “ชื่อ”; ห้ามว่างหลัง Trim | ต้องว่าง |
| 5 | E | สกุล | `applicants` | `last_name` | Hard Required | Trim; ห้ามว่างหลัง Trim | ต้องว่าง |
| 6 | F | คณะ | `applicants` | `faculty_name` | Hard Required | Trim; Map กับข้อมูลอ้างอิง; ห้ามว่าง; ค่าไม่รู้จักให้ Warning/เลือก Mapping | ต้องว่าง |
| 7 | G | สาขา | `applicants` | `major_name` | Hard Required | Trim; Map กับข้อมูลอ้างอิง; ห้ามว่าง; ค่าไม่รู้จักให้ Warning/เลือก Mapping | ต้องว่าง |
| 8 | H | ชั้นปี | `applicants` | `year_level` | Hard Required | Integer; 1–8 (ช่วง Draft; ต้องยืนยันค่าสูงสุด) | ต้องว่าง |
| 9 | I | วันที่สมัคร | `applicants` | `application_date` | Required before Evaluation | Parse ISO/Excel Date/เดือนภาษาไทย; ถ้า พ.ศ. ให้ลบ 543; timezone Asia/Bangkok; ต้อง Parse ได้และไม่กำกวม | ต้องว่าง |
| 10 | J | gpa | `applicants` | `gpa` | Required before Evaluation | ลบช่องว่าง; Decimal(3,2); 0.00–4.00 | ต้องว่าง |
| 11 | K | โทรศัพท์ | `applicants` | `phone` | Conditional | อ่านเป็น Text; ลบช่องว่าง/ขีด; Normalize 0XXXXXXXXX หรือ +66XXXXXXXXX; ^0\d{8,9}$ หรือ ^\+66\d{8,9}$; อย่างน้อย phone หรือ email | ต้องว่าง |
| 12 | L | อีเมล์ | `applicants` | `email` | Conditional | Trim; lowercase; รูปแบบอีเมลถูกต้อง; อย่างน้อย phone หรือ email | ต้องว่าง |
| 13 | M | ที่พัก | `applicants` | `residence_type` | Optional | Trim; Map กับ Code List; ค่าไม่รู้จักให้ Warning และเก็บ raw value เพื่อ Mapping | ต้องว่าง |
| 14 | N | ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ | `applicant_expenses` | `housing_cost_monthly` | Optional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0 | ต้องว่าง |
| 15 | O | ค่าใช้จ่ายส่วนตัว | `applicant_expenses` | `personal_expense_monthly` | Optional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0 | ต้องว่าง |
| 16 | P | ค่าอุปกรณ์การศึกษา | `applicant_expenses` | `education_equipment_expense` | Optional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0 | ต้องว่าง |
| 17 | Q | อุปกรณ์อิเล็กทรอนิกส์ที่มี | `applicant_expenses` | `electronic_devices` | Optional | Trim; เก็บเป็น Text; ความยาวไม่เกินค่าที่ระบบกำหนด | ต้องว่าง |
| 18 | R | รายได้เสริม | `applicants` | `supplementary_income_detail` | Optional | Trim; ค่าว่างหรือ '-' → NULL; ข้อความตามความยาวที่กำหนด | ต้องว่าง |
| 19 | S | บิดา อายุ | `parent_information` | `age (parent_type=FATHER)` | Optional | Integer; 15–120; ถ้าเสียชีวิตอาจว่างได้ | ต้องว่าง |
| 20 | T | บิดา อาชีพ | `parent_information` | `occupation (parent_type=FATHER)` | Optional | Trim; Map Code List เมื่อมี; ค่าไม่รู้จักให้ Warning | ต้องว่าง |
| 21 | U | บิดา รายได้ | `parent_information` | `monthly_income (parent_type=FATHER)` | Optional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0; หน่วยบาทต่อเดือน | ต้องว่าง |
| 22 | V | บิดา สภาพ | `parent_information` | `life_status (parent_type=FATHER)` | Optional | Trim; Map Code List; เช่น มีชีวิตอยู่/เสียชีวิต/ไม่ทราบ | ต้องว่าง |
| 23 | W | มารดา อายุ | `parent_information` | `age (parent_type=MOTHER)` | Optional | Integer; 15–120; ถ้าเสียชีวิตอาจว่างได้ | ต้องว่าง |
| 24 | X | มารดา อาชีพ | `parent_information` | `occupation (parent_type=MOTHER)` | Optional | Trim; Map Code List เมื่อมี; ค่าไม่รู้จักให้ Warning | ต้องว่าง |
| 25 | Y | มารดา รายได้ | `parent_information` | `monthly_income (parent_type=MOTHER)` | Optional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0; หน่วยบาทต่อเดือน | ต้องว่าง |
| 26 | Z | มารดา สภาพ | `parent_information` | `life_status (parent_type=MOTHER)` | Optional | Trim; Map Code List; เช่น มีชีวิตอยู่/เสียชีวิต/ไม่ทราบ | ต้องว่าง |
| 27 | AA | สภาพบิดา-มารดา | `education_support` | `parents_relationship_status` | Optional | Trim; Map Code List; ค่าไม่รู้จักให้ Warning | ต้องว่าง |
| 28 | AB | คนออกเงินเรียน | `education_support` | `tuition_payer` | Optional | Trim; Map Code List; เช่น บิดา-มารดา/ตนเอง/ญาติ/อื่น ๆ | ต้องว่าง |
| 29 | AC | อุปการะ-ความเกี่ยวข้อง | `education_support` | `supporter_relationship` | Conditional | Trim; Required เมื่อ tuition_payer เป็นบุคคลอื่น | ต้องว่าง |
| 30 | AD | อุปการะ-อาชีพ | `education_support` | `supporter_occupation` | Conditional | Trim; Required เมื่อมีข้อมูลผู้อุปการะ | ต้องว่าง |
| 31 | AE | อุปการะ-รายได้ | `education_support` | `supporter_monthly_income` | Conditional | ลบ comma/ช่องว่าง; Decimal(12,2); >= 0; Required เมื่อมีข้อมูลผู้อุปการะ; หน่วยบาทต่อเดือน | ต้องว่าง |
| 32 | AF | พี่น้อง-ทำงาน | `sibling_summaries` | `working_count` | Optional | Integer; >= 0 | ต้องว่าง |
| 33 | AG | พี่น้อง-ไม่ทำงาน | `sibling_summaries` | `not_working_count` | Optional | Integer; >= 0 | ต้องว่าง |
| 34 | AH | พี่น้อง-เรียน | `sibling_summaries` | `studying_count` | Optional | Integer; >= 0 | ต้องว่าง |
| 35 | AI | กยศ | `education_loan_histories` | `academic_year_be + amount` | Optional / Repeatable | Regex: ^\s*-?\s*(\d{4})\s*:\s*([0-9,]+(?:\.\d{1,2})?)\s*$; ลบ comma จาก amount; ปี พ.ศ. 4 หลัก; amount >= 0; ไม่ซ้ำ applicant+year | อนุญาต; สร้าง Child Record และสืบทอด student_id จาก Applicant Row ก่อนหน้า |
| 36 | AJ | ทุน | `scholarship_histories` | `academic_year_be + scholarship_name + amount` | Optional / Repeatable | Regex: ^\s*-?\s*(\d{4})\s+(.+?)\s*:\s*([0-9,]+(?:\.\d{1,2})?)\s*$; ปี/ชื่อทุน/จำนวนเงินต้องครบ; amount >= 0; ไม่ซ้ำ applicant+year+ชื่อทุน | อนุญาต; สร้าง Child Record และสืบทอด student_id จาก Applicant Row ก่อนหน้า |
| 37 | AK | พิกัดแผนที่บ้าน | `address_coordinates` | `latitude + longitude` | Conditional Pair | Split ด้วย comma; Trim; Decimal; ต้องมี 2 ค่า; latitude -90..90; longitude -180..180 | ต้องว่าง |

## 4. การ Parse ข้อมูลพิเศษ

### 4.1 วันที่สมัคร

- รูปแบบ Legacy: `09 ก.ค. 2569 13:36` → `2026-07-09T13:36:00+07:00`
- รองรับ ISO และ Excel Date/Serial เฉพาะรูปแบบที่ประกาศใน Test Case
- ปีที่มากกว่าเกณฑ์ พ.ศ. ให้แปลงด้วย `ปี ค.ศ. = ปี พ.ศ. - 543`
- วันที่กำกวมต้องเป็น `INVALID_DATE` ไม่ควรเดา

### 4.2 ประวัติ กยศ.

- รูปแบบ: `-2565 : 66,000`
- Regex: `^\s*-?\s*(\d{4})\s*:\s*([0-9,]+(?:\.\d{1,2})?)\s*$`
- ผลลัพธ์: `academic_year_be=2565`, `amount=66000.00`

### 4.3 ประวัติทุน

- รูปแบบ: `-2565 ทุนตัวอย่าง : 10,000`
- Regex: `^\s*-?\s*(\d{4})\s+(.+?)\s*:\s*([0-9,]+(?:\.\d{1,2})?)\s*$`
- ผลลัพธ์: `academic_year_be`, `scholarship_name`, `amount`

### 4.4 พิกัดบ้าน

- Split ด้วย comma และต้องได้ 2 ค่า
- `latitude` ต้องอยู่ในช่วง -90 ถึง 90
- `longitude` ต้องอยู่ในช่วง -180 ถึง 180
- มีเพียงค่าเดียวให้ใช้ `PARTIAL_COORDINATE`

## 5. Row Classification

| Row Type | Detection Rule | Result |
|---|---|---|
| `HEADER` | แถวแรกหรือแถวที่ผู้ใช้เลือกเป็น Header | ไม่สร้างข้อมูล |
| `APPLICANT` | student_id มีค่าหลัง Trim | สร้าง/เชื่อม Applicant และ Child Records |
| `CONTINUATION` | student_id ว่าง และมีค่าอย่างน้อยหนึ่งช่องใน กยศ/ทุน โดยคอลัมน์อื่นทั้งหมดว่าง | สร้าง Child History Records เท่านั้น |
| `BLANK` | ทุก Cell ว่าง/Whitespace หรือเป็น NULL | Skip |
| `INVALID` | ไม่เข้าเงื่อนไขด้านบน | Reject row |

## 6. Error Codes

| Code | Name | Severity | Condition | Action |
|---|---|---|---|---|
| `IMP-001` | `UNSUPPORTED_FILE_TYPE` | ERROR | Release 1 รับเฉพาะ `.xlsx`/`.csv`; `.xls` เป็น Optional / Out of Scope | Reject file |
| `IMP-002` | `FILE_READ_FAILED` | ERROR | ไม่สามารถอ่าน Workbook/CSV หรือไฟล์เสียหาย | Reject file |
| `IMP-003` | `HEADER_ROW_MISSING` | ERROR | ไม่พบแถวหัวคอลัมน์ | Reject file |
| `IMP-004` | `REQUIRED_HEADER_MISSING` | ERROR | ไม่พบหัวคอลัมน์ที่จำเป็นหลังใช้ Alias Mapping | Reject file |
| `IMP-005` | `DUPLICATE_HEADER` | ERROR | หัวคอลัมน์ซ้ำจน Mapping ไม่ชัดเจน | Reject file |
| `IMP-006` | `UNMAPPED_COLUMN` | WARNING | พบคอลัมน์ที่ระบบไม่รู้จัก | Ignore หลัง Preview หรือให้ผู้ใช้ Mapping |
| `IMP-007` | `REQUIRED_FIELD_MISSING` | ERROR | Hard Required ว่างหรือเป็น '-' | Reject row |
| `IMP-008` | `INVALID_STUDENT_ID` | ERROR | รหัสนักศึกษาไม่ตรงรูปแบบ ^\d{9}-\d$ | Reject row |
| `IMP-009` | `INVALID_STUDENT_ID` | ERROR | Excel แปลงรหัสเป็น Scientific Notation หรือสูญเสียเลขนำหน้า | Reject row |
| `IMP-010` | `DUPLICATE_STUDENT_IN_FILE` | ERROR | รหัสนักศึกษาซ้ำภายในไฟล์เดียวกัน | Reject duplicate Applicant Row |
| `IMP-011` | `DUPLICATE_STUDENT_IN_ROUND` | WARNING/CHOICE | มีผู้สมัครรหัสเดียวกันในรอบทุนแล้ว | Default Skip; Update เฉพาะผู้ดูแลเลือกและยังไม่มี Evaluation |
| `IMP-012` | `IMPORT_STATE_INVALID` | ERROR | พยายาม Update ผู้สมัครที่เริ่มมี Evaluation แล้ว | Block update |
| `IMP-013` | `INVALID_YEAR_LEVEL` | ERROR | ไม่ใช่จำนวนเต็มหรืออยู่นอกช่วงที่กำหนด | Reject field/row |
| `IMP-014` | `INVALID_GPA` | ERROR | ไม่ใช่ Decimal หรืออยู่นอกช่วง 0.00–4.00 | Reject field; block evaluation |
| `IMP-015` | `INVALID_DATE` | ERROR | ไม่สามารถ Parse หรือวันที่กำกวม | Reject/Warning ตาม Required Policy |
| `IMP-016` | `INVALID_PHONE` | ERROR | รูปแบบเบอร์ไม่ตรงรูปแบบที่ประกาศ | Reject field |
| `IMP-017` | `INVALID_EMAIL` | ERROR | รูปแบบอีเมลไม่ถูกต้อง | Reject field |
| `IMP-018` | `CONTACT_REQUIRED` | ERROR | ไม่มีทั้งโทรศัพท์และอีเมลเมื่อกฎบังคับใช้ | Reject row หรือ block evaluation |
| `IMP-019` | `INVALID_NUMBER` | ERROR | ค่าไม่สามารถแปลงเป็น Integer/Decimal | Reject field/row |
| `IMP-020` | `NEGATIVE_AMOUNT` | ERROR | จำนวนเงินติดลบ | Reject field/row |
| `IMP-021` | `INVALID_PARENT_AGE` | ERROR | อายุไม่ใช่จำนวนเต็มหรืออยู่นอก 15–120 | Reject field |
| `IMP-022` | `INCOMPLETE_SUPPORTER_DATA` | ERROR | มีข้อมูลผู้อุปการะบางส่วนแต่ไม่ครบตามเงื่อนไข | Reject related fields |
| `IMP-023` | `VALIDATION_ERROR` | ERROR | รูปแบบประวัติ กยศ. ไม่ตรง -YYYY : amount | Reject history record |
| `IMP-024` | `DUPLICATE_LOAN_HISTORY` | ERROR | ประวัติ กยศ. ปีเดียวกันซ้ำสำหรับผู้สมัคร | Reject duplicate history |
| `IMP-025` | `VALIDATION_ERROR` | ERROR | รูปแบบประวัติทุนไม่ตรง -YYYY ชื่อทุน : amount | Reject history record |
| `IMP-026` | `DUPLICATE_SCHOLARSHIP_HISTORY` | ERROR | ปีและชื่อทุนซ้ำสำหรับผู้สมัคร | Reject duplicate history |
| `IMP-027` | `INVALID_COORDINATE` | ERROR | ไม่ใช่เลข 2 ค่า หรืออยู่นอกช่วง lat/lon | Reject coordinate |
| `IMP-028` | `PARTIAL_COORDINATE` | ERROR | มี latitude หรือ longitude เพียงค่าเดียว | Reject coordinate |
| `IMP-029` | `ORPHAN_CONTINUATION_ROW` | ERROR | แถวต่อเนื่องไม่มี Applicant Row ก่อนหน้าที่ใช้ได้ | Reject row |
| `IMP-030` | `VALIDATION_ERROR` | ERROR | แถวไม่มีรหัสแต่มีข้อมูลในคอลัมน์อื่นนอกจาก กยศ./ทุน | Reject row |
| `IMP-031` | `EMPTY_CONTINUATION_ROW` | ERROR | แถวไม่มีรหัสและไม่มี กยศ./ทุน | Classify เป็น Blank หรือ Invalid |
| `IMP-032` | `UNKNOWN_REFERENCE_VALUE` | WARNING | ค่าคณะ/สาขา/สถานะ/ผู้จ่ายไม่ตรง Reference Value | ให้ผู้ใช้ Mapping หรือยืนยันเก็บ raw value |
| `IMP-033` | `EMPTY_ROW_SKIPPED` | INFO | แถวว่างทั้งหมด | Skip และนับใน Audit |
| `IMP-034` | `IMPORT_STATE_INVALID` | ERROR | สถานะ Batch หรือข้อมูลปลายทางไม่อนุญาตให้ commit Transaction | Rollback batch |

## 7. Import Flow

1. **Upload** — รับไฟล์ Excel/CSV และ round_id ที่ผู้ดูแลเลือก
   Audit/Constraint: import_batches: file_name, file_hash, uploaded_by, round_id
2. **Read & Detect** — อ่าน Sheet/Encoding/Header และสร้าง raw row index
   Audit/Constraint: ห้ามแปลง Identifier เป็น Number
3. **Header Mapping** — จับคู่หัวคอลัมน์ด้วยชื่อจริงและ Alias; ผู้ใช้แก้ Mapping ได้
   Audit/Constraint: ต้องผ่าน Required Header validation
4. **Row Classification** — จำแนก APPLICANT / CONTINUATION / BLANK / INVALID
   Audit/Constraint: ใช้กฎใน Sheet 03_ROW_RULES
5. **Normalization** — Trim, NULL normalization, Date/Number parsing, Code List mapping
   Audit/Constraint: เก็บ raw_value และ normalized_value
6. **Validation** — ตรวจ Field, Row, Cross-row, Duplicate ในไฟล์และฐานข้อมูล
   Audit/Constraint: สร้าง messages {field, code, severity, message}
7. **Preview** — แสดงเลขแถว ค่าหลังแปลง ผู้สมัครเจ้าของ Continuation และ Error/Warning
   Audit/Constraint: ยังไม่เขียนข้อมูลจริง
8. **Confirm Policy** — ผู้ดูแลเลือก Skip/Update สำหรับ Duplicate ที่อนุญาต
   Audit/Constraint: Update ได้เฉพาะก่อนมี Evaluation
9. **Transactional Import** — บันทึก Applicant และ Child Records ภายใน Transaction
   Audit/Constraint: Error ระดับ Batch → Rollback
10. **Audit Result** — บันทึกจำนวน total/valid/warning/error/skipped/imported และรายละเอียด
   Audit/Constraint: รองรับตรวจสอบย้อนหลัง/Export Error Report

## 8. Minimum Test Cases

| Test ID | Scenario | Expected Result |
|---|---|---|
| `TC-IMP-001` | Applicant Row ถูกต้อง — รหัสและ Hard Required ครบ; วันที่ไทย; พิกัดครบคู่ | VALID และแสดง normalized payload |
| `TC-IMP-002` | Missing Hard Required — ไม่มีชื่อหรือสาขา | REQUIRED_FIELD_MISSING; Reject row |
| `TC-IMP-003` | Invalid student ID — 6630406648 หรือ 6.6304E+09 | INVALID_STUDENT_ID |
| `TC-IMP-004` | Thai Buddhist date — 09 ก.ค. 2569 13:36 | 2026-07-09T13:36:00+07:00 |
| `TC-IMP-005` | Invalid GPA — 4.50 | INVALID_GPA |
| `TC-IMP-006` | Duplicate in same file — Applicant Row รหัสเดิม 2 แถว | DUPLICATE_STUDENT_IN_FILE |
| `TC-IMP-007` | Valid continuation loan — รหัสว่าง; กยศ=-2566 : 66,000; ช่องอื่นว่าง | CONTINUATION; ผูกกับ Applicant ก่อนหน้า |
| `TC-IMP-008` | Orphan continuation — แถวข้อมูลแรกมีเฉพาะทุน | ORPHAN_CONTINUATION_ROW |
| `TC-IMP-009` | Continuation has other data — รหัสว่าง; มี กยศ และพิกัด | VALIDATION_ERROR |
| `TC-IMP-010` | Invalid loan syntax — 2565 66000 | VALIDATION_ERROR |
| `TC-IMP-011` | Valid scholarship syntax — -2565 ทุนตัวอย่าง : 10,000 | สร้าง scholarship_history 1 รายการ |
| `TC-IMP-012` | Coordinate out of range — 95, 104.3 | INVALID_COORDINATE |
| `TC-IMP-013` | Blank row — ทุก Cell ว่าง | EMPTY_ROW_SKIPPED; ไม่สร้างข้อมูล |
| `TC-IMP-014` | Duplicate in database, no evaluation — พบ applicant เดิมใน round | Default Skip; Admin เลือก Update ได้ |
| `TC-IMP-015` | Duplicate in database, has evaluation — พบ applicant เดิมและมี Evaluation | IMPORT_STATE_INVALID |

## 9. Historical open decisions resolved for the baseline candidate

| Decision ID | ประเด็น | ข้อเสนอปัจจุบัน | Owner | Status |
|---|---|---|---|---|
| RD-015 | Business Key | `round_id + scholarship_type_id + student_id` | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |
| RD-017 | Legacy Continuation Row | UAT and first production transition round only | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |
| RD-018 | Duplicate policy | file duplicate Error; DB duplicate Skip; explicit update before Evaluation; never auto-Upsert | งานทุน | Confirmed Response — Pending Formal Record |
| RD-019/RD-028 | Required levels | Hard Import / Required Before Evaluation / Optional | งานทุน/ผู้ประเมิน | Confirmed Response — Pending Formal Record |
| RD-020 | Date/phone normalization | ISO new; declared legacy formats normalized in Preview; blank/`-`→NULL and zero preserved | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |
| DD-OD-003 | ค่าอุปกรณ์การศึกษา | ต่อภาคการศึกษา; store period/unit | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-005 | Reference Values | versioned DB Code Lists, never frontend hardcode | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-009 | ประวัติ กยศ./ทุน | Snapshot per application/round | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |

## 10. Acceptance Criteria

- ระบบอ่านและจับคู่หัวคอลัมน์ทั้ง 37 คอลัมน์ได้ รวม Alias `ชือ`/`ชื่อ`
- ระบบแสดง Source Row Number, Raw Value, Normalized Value, Error Code และ Severity ใน Preview
- ระบบแสดงว่า Continuation Row ถูกผูกกับนักศึกษาคนใดก่อน Confirm
- ไม่มีข้อมูลจริงถูกเขียนลงฐานข้อมูลก่อนผู้ดูแลกดยืนยัน
- หากสถานะไม่อนุญาตให้ commit Transaction ต้อง Rollback และบันทึก `IMPORT_STATE_INVALID`
- Import History ต้องมีชื่อไฟล์ ผู้นำเข้า รอบทุน เวลา จำนวนแถว และสรุป Valid/Warning/Error/Skipped/Imported

## แหล่งอ้างอิง

- [`Data_import_to_web.xlsx`](./Data_import_to_web.xlsx)
- [`SEMS-project-proposal.pdf`](../../Requirements/Proposal/SEMS-project-proposal.pdf)
- `SEMS_Data_Dictionary.xlsx`
- [`SEMS_Requirement_Decision_Analysis.md`](../../Requirements/SEMS_Requirement_Decision_Analysis.md)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Design Team | Replaced import-specific aliases with canonical allowed codes while retaining detailed validation reasons. |
| v0.2 | 2026-07-23 | SEMS Design Team | Limited Release 1 import to `.xlsx`/`.csv` and aligned canonical file-type error code. |
| v0.1 | 2026-07-23 | SEMS Design Team | Initial applicant import mapping draft. |
