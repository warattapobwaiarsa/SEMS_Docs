# 02 DATA DICTIONARY

| Metadata | Value |
| :--- | :--- |
| Version | **v1.0** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `02_DATA_DICTIONARY`

## `import_batches.id`

- **ชื่อภาษาไทย:** รหัสชุดนำเข้า
- **คำอธิบาย:** Primary Key ของการนำเข้าหนึ่งครั้ง
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** ต้องเป็น UUID
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** Confirmed design

## `import_batches.round_id`

- **ชื่อภาษาไทย:** รอบทุน
- **คำอธิบาย:** รอบทุนปลายทางที่ผู้ดูแลเลือกก่อนนำเข้า
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** เลือกจากหน้าจอ
- **Validation / Allowed Values:** ต้องอ้างถึงรอบทุนที่อนุญาตให้นำเข้า
- **Unique / Index:** INDEX, FK
- **PII Classification:** None
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** ไม่อ่านจากทุกแถวในไฟล์

## `import_batches.file_name`

- **ชื่อภาษาไทย:** ชื่อไฟล์ต้นทาง
- **คำอธิบาย:** ชื่อไฟล์ Excel/CSV ที่นำเข้า
- **PostgreSQL Type:** VARCHAR(255)
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** ชื่อไฟล์อัปโหลด
- **Validation / Allowed Values:** นามสกุลที่ระบบรองรับ
- **Unique / Index:** -
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `import_batches.file_hash`

- **ชื่อภาษาไทย:** ค่าแฮชไฟล์
- **คำอธิบาย:** ใช้ตรวจสอบไฟล์ซ้ำและ Audit
- **PostgreSQL Type:** VARCHAR(64)
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** SHA-256
- **Validation / Allowed Values:** รูปแบบ hexadecimal 64 ตัวอักษร
- **Unique / Index:** INDEX
- **PII Classification:** None
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** แนะนำ

## `import_batches.imported_by_user_id`

- **ชื่อภาษาไทย:** ผู้นำเข้า
- **คำอธิบาย:** ผู้ดูแลระบบที่ดำเนินการ
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** Session user
- **Validation / Allowed Values:** ต้องมีสิทธิ์ Import
- **Unique / Index:** INDEX, FK
- **PII Classification:** Identity
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `import_batches.imported_at`

- **ชื่อภาษาไทย:** เวลานำเข้า
- **คำอธิบาย:** วันเวลาที่เริ่มหรือยืนยันนำเข้า
- **PostgreSQL Type:** TIMESTAMPTZ
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** now()
- **Validation / Allowed Values:** เก็บ Time zone
- **Unique / Index:** INDEX
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `import_batches.status`

- **ชื่อภาษาไทย:** สถานะชุดนำเข้า
- **คำอธิบาย:** สถานะ Preview/Validated/Imported/Failed
- **PostgreSQL Type:** VARCHAR(30)
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** PREVIEW
- **Validation / Allowed Values:** PREVIEW, VALIDATED, IMPORTED, FAILED, CANCELLED
- **Unique / Index:** INDEX
- **PII Classification:** None
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `import_batches.summary_json`

- **ชื่อภาษาไทย:** สรุปผลนำเข้า
- **คำอธิบาย:** จำนวน Inserted/Updated/Skipped/Failed และรายละเอียดรวม
- **PostgreSQL Type:** JSONB
- **Required Level:** System
- **Nullable:** Yes
- **Default / Source:** NULL
- **Validation / Allowed Values:** ต้องตรงกับผลรายแถว
- **Unique / Index:** -
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `import_rows.id`

- **ชื่อภาษาไทย:** รหัสแถวนำเข้า
- **คำอธิบาย:** Primary Key ของข้อมูลต้นทางรายแถว
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** ต้องเป็น UUID
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `import_rows.import_batch_id`

- **ชื่อภาษาไทย:** ชุดนำเข้า
- **คำอธิบาย:** เชื่อมกับ import_batches
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** -
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** INDEX, FK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `import_rows.sheet_name`

- **ชื่อภาษาไทย:** ชื่อชีต
- **คำอธิบาย:** ชื่อ Sheet ที่อ่านข้อมูล
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** ชื่อ Sheet
- **Validation / Allowed Values:** ห้ามว่าง
- **Unique / Index:** -
- **PII Classification:** Operational
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `import_rows.source_row_number`

- **ชื่อภาษาไทย:** เลขแถวต้นทาง
- **คำอธิบาย:** เลขแถวใน Excel/CSV สำหรับแจ้ง Error
- **PostgreSQL Type:** INTEGER
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** เลขแถวจริง
- **Validation / Allowed Values:** > 0
- **Unique / Index:** INDEX
- **PII Classification:** None
- **Source Column:** ลำดับแถว
- **สถานะ / หมายเหตุ:** -

## `import_rows.row_type`

- **ชื่อภาษาไทย:** ประเภทแถว
- **คำอธิบาย:** APPLICANT, CONTINUATION หรือ EMPTY
- **PostgreSQL Type:** VARCHAR(20)
- **Required Level:** System/Derived
- **Nullable:** No
- **Default / Source:** Derived
- **Validation / Allowed Values:** APPLICANT, CONTINUATION, EMPTY
- **Unique / Index:** INDEX
- **PII Classification:** None
- **Source Column:** [Derived]
- **สถานะ / หมายเหตุ:** Continuation Row ใช้เฉพาะ Legacy Import

## `import_rows.resolved_student_id`

- **ชื่อภาษาไทย:** รหัสนักศึกษาที่ระบุได้
- **คำอธิบาย:** รหัสจากแถวปัจจุบันหรือผู้สมัครแถวก่อนหน้า
- **PostgreSQL Type:** VARCHAR(30)
- **Required Level:** Derived
- **Nullable:** Yes
- **Default / Source:** รหัส / Fill-down context
- **Validation / Allowed Values:** ห้ามว่างสำหรับ APPLICANT และ CONTINUATION ที่จะนำเข้า
- **Unique / Index:** INDEX
- **PII Classification:** Direct Identifier
- **Source Column:** รหัส
- **สถานะ / หมายเหตุ:** -

## `import_rows.raw_payload`

- **ชื่อภาษาไทย:** ข้อมูลดิบ
- **คำอธิบาย:** ค่าทุกคอลัมน์ก่อน Normalize
- **PostgreSQL Type:** JSONB
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** ค่าจากไฟล์
- **Validation / Allowed Values:** เก็บตาม Header ต้นทาง
- **Unique / Index:** -
- **PII Classification:** Contains PII
- **Source Column:** ทุกคอลัมน์
- **สถานะ / หมายเหตุ:** จำกัดสิทธิ์การอ่าน

## `import_rows.validation_status`

- **ชื่อภาษาไทย:** ผลตรวจสอบ
- **คำอธิบาย:** VALID, WARNING หรือ ERROR
- **PostgreSQL Type:** VARCHAR(20)
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** Derived
- **Validation / Allowed Values:** VALID, WARNING, ERROR
- **Unique / Index:** INDEX
- **PII Classification:** None
- **Source Column:** [Derived]
- **สถานะ / หมายเหตุ:** -

## `import_rows.validation_messages`

- **ชื่อภาษาไทย:** รายการปัญหา
- **คำอธิบาย:** รหัสกฎและรายละเอียด Warning/Error
- **PostgreSQL Type:** JSONB
- **Required Level:** System
- **Nullable:** Yes
- **Default / Source:** NULL
- **Validation / Allowed Values:** ต้องมีเมื่อ status ไม่ใช่ VALID
- **Unique / Index:** -
- **PII Classification:** Contains PII
- **Source Column:** [Derived]
- **สถานะ / หมายเหตุ:** -

## `applicants.id`

- **ชื่อภาษาไทย:** รหัสผู้สมัครภายใน
- **คำอธิบาย:** Primary Key ทางเทคนิค
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** ต้องเป็น UUID
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `applicants.student_id`

- **ชื่อภาษาไทย:** รหัสนักศึกษา
- **คำอธิบาย:** Business Identifier ของนักศึกษา
- **PostgreSQL Type:** VARCHAR(30)
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Trim จากไฟล์
- **Validation / Allowed Values:** เก็บเป็น Text; ห้าม Scientific Notation; รองรับรูปแบบมาตรฐานและ documented legacy normalization ตาม RD-020/Q-030
- **Unique / Index:** UNIQUE, INDEX
- **PII Classification:** Direct Identifier
- **Source Column:** รหัส
- **สถานะ / หมายเหตุ:** Business Key ระดับบุคคล

## `applicants.title`

- **ชื่อภาษาไทย:** คำนำหน้า
- **คำอธิบาย:** คำนำหน้าชื่อ
- **PostgreSQL Type:** VARCHAR(30)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** ใช้ Reference Value ที่อนุมัติ
- **Unique / Index:** -
- **PII Classification:** Identity
- **Source Column:** คำนำหน้า
- **สถานะ / หมายเหตุ:** -

## `applicants.first_name`

- **ชื่อภาษาไทย:** ชื่อ
- **คำอธิบาย:** ชื่อจริงของผู้สมัคร
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามเป็นค่าว่างหรือ '-'
- **Unique / Index:** INDEX
- **PII Classification:** Direct Identifier
- **Source Column:** ชือ / ชื่อ
- **สถานะ / หมายเหตุ:** รองรับ Header เดิมที่สะกดผิด

## `applicants.last_name`

- **ชื่อภาษาไทย:** นามสกุล
- **คำอธิบาย:** นามสกุลของผู้สมัคร
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามเป็นค่าว่างหรือ '-'
- **Unique / Index:** INDEX
- **PII Classification:** Direct Identifier
- **Source Column:** สกุล
- **สถานะ / หมายเหตุ:** -

## `applicants.phone`

- **ชื่อภาษาไทย:** โทรศัพท์
- **คำอธิบาย:** หมายเลขโทรศัพท์สำหรับติดต่อ
- **PostgreSQL Type:** VARCHAR(20)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Normalize digits
- **Validation / Allowed Values:** เก็บเป็น Text; 9–15 หลัก; Scientific Notation เป็น Error
- **Unique / Index:** -
- **PII Classification:** Contact
- **Source Column:** โทรศัพท์
- **สถานะ / หมายเหตุ:** ห้ามแปลงเป็น Number

## `applicants.email`

- **ชื่อภาษาไทย:** อีเมล
- **คำอธิบาย:** อีเมลผู้สมัคร
- **PostgreSQL Type:** VARCHAR(254)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Lowercase + Trim
- **Validation / Allowed Values:** ตรวจรูปแบบอีเมล
- **Unique / Index:** INDEX
- **PII Classification:** Contact
- **Source Column:** อีเมล์ / อีเมล
- **สถานะ / หมายเหตุ:** -

## Historical draft field: `applicants.citizen_id_encrypted`

- **Release 1 status:** `Out of Scope for Release 1 — requires separate lawful-need and security approval`
- **Confirmed rule:** no column, import mapping, UI, export, log or test value is implemented for national ID in the Release 1 Core Schema.
- **Traceability:** RD-016 and RD-029 supersede the former optional-field proposal while preserving this historical note.

## `round_applications.id`

- **ชื่อภาษาไทย:** รหัสใบสมัครรอบทุน
- **คำอธิบาย:** Primary Key ของผู้สมัครในรอบทุน
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** ต้องเป็น UUID
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `round_applications.round_id`

- **ชื่อภาษาไทย:** รอบทุน
- **คำอธิบาย:** รอบทุนที่ผู้สมัครสังกัด
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** เลือกก่อน Import
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** UNIQUE with applicant_id, FK
- **PII Classification:** None
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `round_applications.applicant_id`

- **ชื่อภาษาไทย:** ผู้สมัคร
- **คำอธิบาย:** เชื่อมกับ applicants
- **PostgreSQL Type:** UUID
- **Required Level:** System/Resolved
- **Nullable:** No
- **Default / Source:** Resolve จาก student_id
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** UNIQUE with round_id, FK
- **PII Classification:** Identity
- **Source Column:** รหัส
- **สถานะ / หมายเหตุ:** -

## `round_applications.source_sequence`

- **ชื่อภาษาไทย:** ลำดับจากไฟล์
- **คำอธิบาย:** ลำดับที่แสดงในไฟล์ต้นทาง
- **PostgreSQL Type:** INTEGER
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** >= 1
- **Unique / Index:** -
- **PII Classification:** None
- **Source Column:** ลำดับ
- **สถานะ / หมายเหตุ:** ไม่ใช้เป็น Key

## `round_applications.applied_at`

- **ชื่อภาษาไทย:** วันที่สมัคร
- **คำอธิบาย:** วันเวลาที่ผู้สมัครส่งใบสมัคร
- **PostgreSQL Type:** TIMESTAMPTZ
- **Required Level:** Recommended
- **Nullable:** Yes
- **Default / Source:** Parse เป็น Asia/Bangkok
- **Validation / Allowed Values:** รองรับรูปแบบที่ประกาศ; ค่ากำกวมเป็น Error
- **Unique / Index:** INDEX
- **PII Classification:** Operational
- **Source Column:** วันที่สมัคร
- **สถานะ / หมายเหตุ:** Required before Evaluation ตาม RD-019/Q-025–Q-026

## `round_applications.faculty_name_snapshot`

- **ชื่อภาษาไทย:** คณะ
- **คำอธิบาย:** ชื่อคณะ ณ รอบทุนนี้
- **PostgreSQL Type:** VARCHAR(150)
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามว่าง
- **Unique / Index:** INDEX
- **PII Classification:** Academic
- **Source Column:** คณะ
- **สถานะ / หมายเหตุ:** -

## `round_applications.major_name_snapshot`

- **ชื่อภาษาไทย:** สาขา
- **คำอธิบาย:** ชื่อสาขา ณ รอบทุนนี้
- **PostgreSQL Type:** VARCHAR(150)
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามว่าง
- **Unique / Index:** INDEX
- **PII Classification:** Academic
- **Source Column:** สาขา
- **สถานะ / หมายเหตุ:** -

## `round_applications.year_level`

- **ชื่อภาษาไทย:** ชั้นปี
- **คำอธิบาย:** ชั้นปี ณ วันที่สมัคร
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Hard Required
- **Nullable:** No
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** 1–8 หรือช่วงที่งานทุนยืนยัน
- **Unique / Index:** INDEX
- **PII Classification:** Academic
- **Source Column:** ชั้นปี
- **สถานะ / หมายเหตุ:** -

## `round_applications.gpa`

- **ชื่อภาษาไทย:** เกรดเฉลี่ย
- **คำอธิบาย:** GPA ที่ใช้ประกอบการประเมิน
- **PostgreSQL Type:** NUMERIC(4,2)
- **Required Level:** Required before Evaluation
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** 0.00–4.00
- **Unique / Index:** INDEX
- **PII Classification:** Academic
- **Source Column:** gpa / GPA
- **สถานะ / หมายเหตุ:** -

## `round_applications.residence_type`

- **ชื่อภาษาไทย:** ประเภทที่พัก
- **คำอธิบาย:** รูปแบบที่พักของผู้สมัคร
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** Reference Value หรือ Free text ตามข้อสรุป
- **Unique / Index:** -
- **PII Classification:** Personal Circumstance
- **Source Column:** ที่พัก
- **สถานะ / หมายเหตุ:** -

## `round_applications.housing_monthly_cost`

- **ชื่อภาษาไทย:** ค่าเช่าหอ/บ้านรวมค่าน้ำไฟ
- **คำอธิบาย:** ค่าใช้จ่ายที่พักต่อเดือน
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** >= 0; '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ
- **สถานะ / หมายเหตุ:** -

## `round_applications.personal_monthly_cost`

- **ชื่อภาษาไทย:** ค่าใช้จ่ายส่วนตัว
- **คำอธิบาย:** ค่าใช้จ่ายส่วนตัวต่อเดือน
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** >= 0; '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** ค่าใช้จ่ายส่วนตัว
- **สถานะ / หมายเหตุ:** -

## `round_applications.education_material_cost`

- **ชื่อภาษาไทย:** ค่าอุปกรณ์การศึกษา
- **คำอธิบาย:** ค่าอุปกรณ์การศึกษา
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** >= 0; period = `SEMESTER`
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** ค่าอุปกรณ์การศึกษา
- **สถานะ / หมายเหตุ:** Confirmed Response — ต่อภาคการศึกษา

## `round_applications.electronic_devices`

- **ชื่อภาษาไทย:** อุปกรณ์อิเล็กทรอนิกส์
- **คำอธิบาย:** รายการอุปกรณ์ที่ผู้สมัครมี
- **PostgreSQL Type:** TEXT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Personal Circumstance
- **Source Column:** อุปกรณ์อิเล็กทรอนิกส์ที่มี
- **สถานะ / หมายเหตุ:** -

## `round_applications.additional_income_description`

- **ชื่อภาษาไทย:** รายละเอียดรายได้เสริม
- **คำอธิบาย:** ข้อความจากไฟล์เกี่ยวกับรายได้เสริม
- **PostgreSQL Type:** TEXT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** รายได้เสริม
- **สถานะ / หมายเหตุ:** -

## `round_applications.has_additional_income`

- **ชื่อภาษาไทย:** มีรายได้เสริม
- **คำอธิบาย:** Boolean ที่อนุมานจากข้อความ
- **PostgreSQL Type:** BOOLEAN
- **Required Level:** Derived
- **Nullable:** Yes
- **Default / Source:** Derived
- **Validation / Allowed Values:** ไม่มีรายได้เสริม=false; ข้อความอื่น=true; ว่าง=NULL
- **Unique / Index:** INDEX
- **PII Classification:** Financial Sensitive
- **Source Column:** รายได้เสริม
- **สถานะ / หมายเหตุ:** เก็บทั้งค่าดิบและ Boolean

## `round_applications.parents_household_status`

- **ชื่อภาษาไทย:** สภาพบิดา-มารดา
- **คำอธิบาย:** สถานะครอบครัวหรือการอยู่อาศัยของบิดามารดา
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** Reference Value รอยืนยัน
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** สภาพบิดา-มารดา
- **สถานะ / หมายเหตุ:** -

## `round_applications.education_funder`

- **ชื่อภาษาไทย:** ผู้รับผิดชอบค่าเรียน
- **คำอธิบาย:** บุคคลหรือแหล่งที่ออกเงินเรียน
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** Reference Value รอยืนยัน
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** คนออกเงินเรียน
- **สถานะ / หมายเหตุ:** -

## `round_applications.siblings_working_count`

- **ชื่อภาษาไทย:** พี่น้องที่ทำงาน
- **คำอธิบาย:** จำนวนพี่น้องที่ทำงาน
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** >= 0
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** พี่น้อง-ทำงาน
- **สถานะ / หมายเหตุ:** -

## `round_applications.siblings_not_working_count`

- **ชื่อภาษาไทย:** พี่น้องที่ไม่ทำงาน
- **คำอธิบาย:** จำนวนพี่น้องที่ไม่ทำงาน
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** >= 0
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** พี่น้อง-ไม่ทำงาน
- **สถานะ / หมายเหตุ:** -

## `round_applications.siblings_studying_count`

- **ชื่อภาษาไทย:** พี่น้องที่กำลังเรียน
- **คำอธิบาย:** จำนวนพี่น้องที่กำลังศึกษา
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** >= 0
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** พี่น้อง-เรียน
- **สถานะ / หมายเหตุ:** -

## `round_applications.home_location_raw`

- **ชื่อภาษาไทย:** พิกัด/ลิงก์บ้านต้นฉบับ
- **คำอธิบาย:** ค่าพิกัดหรือลิงก์ที่อ่านจากไฟล์
- **PostgreSQL Type:** TEXT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Location Sensitive
- **Source Column:** พิกัดแผนที่บ้าน
- **สถานะ / หมายเหตุ:** จำกัดสิทธิ์

## `round_applications.home_map_url`

- **ชื่อภาษาไทย:** ลิงก์แผนที่บ้าน
- **คำอธิบาย:** URL แผนที่เมื่อค่าต้นทางเป็น URL
- **PostgreSQL Type:** TEXT
- **Required Level:** Derived
- **Nullable:** Yes
- **Default / Source:** Derived
- **Validation / Allowed Values:** ตรวจ URL scheme/domain
- **Unique / Index:** -
- **PII Classification:** Location Sensitive
- **Source Column:** พิกัดแผนที่บ้าน
- **สถานะ / หมายเหตุ:** -

## `round_applications.home_latitude`

- **ชื่อภาษาไทย:** ละติจูดบ้าน
- **คำอธิบาย:** ละติจูดเมื่อแยกพิกัดได้
- **PostgreSQL Type:** NUMERIC(10,7)
- **Required Level:** Derived
- **Nullable:** Yes
- **Default / Source:** Derived
- **Validation / Allowed Values:** -90 ถึง 90
- **Unique / Index:** -
- **PII Classification:** Location Sensitive
- **Source Column:** พิกัดแผนที่บ้าน
- **สถานะ / หมายเหตุ:** -

## `round_applications.home_longitude`

- **ชื่อภาษาไทย:** ลองจิจูดบ้าน
- **คำอธิบาย:** ลองจิจูดเมื่อแยกพิกัดได้
- **PostgreSQL Type:** NUMERIC(10,7)
- **Required Level:** Derived
- **Nullable:** Yes
- **Default / Source:** Derived
- **Validation / Allowed Values:** -180 ถึง 180
- **Unique / Index:** -
- **PII Classification:** Location Sensitive
- **Source Column:** พิกัดแผนที่บ้าน
- **สถานะ / หมายเหตุ:** -

## `round_applications.import_batch_id`

- **ชื่อภาษาไทย:** ชุดนำเข้าต้นทาง
- **คำอธิบาย:** อ้างอิงการนำเข้าที่สร้างข้อมูล
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** Current batch
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** INDEX, FK
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `round_applications.created_at`

- **ชื่อภาษาไทย:** เวลาสร้าง
- **คำอธิบาย:** เวลาที่สร้างข้อมูล
- **PostgreSQL Type:** TIMESTAMPTZ
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** now()
- **Validation / Allowed Values:** -
- **Unique / Index:** -
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `round_applications.updated_at`

- **ชื่อภาษาไทย:** เวลาแก้ไขล่าสุด
- **คำอธิบาย:** เวลาที่ข้อมูลเปลี่ยนล่าสุด
- **PostgreSQL Type:** TIMESTAMPTZ
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** now()
- **Validation / Allowed Values:** -
- **Unique / Index:** -
- **PII Classification:** Operational
- **Source Column:** [System-supplied]
- **สถานะ / หมายเหตุ:** -

## `application_parents.id`

- **ชื่อภาษาไทย:** รหัสข้อมูลผู้ปกครอง
- **คำอธิบาย:** Primary Key
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** -
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `application_parents.application_id`

- **ชื่อภาษาไทย:** ใบสมัครรอบทุน
- **คำอธิบาย:** เชื่อมกับ round_applications
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** -
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** UNIQUE with parent_type, FK
- **PII Classification:** Identity
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `application_parents.parent_type`

- **ชื่อภาษาไทย:** ประเภทผู้ปกครอง
- **คำอธิบาย:** บิดาหรือมารดา
- **PostgreSQL Type:** VARCHAR(10)
- **Required Level:** Required if row exists
- **Nullable:** No
- **Default / Source:** FATHER/MOTHER
- **Validation / Allowed Values:** FATHER, MOTHER
- **Unique / Index:** UNIQUE with application_id
- **PII Classification:** Family Sensitive
- **Source Column:** [Derived by source column]
- **สถานะ / หมายเหตุ:** -

## `application_parents.age`

- **ชื่อภาษาไทย:** อายุ
- **คำอธิบาย:** อายุของบิดาหรือมารดา
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse integer
- **Validation / Allowed Values:** 0–120; '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** บิดา อายุ / มารดา อายุ
- **สถานะ / หมายเหตุ:** -

## `application_parents.occupation`

- **ชื่อภาษาไทย:** อาชีพ
- **คำอธิบาย:** อาชีพของบิดาหรือมารดา
- **PostgreSQL Type:** VARCHAR(150)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** บิดา อาชีพ / มารดา อาชีพ
- **สถานะ / หมายเหตุ:** -

## `application_parents.monthly_income`

- **ชื่อภาษาไทย:** รายได้ต่อเดือน
- **คำอธิบาย:** รายได้ของบิดาหรือมารดา
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** >= 0; ว่างไม่เท่ากับ 0
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** บิดา รายได้ / มารดา รายได้
- **สถานะ / หมายเหตุ:** -

## `application_parents.life_status`

- **ชื่อภาษาไทย:** สถานะการมีชีวิต
- **คำอธิบาย:** สถานะของบิดาหรือมารดา
- **PostgreSQL Type:** VARCHAR(20)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Map reference
- **Validation / Allowed Values:** ALIVE, DECEASED, UNKNOWN
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** บิดา สภาพ / มารดา สภาพ
- **สถานะ / หมายเหตุ:** เก็บ raw_value ใน Import Row

## `application_guardians.id`

- **ชื่อภาษาไทย:** รหัสผู้อุปการะ
- **คำอธิบาย:** Primary Key
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** -
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `application_guardians.application_id`

- **ชื่อภาษาไทย:** ใบสมัครรอบทุน
- **คำอธิบาย:** เชื่อมกับ round_applications
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** -
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** INDEX, FK
- **PII Classification:** Identity
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `application_guardians.relationship`

- **ชื่อภาษาไทย:** ความเกี่ยวข้อง
- **คำอธิบาย:** ความสัมพันธ์ระหว่างผู้อุปการะกับผู้สมัคร
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** อุปการะ-ความเกี่ยวข้อง
- **สถานะ / หมายเหตุ:** -

## `application_guardians.occupation`

- **ชื่อภาษาไทย:** อาชีพผู้อุปการะ
- **คำอธิบาย:** อาชีพของผู้อุปการะ
- **PostgreSQL Type:** VARCHAR(150)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Trim
- **Validation / Allowed Values:** '-' เป็น NULL
- **Unique / Index:** -
- **PII Classification:** Family Sensitive
- **Source Column:** อุปการะ-อาชีพ
- **สถานะ / หมายเหตุ:** -

## `application_guardians.monthly_income`

- **ชื่อภาษาไทย:** รายได้ผู้อุปการะ
- **คำอธิบาย:** รายได้ต่อเดือนของผู้อุปการะ
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse decimal
- **Validation / Allowed Values:** >= 0; ว่างไม่เท่ากับ 0
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** อุปการะ-รายได้
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.id`

- **ชื่อภาษาไทย:** รหัสประวัติ กยศ.
- **คำอธิบาย:** Primary Key
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** -
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.applicant_id`

- **ชื่อภาษาไทย:** ผู้สมัคร
- **คำอธิบาย:** เชื่อมกับ applicants
- **PostgreSQL Type:** UUID
- **Required Level:** Resolved
- **Nullable:** No
- **Default / Source:** Resolve จากรหัสนักศึกษา
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** INDEX, FK
- **PII Classification:** Identity
- **Source Column:** รหัสหรือ Continuation Context
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.academic_year_be`

- **ชื่อภาษาไทย:** ปีการศึกษา พ.ศ.
- **คำอธิบาย:** ปีที่ได้รับ/กู้ยืม
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse จากข้อความ
- **Validation / Allowed Values:** 2400–2700
- **Unique / Index:** INDEX
- **PII Classification:** Financial Sensitive
- **Source Column:** กยศ
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.amount`

- **ชื่อภาษาไทย:** จำนวนเงิน
- **คำอธิบาย:** จำนวนเงิน กยศ.
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse จากข้อความ
- **Validation / Allowed Values:** >= 0
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** กยศ
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.loan_type`

- **ชื่อภาษาไทย:** ประเภทเงินกู้
- **คำอธิบาย:** ประเภท เช่น กยศ.
- **PostgreSQL Type:** VARCHAR(100)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** 'กยศ'
- **Validation / Allowed Values:** Reference Value
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** กยศ
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.raw_text`

- **ชื่อภาษาไทย:** ข้อความต้นฉบับ
- **คำอธิบาย:** ข้อความก่อน Parse
- **PostgreSQL Type:** TEXT
- **Required Level:** Required if row exists
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามว่าง
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** กยศ
- **สถานะ / หมายเหตุ:** -

## `student_loan_histories.source_import_row_id`

- **ชื่อภาษาไทย:** แถวนำเข้าต้นทาง
- **คำอธิบาย:** ใช้ Audit และแจ้ง Error
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** Current import row
- **Validation / Allowed Values:** FK
- **Unique / Index:** INDEX, FK
- **PII Classification:** Operational
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.id`

- **ชื่อภาษาไทย:** รหัสประวัติทุน
- **คำอธิบาย:** Primary Key
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** gen_random_uuid()
- **Validation / Allowed Values:** -
- **Unique / Index:** PK
- **PII Classification:** None
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.applicant_id`

- **ชื่อภาษาไทย:** ผู้สมัคร
- **คำอธิบาย:** เชื่อมกับ applicants
- **PostgreSQL Type:** UUID
- **Required Level:** Resolved
- **Nullable:** No
- **Default / Source:** Resolve จากรหัสนักศึกษา
- **Validation / Allowed Values:** FK ต้องมีอยู่จริง
- **Unique / Index:** INDEX, FK
- **PII Classification:** Identity
- **Source Column:** รหัสหรือ Continuation Context
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.academic_year_be`

- **ชื่อภาษาไทย:** ปีการศึกษา พ.ศ.
- **คำอธิบาย:** ปีที่ได้รับทุน
- **PostgreSQL Type:** SMALLINT
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse จากข้อความ
- **Validation / Allowed Values:** 2400–2700
- **Unique / Index:** INDEX
- **PII Classification:** Financial Sensitive
- **Source Column:** ทุน
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.scholarship_name`

- **ชื่อภาษาไทย:** ชื่อทุน
- **คำอธิบาย:** ชื่อทุนหรือแหล่งทุน
- **PostgreSQL Type:** VARCHAR(255)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse จากข้อความ
- **Validation / Allowed Values:** Trim
- **Unique / Index:** INDEX
- **PII Classification:** Financial Sensitive
- **Source Column:** ทุน
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.amount`

- **ชื่อภาษาไทย:** มูลค่าทุน
- **คำอธิบาย:** จำนวนเงินทุน
- **PostgreSQL Type:** NUMERIC(12,2)
- **Required Level:** Optional
- **Nullable:** Yes
- **Default / Source:** Parse จากข้อความ
- **Validation / Allowed Values:** >= 0
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** ทุน
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.raw_text`

- **ชื่อภาษาไทย:** ข้อความต้นฉบับ
- **คำอธิบาย:** ข้อความก่อน Parse
- **PostgreSQL Type:** TEXT
- **Required Level:** Required if row exists
- **Nullable:** No
- **Default / Source:** Trim
- **Validation / Allowed Values:** ห้ามว่าง
- **Unique / Index:** -
- **PII Classification:** Financial Sensitive
- **Source Column:** ทุน
- **สถานะ / หมายเหตุ:** -

## `scholarship_histories.source_import_row_id`

- **ชื่อภาษาไทย:** แถวนำเข้าต้นทาง
- **คำอธิบาย:** ใช้ Audit และแจ้ง Error
- **PostgreSQL Type:** UUID
- **Required Level:** System
- **Nullable:** No
- **Default / Source:** Current import row
- **Validation / Allowed Values:** FK
- **Unique / Index:** INDEX, FK
- **PII Classification:** Operational
- **Source Column:** -
- **สถานะ / หมายเหตุ:** -
