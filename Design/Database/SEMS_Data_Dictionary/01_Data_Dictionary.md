# Data Dictionary

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

แหล่งข้อมูล: [`SEMS_Data_Dictionary.xlsx`](../SEMS_Data_Dictionary.xlsx), ชีต `Data Dictionary`

รวม 115 ฟิลด์ใน 11 Entity/Table

## รายการ Entity/Table

- [`applicants`](#applicants)
- [`applicant_expenses`](#applicant-expenses)
- [`parent_information`](#parent-information)
- [`education_support`](#education-support)
- [`sibling_summaries`](#sibling-summaries)
- [`education_loan_histories`](#education-loan-histories)
- [`scholarship_histories`](#scholarship-histories)
- [`applicant_documents`](#applicant-documents)
- [`address_coordinates`](#address-coordinates)
- [`import_batches`](#import-batches)
- [`import_rows`](#import-rows)

## `applicants`

### `id`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** รหัสภายในของผู้สมัครในรอบทุน
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** 7e3d…
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** ใช้ UUID เพื่อไม่เปิดเผยลำดับข้อมูล

### `scholarship_round_id`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** รอบทุนที่ผู้สมัครอยู่
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → scholarship_rounds.id
- **Validation / Business Rule:** ต้องอ้างถึงรอบทุนที่มีอยู่จริง; Unique ร่วมกับ student_id
- **ตัวอย่าง:** round-2569-01
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `sequence_no`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ลำดับรายการในไฟล์ต้นทาง
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็มมากกว่า 0; ไม่ใช้เป็น Primary Key
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** ลำดับ
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `student_id`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** รหัสนักศึกษา
- **ชนิดข้อมูล:** `Varchar(11)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** Unique (scholarship_round_id, student_id)
- **Validation / Business Rule:** รูปแบบเบื้องต้น ^\\d{9}-\\d$; ตัดช่องว่าง; ห้ามซ้ำภายในรอบทุน
- **ตัวอย่าง:** 663040664-8
- **คอลัมน์ต้นทาง:** รหัส
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** ยังไม่ควรตรวจ check digit จนกว่าจะได้สูตรยืนยันจากมหาวิทยาลัย

### `title`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** คำนำหน้าชื่อ
- **ชนิดข้อมูล:** `Varchar(30)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตัดช่องว่าง; ควรอ้างอิงชุดค่าที่อนุญาต
- **ตัวอย่าง:** นาย
- **คอลัมน์ต้นทาง:** คำนำหน้า
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `first_name`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ชื่อ
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ห้ามเป็นค่าว่างหลัง Trim
- **ตัวอย่าง:** สมชาย
- **คอลัมน์ต้นทาง:** ชือ
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** รองรับชื่อหัวคอลัมน์ต้นทางทั้ง “ชือ” และ “ชื่อ”

### `last_name`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** นามสกุล
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ห้ามเป็นค่าว่างหลัง Trim
- **ตัวอย่าง:** ใจดี
- **คอลัมน์ต้นทาง:** สกุล
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `faculty_name`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ชื่อคณะ
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตัดช่องว่าง; ควรทำ Mapping กับข้อมูลอ้างอิงของมหาวิทยาลัย
- **ตัวอย่าง:** คณะวิศวกรรมศาสตร์
- **คอลัมน์ต้นทาง:** คณะ
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `major_name`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ชื่อสาขาวิชา
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตัดช่องว่าง; ควรทำ Mapping กับข้อมูลอ้างอิง
- **ตัวอย่าง:** วิศวกรรมเครื่องกล
- **คอลัมน์ต้นทาง:** สาขา
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `year_level`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ชั้นปีของนักศึกษา
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็ม; ค่าแนะนำ 1–8
- **ตัวอย่าง:** 5
- **คอลัมน์ต้นทาง:** ชั้นปี
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** ต้องยืนยันชั้นปีสูงสุดที่ระบบยอมรับ

### `application_date`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** วันและเวลาที่สมัคร
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** อ่านเดือนภาษาไทย; แปลงปี พ.ศ. เป็น ค.ศ.; ใช้เขตเวลา Asia/Bangkok
- **ตัวอย่าง:** 46212.275
- **คอลัมน์ต้นทาง:** วันที่สมัคร
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `gpa`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** เกรดเฉลี่ยสะสม
- **ชนิดข้อมูล:** `Decimal(3,2)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** 0.00–4.00; เก็บ 2 ตำแหน่งทศนิยม
- **ตัวอย่าง:** 3.25
- **คอลัมน์ต้นทาง:** gpa
- **ระดับความอ่อนไหว:** Sensitive-Education
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `phone`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** หมายเลขโทรศัพท์
- **ชนิดข้อมูล:** `Varchar(20)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ลบช่องว่าง/ขีด; รองรับ 0XXXXXXXXX หรือ +66XXXXXXXXX; ต้องมีอย่างน้อยโทรศัพท์หรืออีเมล
- **ตัวอย่าง:** 0812345678
- **คอลัมน์ต้นทาง:** โทรศัพท์
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `email`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** อีเมล
- **ชนิดข้อมูล:** `Varchar(254)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** Trim และแปลงเป็นตัวพิมพ์เล็ก; ตรวจรูปแบบอีเมล; ต้องมีอย่างน้อยโทรศัพท์หรืออีเมล
- **ตัวอย่าง:** student@kkumail.com
- **คอลัมน์ต้นทาง:** อีเมล์
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `residence_type`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ลักษณะที่พักปัจจุบัน
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** Trim; แนะนำใช้ชุดค่ามาตรฐานและอนุญาต “อื่น ๆ”
- **ตัวอย่าง:** หอพัก มข
- **คอลัมน์ต้นทาง:** ที่พัก
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `supplementary_income_detail`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** รายละเอียดรายได้เสริม
- **ชนิดข้อมูล:** `Text`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** Trim; ค่าว่างหรือข้อความ “ไม่มีรายได้เสริม” เก็บตามจริงหรือ Normalize เป็นค่ามาตรฐาน
- **ตัวอย่าง:** ไม่มีรายได้เสริม
- **คอลัมน์ต้นทาง:** รายได้เสริม
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `import_batch_id`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** ชุดการนำเข้าที่สร้างข้อมูลนี้
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** FK → import_batches.id
- **Validation / Business Rule:** ต้องอ้างถึง Import Batch ที่สำเร็จหรือสำเร็จบางส่วน
- **ตัวอย่าง:** batch-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `source_row_no`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** เลขแถวต้นทางของข้อมูลผู้สมัคร
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่า 1 เพราะแถวแรกเป็น Header
- **ตัวอย่าง:** 2
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** วันที่สร้างข้อมูล
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v1.1 | 2026-07-23 | SEMS Documentation Team | Added stable GitHub anchors for entity sections; converted workbook content unchanged. |
| v1.0 | 2026-07-23 | SEMS Documentation Team | Initial workbook conversion. |

### `updated_at`

- **กลุ่มข้อมูล:** Applicant
- **ความหมาย:** วันที่แก้ไขล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติเมื่อข้อมูลเปลี่ยน
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="applicant-expenses"></a>
## `applicant_expenses`

### `id`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** รหัสข้อมูลค่าใช้จ่าย
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** exp-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** ผู้สมัครเจ้าของข้อมูลค่าใช้จ่าย
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id; Unique
- **Validation / Business Rule:** ผู้สมัครหนึ่งรายมีข้อมูลสรุปค่าใช้จ่ายได้ไม่เกินหนึ่งชุดต่อรอบ
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `housing_cost_monthly`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** ค่าเช่าหอ/บ้านรวมค่าน้ำและค่าไฟต่อเดือน
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าตั้งแต่ 0 ขึ้นไป; ลบเครื่องหมายคั่นหลักพัน
- **ตัวอย่าง:** 900.00
- **คอลัมน์ต้นทาง:** ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `personal_expense_monthly`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** ค่าใช้จ่ายส่วนตัวต่อเดือน
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าตั้งแต่ 0 ขึ้นไป; ลบเครื่องหมายคั่นหลักพัน
- **ตัวอย่าง:** 4000.00
- **คอลัมน์ต้นทาง:** ค่าใช้จ่ายส่วนตัว
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `education_equipment_expense`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** ค่าอุปกรณ์การศึกษาที่แจ้ง
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าตั้งแต่ 0 ขึ้นไป; ต้องยืนยันว่าเป็นรายเดือน รายภาค หรือรายปี
- **ตัวอย่าง:** 1000.00
- **คอลัมน์ต้นทาง:** ค่าอุปกรณ์การศึกษา
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `electronic_devices`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** อุปกรณ์อิเล็กทรอนิกส์ที่มี
- **ชนิดข้อมูล:** `Text`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** Trim; รองรับหลายรายการเป็นข้อความในระยะแรก
- **ตัวอย่าง:** โทรศัพท์มือถือ
- **คอลัมน์ต้นทาง:** อุปกรณ์อิเล็กทรอนิกส์ที่มี
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** วันที่สร้างข้อมูลค่าใช้จ่าย
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `updated_at`

- **กลุ่มข้อมูล:** Applicant Expense
- **ความหมาย:** วันที่แก้ไขข้อมูลค่าใช้จ่ายล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติ
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="parent-information"></a>
## `parent_information`

### `id`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** รหัสข้อมูลผู้ปกครอง
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** parent-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** ผู้สมัครเจ้าของข้อมูล
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id
- **Validation / Business Rule:** ต้องอ้างถึงผู้สมัครที่มีอยู่จริง
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `parent_type`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** ประเภทผู้ปกครอง
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** Yes / No
- **Key / Relation:** Unique (applicant_id, parent_type)
- **Validation / Business Rule:** ค่า: FATHER หรือ MOTHER
- **ตัวอย่าง:** FATHER
- **คอลัมน์ต้นทาง:** บิดา/มารดา
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `age`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** อายุผู้ปกครอง
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็ม 15–120; หากเสียชีวิตอาจเว้นว่างได้
- **ตัวอย่าง:** 56
- **คอลัมน์ต้นทาง:** บิดา อายุ / มารดา อายุ
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `occupation`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** อาชีพผู้ปกครอง
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** Trim; ควรมีรายการมาตรฐานพร้อมตัวเลือกอื่น ๆ
- **ตัวอย่าง:** เกษตรกร/ประมง
- **คอลัมน์ต้นทาง:** บิดา อาชีพ / มารดา อาชีพ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `monthly_income`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** รายได้ต่อเดือนของผู้ปกครอง
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าตั้งแต่ 0 ขึ้นไป; ต้องยืนยันหน่วยเวลาเป็นรายเดือน
- **ตัวอย่าง:** 1200.00
- **คอลัมน์ต้นทาง:** บิดา รายได้ / มารดา รายได้
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `life_status`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** สถานภาพการมีชีวิตของผู้ปกครอง
- **ชนิดข้อมูล:** `Varchar(50)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ใช้ชุดค่ามาตรฐาน เช่น มีชีวิตอยู่, เสียชีวิต, ไม่ทราบ
- **ตัวอย่าง:** มีชีวิตอยู่
- **คอลัมน์ต้นทาง:** บิดา สภาพ / มารดา สภาพ
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** วันที่สร้างข้อมูลผู้ปกครอง
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `updated_at`

- **กลุ่มข้อมูล:** Parent Information
- **ความหมาย:** วันที่แก้ไขข้อมูลผู้ปกครองล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติ
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="education-support"></a>
## `education_support`

### `id`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** รหัสข้อมูลผู้สนับสนุนค่าเล่าเรียน
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** support-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** ผู้สมัครเจ้าของข้อมูล
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id; Unique
- **Validation / Business Rule:** ผู้สมัครหนึ่งรายมีข้อมูลสรุปผู้สนับสนุนหนึ่งชุด
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `parents_relationship_status`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** สภาพความสัมพันธ์/การอยู่อาศัยของบิดาและมารดา
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ใช้ชุดค่ามาตรฐานและอนุญาตอื่น ๆ
- **ตัวอย่าง:** อยู่ด้วยกัน
- **คอลัมน์ต้นทาง:** สภาพบิดา-มารดา
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `tuition_payer`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** บุคคลหลักที่ออกค่าใช้จ่ายการศึกษา
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ใช้ชุดค่ามาตรฐาน เช่น บิดา-มารดา, ญาติ, ตนเอง, อื่น ๆ
- **ตัวอย่าง:** บิดา-มารดา
- **คอลัมน์ต้นทาง:** คนออกเงินเรียน
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `supporter_relationship`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** ความเกี่ยวข้องของผู้อุปการะกับผู้สมัคร
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำเป็นเมื่อ tuition_payer เป็นบุคคลอื่นที่ไม่ใช่บิดา/มารดาหรือตนเอง
- **ตัวอย่าง:** ป้า
- **คอลัมน์ต้นทาง:** อุปการะ-ความเกี่ยวข้อง
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `supporter_occupation`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** อาชีพของผู้อุปการะ
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำเป็นเมื่อมีข้อมูลผู้อุปการะ
- **ตัวอย่าง:** ค้าขาย
- **คอลัมน์ต้นทาง:** อุปการะ-อาชีพ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `supporter_monthly_income`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** รายได้ต่อเดือนของผู้อุปการะ
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าตั้งแต่ 0 ขึ้นไป; จำเป็นเมื่อมีข้อมูลผู้อุปการะ; ต้องยืนยันหน่วยเวลา
- **ตัวอย่าง:** 15000.00
- **คอลัมน์ต้นทาง:** อุปการะ-รายได้
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** วันที่สร้างข้อมูล
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `updated_at`

- **กลุ่มข้อมูล:** Education Supporter
- **ความหมาย:** วันที่แก้ไขล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติ
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="sibling-summaries"></a>
## `sibling_summaries`

### `id`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** รหัสข้อมูลสรุปพี่น้อง
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** sib-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** ผู้สมัครเจ้าของข้อมูล
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id; Unique
- **Validation / Business Rule:** ผู้สมัครหนึ่งรายมีข้อมูลสรุปพี่น้องหนึ่งชุด
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `working_count`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** จำนวนพี่น้องที่ทำงาน
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็มตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** พี่น้อง-ทำงาน
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `not_working_count`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** จำนวนพี่น้องที่ไม่ทำงาน
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็มตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** พี่น้อง-ไม่ทำงาน
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `studying_count`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** จำนวนพี่น้องที่กำลังศึกษา
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** จำนวนเต็มตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** พี่น้อง-เรียน
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `total_count`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** จำนวนพี่น้องรวม
- **ชนิดข้อมูล:** `SmallInt (Derived)`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** คำนวณ working_count + not_working_count + studying_count
- **ตัวอย่าง:** 3
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Family
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** วันที่สร้างข้อมูล
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `updated_at`

- **กลุ่มข้อมูล:** Sibling Information
- **ความหมาย:** วันที่แก้ไขล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติ
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="education-loan-histories"></a>
## `education_loan_histories`

### `id`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** รหัสประวัติเงินกู้เพื่อการศึกษา
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** loan-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** ผู้สมัครเจ้าของประวัติ
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id
- **Validation / Business Rule:** ต้องอ้างถึงผู้สมัครที่มีอยู่จริง
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `loan_program`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** ประเภท/โครงการเงินกู้
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าเริ่มต้นจากคอลัมน์นี้คือ กยศ.; ออกแบบให้รองรับประเภทอื่น
- **ตัวอย่าง:** กยศ.
- **คอลัมน์ต้นทาง:** กยศ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `academic_year_be`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** ปีการศึกษา พ.ศ.
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** Yes / No
- **Key / Relation:** Unique แนะนำ (applicant_id, loan_program, academic_year_be)
- **Validation / Business Rule:** เลข 4 หลัก; ช่วงแนะนำ 2500–2700
- **ตัวอย่าง:** 2565
- **คอลัมน์ต้นทาง:** กยศ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `amount`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** จำนวนเงินกู้ในปีนั้น
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่าหรือเท่ากับ 0; ลบ comma ก่อนแปลงตัวเลข
- **ตัวอย่าง:** 66000.00
- **คอลัมน์ต้นทาง:** กยศ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `raw_value`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** ข้อความต้นฉบับจากไฟล์
- **ชนิดข้อมูล:** `Text`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** เก็บเพื่อ Audit และตรวจสอบย้อนหลัง
- **ตัวอย่าง:** -2565 : 66,000
- **คอลัมน์ต้นทาง:** กยศ
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `source_row_no`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** เลขแถวต้นทาง
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่า 1; ใช้ชี้ตำแหน่ง error
- **ตัวอย่าง:** 2
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Education Loan History
- **ความหมาย:** วันที่สร้างประวัติ
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="scholarship-histories"></a>
## `scholarship_histories`

### `id`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** รหัสประวัติทุน
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** sch-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** ผู้สมัครเจ้าของประวัติทุน
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id
- **Validation / Business Rule:** ต้องอ้างถึงผู้สมัครที่มีอยู่จริง
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `academic_year_be`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** ปีการศึกษา พ.ศ. ที่ได้รับ/สมัครทุน
- **ชนิดข้อมูล:** `SmallInt`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** เลข 4 หลัก; ช่วงแนะนำ 2500–2700
- **ตัวอย่าง:** 2565
- **คอลัมน์ต้นทาง:** ทุน
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `scholarship_name`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** ชื่อทุน
- **ชนิดข้อมูล:** `Varchar(500)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** Trim; ห้ามเป็นค่าว่าง
- **ตัวอย่าง:** กองทุนพระราชทานสยามบรมราชกุมารีฯ
- **คอลัมน์ต้นทาง:** ทุน
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `amount`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** จำนวนเงินทุน
- **ชนิดข้อมูล:** `Decimal(12,2)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่าหรือเท่ากับ 0; ลบ comma ก่อนแปลงตัวเลข
- **ตัวอย่าง:** 10000.00
- **คอลัมน์ต้นทาง:** ทุน
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `record_status`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** สถานะประวัติ เช่น สมัครหรือได้รับ
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าแนะนำ APPLIED, RECEIVED, UNKNOWN
- **ตัวอย่าง:** RECEIVED
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** ไฟล์ต้นทางยังไม่ระบุชัดว่าเป็นประวัติสมัครหรือได้รับ

### `raw_value`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** ข้อความต้นฉบับจากไฟล์
- **ชนิดข้อมูล:** `Text`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** เก็บเพื่อ Audit และตรวจสอบย้อนหลัง
- **ตัวอย่าง:** -2565 กองทุนพระราชทานสยามบรมราชกุมารีฯ : 10,000
- **คอลัมน์ต้นทาง:** ทุน
- **ระดับความอ่อนไหว:** Sensitive-Financial
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `source_row_no`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** เลขแถวต้นทาง
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่า 1; ใช้ชี้ตำแหน่ง error
- **ตัวอย่าง:** 2
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Scholarship History
- **ความหมาย:** วันที่สร้างประวัติ
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="applicant-documents"></a>
## `applicant_documents`

### `id`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** รหัสเอกสาร
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** doc-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ผู้สมัครเจ้าของเอกสาร
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id
- **Validation / Business Rule:** ต้องอ้างถึงผู้สมัครที่มีอยู่จริง
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `document_type`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ประเภทเอกสารประกอบ
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ใช้ชุดค่ามาตรฐาน เช่น หนังสือรับรอง, หลักฐานรายได้, รูปบ้าน, อื่น ๆ
- **ตัวอย่าง:** หลักฐานรายได้
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Document
- **สถานะข้อกำหนด:** ต้องยืนยัน
- **หมายเหตุ:** -

### `original_file_name`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ชื่อไฟล์ต้นฉบับ
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตัด path; ป้องกันอักขระอันตราย
- **ตัวอย่าง:** income-proof.pdf
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Document
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `storage_key`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ตำแหน่งอ้างอิงใน File/Object Storage
- **ชนิดข้อมูล:** `Varchar(1000)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** Unique
- **Validation / Business Rule:** ห้ามเปิดเผย path จริงแก่ผู้ใช้; เข้าถึงผ่าน Backend เท่านั้น
- **ตัวอย่าง:** applicants/…/income-proof.pdf
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Secret/Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `mime_type`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ชนิด MIME ของไฟล์
- **ชนิดข้อมูล:** `Varchar(100)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** อนุญาต application/pdf, image/jpeg, image/png
- **ตัวอย่าง:** application/pdf
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Document
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `size_bytes`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ขนาดไฟล์เป็นไบต์
- **ชนิดข้อมูล:** `BigInt`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่า 0 และไม่เกินขนาดสูงสุดที่กำหนด
- **ตัวอย่าง:** 245760
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `checksum_sha256`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ค่าแฮชไฟล์สำหรับตรวจสอบความถูกต้อง/ไฟล์ซ้ำ
- **ชนิดข้อมูล:** `Char(64)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ตัวอักษรฐาน 16 จำนวน 64 ตัว
- **ตัวอย่าง:** a3f1…
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Secret/Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `uploaded_by_user_id`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** ผู้ใช้งานที่อัปโหลด
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → users.id
- **Validation / Business Rule:** ต้องเป็นผู้ดูแลระบบที่มีสิทธิ์
- **ตัวอย่าง:** user-admin-01
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `uploaded_at`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** วันและเวลาอัปโหลด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `is_active`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** สถานะการใช้งานของเอกสาร
- **ชนิดข้อมูล:** `Boolean`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าเริ่มต้น true; เอกสารที่ถูกยกเลิกไม่ควรแสดงแก่ผู้ประเมิน
- **ตัวอย่าง:** true
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `deleted_at`

- **กลุ่มข้อมูล:** Applicant Document
- **ความหมาย:** วันเวลาที่ลบแบบ Soft Delete
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** เป็น null เมื่อยังใช้งานอยู่
- **ตัวอย่าง:** null
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="address-coordinates"></a>
## `address_coordinates`

### `id`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** รหัสพิกัดบ้าน
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** coord-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_id`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** ผู้สมัครเจ้าของพิกัด
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → applicants.id; Unique
- **Validation / Business Rule:** ผู้สมัครหนึ่งรายมีพิกัดหลักหนึ่งชุดต่อรอบ
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `latitude`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** ละติจูดบ้าน
- **ชนิดข้อมูล:** `Decimal(10,7)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** -90 ถึง 90; ต้องมีพร้อม longitude
- **ตัวอย่าง:** 16.3792973
- **คอลัมน์ต้นทาง:** พิกัดแผนที่บ้าน
- **ระดับความอ่อนไหว:** Sensitive-Location
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `longitude`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** ลองจิจูดบ้าน
- **ชนิดข้อมูล:** `Decimal(10,7)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** -180 ถึง 180; ต้องมีพร้อม latitude
- **ตัวอย่าง:** 104.3854202
- **คอลัมน์ต้นทาง:** พิกัดแผนที่บ้าน
- **ระดับความอ่อนไหว:** Sensitive-Location
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์
- **หมายเหตุ:** -

### `raw_coordinate`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** ข้อความพิกัดต้นฉบับ
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** เก็บเพื่อ Audit และตรวจสอบกรณี Parse ไม่สำเร็จ
- **ตัวอย่าง:** 16.37929729279832, 104.38542017283481
- **คอลัมน์ต้นทาง:** พิกัดแผนที่บ้าน
- **ระดับความอ่อนไหว:** Sensitive-Location
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `coordinate_source`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** แหล่งที่มาของพิกัด
- **ชนิดข้อมูล:** `Varchar(50)`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** ค่าแนะนำ IMPORT, MANUAL, MAP_PICKER
- **ตัวอย่าง:** IMPORT
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** วันที่สร้างข้อมูลพิกัด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `updated_at`

- **กลุ่มข้อมูล:** Address Coordinate
- **ความหมาย:** วันที่แก้ไขพิกัดล่าสุด
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** อัปเดตอัตโนมัติ
- **ตัวอย่าง:** 46226.145833333336
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="import-batches"></a>
## `import_batches`

### `id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** รหัสชุดการนำเข้า
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** batch-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `scholarship_round_id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** รอบทุนปลายทาง
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → scholarship_rounds.id
- **Validation / Business Rule:** ต้องอ้างถึงรอบทุนที่อนุญาตให้นำเข้า
- **ตัวอย่าง:** round-2569-01
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `original_file_name`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ชื่อไฟล์ที่นำเข้า
- **ชนิดข้อมูล:** `Varchar(255)`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** เก็บชื่อไฟล์ต้นฉบับโดยไม่รวม local path
- **ตัวอย่าง:** Data_import_to_web.xlsx
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `file_type`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ประเภทไฟล์
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** XLSX หรือ CSV เท่านั้น
- **ตัวอย่าง:** XLSX
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `file_size_bytes`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ขนาดไฟล์นำเข้า
- **ชนิดข้อมูล:** `BigInt`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** มากกว่า 0 และไม่เกินขนาดสูงสุดที่ระบบกำหนด
- **ตัวอย่าง:** 81920
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `imported_by_user_id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ผู้ดูแลระบบที่นำเข้า
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → users.id
- **Validation / Business Rule:** ต้องมีบทบาทผู้ดูแลระบบและสถานะ Active
- **ตัวอย่าง:** user-admin-01
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `imported_at`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** วันและเวลานำเข้า
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `status`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** สถานะชุดการนำเข้า
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** PREVIEWED, VALIDATED, IMPORTED, PARTIAL, FAILED, CANCELLED
- **ตัวอย่าง:** IMPORTED
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `total_data_rows`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนแถวข้อมูลทั้งหมดไม่รวม Header
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 4
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `applicant_row_count`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนแถวหลักของผู้สมัคร
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** แถวที่มี student_id
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `continuation_row_count`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนแถวต่อเนื่องสำหรับประวัติหลายปี
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** แถวที่ student_id ว่างแต่มี กยศ/ทุน และเชื่อมกับผู้สมัครก่อนหน้าได้
- **ตัวอย่าง:** 3
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `success_count`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนผู้สมัครที่นำเข้าสำเร็จ
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตั้งแต่ 0 ขึ้นไปและไม่เกิน applicant_row_count
- **ตัวอย่าง:** 1
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `error_count`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนแถวที่มี Error
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 0
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อมูลจากไฟล์/Proposal
- **หมายเหตุ:** -

### `warning_count`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** จำนวนแถวที่มี Warning
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** ตั้งแต่ 0 ขึ้นไป
- **ตัวอย่าง:** 0
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -


<a id="import-rows"></a>
## `import_rows`

### `id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** รหัสผลตรวจสอบแถว
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** PK
- **Validation / Business Rule:** สร้างโดยระบบและห้ามซ้ำ
- **ตัวอย่าง:** row-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `import_batch_id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ชุดการนำเข้าของแถว
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** Yes / No
- **Key / Relation:** FK → import_batches.id
- **Validation / Business Rule:** ต้องอ้างถึง Import Batch ที่มีอยู่จริง
- **ตัวอย่าง:** batch-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `source_row_no`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** เลขแถวจริงในไฟล์
- **ชนิดข้อมูล:** `Integer`
- **Required / Nullable:** Yes / No
- **Key / Relation:** Unique (import_batch_id, source_row_no)
- **Validation / Business Rule:** มากกว่า 1
- **ตัวอย่าง:** 2
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `row_type`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ประเภทแถว
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** APPLICANT, CONTINUATION, BLANK, INVALID
- **ตัวอย่าง:** CONTINUATION
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `resolved_student_id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** รหัสนักศึกษาหลังใช้กฎสืบทอดจากแถวก่อนหน้า
- **ชนิดข้อมูล:** `Varchar(11)`
- **Required / Nullable:** Conditional / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** แถว CONTINUATION ต้อง resolve ได้; ห้ามสืบทอดข้ามแถว INVALID ที่ตัดบริบท
- **ตัวอย่าง:** 663040664-8
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** PII
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `raw_data_json`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ข้อมูลต้นฉบับทั้งแถว
- **ชนิดข้อมูล:** `JSONB`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** เก็บเฉพาะระยะเวลาตามนโยบาย; จำกัดสิทธิ์เข้าถึง
- **ตัวอย่าง:** {…}
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Sensitive-Mixed
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `validation_status`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ผลการตรวจสอบแถว
- **ชนิดข้อมูล:** `Enum`
- **Required / Nullable:** Yes / No
- **Key / Relation:** -
- **Validation / Business Rule:** VALID, WARNING, ERROR, SKIPPED
- **ตัวอย่าง:** VALID
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `messages_json`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** รายการ Error/Warning ของแถว
- **ชนิดข้อมูล:** `JSONB`
- **Required / Nullable:** No / Yes
- **Key / Relation:** -
- **Validation / Business Rule:** แต่ละข้อความควรมี field, code, message, severity
- **ตัวอย่าง:** [{…}]
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `imported_applicant_id`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** ผู้สมัครที่สร้างหรือเชื่อมโยงจากแถว
- **ชนิดข้อมูล:** `UUID`
- **Required / Nullable:** No / Yes
- **Key / Relation:** FK → applicants.id
- **Validation / Business Rule:** เป็น null เมื่อแถวนำเข้าไม่สำเร็จหรือเป็น Blank
- **ตัวอย่าง:** applicant-001
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -

### `created_at`

- **กลุ่มข้อมูล:** Import Management
- **ความหมาย:** วันที่สร้างผลตรวจสอบแถว
- **ชนิดข้อมูล:** `Timestamptz`
- **Required / Nullable:** Yes (System) / No
- **Key / Relation:** -
- **Validation / Business Rule:** กำหนดโดยระบบ
- **ตัวอย่าง:** 46226.125
- **คอลัมน์ต้นทาง:** -
- **ระดับความอ่อนไหว:** Internal
- **สถานะข้อกำหนด:** ข้อเสนอแนะ
- **หมายเหตุ:** -
