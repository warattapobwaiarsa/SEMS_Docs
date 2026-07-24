# Data Import to Web - Column Specification

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../START_HERE.md) › [🎨 Design](../README.md) › Data Import to Web - Column Specification

> ถอดหัวคอลัมน์จาก [`Data_import_to_web.xlsx`](./Data_import_to_web.xlsx) จำนวน 37 คอลัมน์เป็นรายการแนวตั้ง เพื่อให้อ่านบน GitHub ได้โดยไม่ต้องเลื่อนตารางในแนวนอน

รายละเอียดกฎนำเข้าและ Error Code ฉบับเต็มอยู่ที่ [`SEMS_Applicant_Import_Mapping_Specification.md`](./SEMS_Applicant_Import_Mapping_Specification.md)

## รายการคอลัมน์

### 1. `A` - `ลำดับ`

- **Alias ที่ยอมรับ:** -
- **ปลายทาง:** `applicants.sequence_no`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Integer
- **Validation:** > 0 เมื่อมีค่า
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1
- **หมายเหตุ:** ใช้เพื่อแสดงผล/Audit เท่านั้น ไม่ใช้เป็น Key

### 2. `B` - `รหัส`

- **Alias ที่ยอมรับ:** student_id
- **ปลายทาง:** `applicants.student_id`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** อ่านเป็น Text; Trim; คงเครื่องหมายขีดกลาง
- **Validation:** ^\\d{9}-\\d$; Unique ภายในรอบทุน; ยังไม่ตรวจ check digit
- **Continuation Row:** ว่างได้เฉพาะ Continuation Row และสืบทอดจาก Applicant Row ก่อนหน้า
- **ตัวอย่าง:** 663040664-8
- **หมายเหตุ:** ห้าม Excel แปลงเป็น Scientific Notation

### 3. `C` - `คำนำหน้า`

- **Alias ที่ยอมรับ:** title
- **ปลายทาง:** `applicants.title`
- **ระดับความจำเป็น:** Required before Evaluation
- **Parsing / Normalization:** Trim; Map กับ Code List
- **Validation:** ต้องอยู่ในชุดค่าที่อนุญาต เช่น นาย/นาง/นางสาว/อื่น ๆ
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** นาย
- **หมายเหตุ:** ว่างได้ตอน Upload/Preview แต่ต้องครบก่อนเริ่ม Evaluation ตาม RD-019/Q-025

### 4. `D` - `ชือ`

- **Alias ที่ยอมรับ:** ชื่อ\|first_name
- **ปลายทาง:** `applicants.first_name`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** Trim; รองรับ Alias “ชื่อ”
- **Validation:** ห้ามว่างหลัง Trim
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** สมชาย
- **หมายเหตุ:** ควรแก้ Header Template เป็น “ชื่อ”

### 5. `E` - `สกุล`

- **Alias ที่ยอมรับ:** last_name
- **ปลายทาง:** `applicants.last_name`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** Trim
- **Validation:** ห้ามว่างหลัง Trim
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** ใจดี
- **หมายเหตุ:** -

### 6. `F` - `คณะ`

- **Alias ที่ยอมรับ:** faculty
- **ปลายทาง:** `applicants.faculty_name`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** Trim; Map กับข้อมูลอ้างอิง
- **Validation:** ห้ามว่าง; ค่าไม่รู้จักให้ Warning/เลือก Mapping
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** คณะวิศวกรรมศาสตร์
- **หมายเหตุ:** -

### 7. `G` - `สาขา`

- **Alias ที่ยอมรับ:** major
- **ปลายทาง:** `applicants.major_name`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** Trim; Map กับข้อมูลอ้างอิง
- **Validation:** ห้ามว่าง; ค่าไม่รู้จักให้ Warning/เลือก Mapping
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** วิศวกรรมเครื่องกล
- **หมายเหตุ:** -

### 8. `H` - `ชั้นปี`

- **Alias ที่ยอมรับ:** year_level
- **ปลายทาง:** `applicants.year_level`
- **ระดับความจำเป็น:** Hard Required
- **Parsing / Normalization:** Integer
- **Validation:** 1–8 (ช่วง Draft; ต้องยืนยันค่าสูงสุด)
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 5
- **หมายเหตุ:** -

### 9. `I` - `วันที่สมัคร`

- **Alias ที่ยอมรับ:** application_date
- **ปลายทาง:** `applicants.application_date`
- **ระดับความจำเป็น:** Required before Evaluation
- **Parsing / Normalization:** Parse ISO/Excel Date/เดือนภาษาไทย; ถ้า พ.ศ. ให้ลบ 543; timezone Asia/Bangkok
- **Validation:** ต้อง Parse ได้และไม่กำกวม
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 09 ก.ค. 2569 13:36 → 2026-07-09T13:36:00+07:00
- **หมายเหตุ:** ใช้รูปแบบมาตรฐานและ documented legacy normalization ตาม RD-020/Q-030

### 10. `J` - `gpa`

- **Alias ที่ยอมรับ:** GPA
- **ปลายทาง:** `applicants.gpa`
- **ระดับความจำเป็น:** Required before Evaluation
- **Parsing / Normalization:** ลบช่องว่าง; Decimal(3,2)
- **Validation:** 0.00–4.00
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 3.25
- **หมายเหตุ:** ค่าจากไฟล์ 0 ให้เก็บ 0.00 ไม่ใช่ NULL

### 11. `K` - `โทรศัพท์`

- **Alias ที่ยอมรับ:** phone\|เบอร์โทร
- **ปลายทาง:** `applicants.phone`
- **ระดับความจำเป็น:** Conditional
- **Parsing / Normalization:** อ่านเป็น Text; ลบช่องว่าง/ขีด; Normalize 0XXXXXXXXX หรือ +66XXXXXXXXX
- **Validation:** ^0\\d{8,9}$ หรือ ^\\+66\\d{8,9}$; อย่างน้อย phone หรือ email
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 0812345678
- **หมายเหตุ:** ห้าม Scientific Notation และต้องคงเลข 0 นำหน้า

### 12. `L` - `อีเมล์`

- **Alias ที่ยอมรับ:** email\|อีเมล
- **ปลายทาง:** `applicants.email`
- **ระดับความจำเป็น:** Conditional
- **Parsing / Normalization:** Trim; lowercase
- **Validation:** รูปแบบอีเมลถูกต้อง; อย่างน้อย phone หรือ email
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** student@kkumail.com
- **หมายเหตุ:** -

### 13. `M` - `ที่พัก`

- **Alias ที่ยอมรับ:** residence_type
- **ปลายทาง:** `applicants.residence_type`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map กับ Code List
- **Validation:** ค่าไม่รู้จักให้ Warning และเก็บ raw value เพื่อ Mapping
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** หอพัก มข
- **หมายเหตุ:** -

### 14. `N` - `ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ`

- **Alias ที่ยอมรับ:** housing_cost
- **ปลายทาง:** `applicant_expenses.housing_cost_monthly`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 900
- **หมายเหตุ:** หน่วยต่อเดือนตามชื่อคอลัมน์

### 15. `O` - `ค่าใช้จ่ายส่วนตัว`

- **Alias ที่ยอมรับ:** personal_expense
- **ปลายทาง:** `applicant_expenses.personal_expense_monthly`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 4000
- **หมายเหตุ:** หน่วยต่อเดือนตาม Data Dictionary Draft

### 16. `P` - `ค่าอุปกรณ์การศึกษา`

- **Alias ที่ยอมรับ:** education_equipment_expense
- **ปลายทาง:** `applicant_expenses.education_equipment_expense`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1000
- **หมายเหตุ:** ต้องยืนยันว่าเป็นรายเดือน/ภาค/ปี

### 17. `Q` - `อุปกรณ์อิเล็กทรอนิกส์ที่มี`

- **Alias ที่ยอมรับ:** electronic_devices
- **ปลายทาง:** `applicant_expenses.electronic_devices`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; เก็บเป็น Text
- **Validation:** ความยาวไม่เกินค่าที่ระบบกำหนด
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** โทรศัพท์มือถือ
- **หมายเหตุ:** ระยะแรกไม่แยกเป็นหลาย Record

### 18. `R` - `รายได้เสริม`

- **Alias ที่ยอมรับ:** supplementary_income
- **ปลายทาง:** `applicants.supplementary_income_detail`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; ค่าว่างหรือ '-' → NULL
- **Validation:** ข้อความตามความยาวที่กำหนด
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** ไม่มีรายได้เสริม
- **หมายเหตุ:** ไม่ควรตีความข้อความเป็นจำนวนเงินโดยอัตโนมัติ

### 19. `S` - `บิดา อายุ`

- **Alias ที่ยอมรับ:** father_age
- **ปลายทาง:** `parent_information.age (parent_type=FATHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Integer
- **Validation:** 15–120; ถ้าเสียชีวิตอาจว่างได้
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 56
- **หมายเหตุ:** -

### 20. `T` - `บิดา อาชีพ`

- **Alias ที่ยอมรับ:** father_occupation
- **ปลายทาง:** `parent_information.occupation (parent_type=FATHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List เมื่อมี
- **Validation:** ค่าไม่รู้จักให้ Warning
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** เกษตรกร/ ประมง
- **หมายเหตุ:** -

### 21. `U` - `บิดา รายได้`

- **Alias ที่ยอมรับ:** father_income
- **ปลายทาง:** `parent_information.monthly_income (parent_type=FATHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0; หน่วยบาทต่อเดือน
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1200
- **หมายเหตุ:** 0 = ไม่มีรายได้; NULL = ไม่ทราบ/ไม่กรอก

### 22. `V` - `บิดา สภาพ`

- **Alias ที่ยอมรับ:** father_life_status
- **ปลายทาง:** `parent_information.life_status (parent_type=FATHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List
- **Validation:** เช่น มีชีวิตอยู่/เสียชีวิต/ไม่ทราบ
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** มีชีวิตอยู่
- **หมายเหตุ:** -

### 23. `W` - `มารดา อายุ`

- **Alias ที่ยอมรับ:** mother_age
- **ปลายทาง:** `parent_information.age (parent_type=MOTHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Integer
- **Validation:** 15–120; ถ้าเสียชีวิตอาจว่างได้
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 54
- **หมายเหตุ:** -

### 24. `X` - `มารดา อาชีพ`

- **Alias ที่ยอมรับ:** mother_occupation
- **ปลายทาง:** `parent_information.occupation (parent_type=MOTHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List เมื่อมี
- **Validation:** ค่าไม่รู้จักให้ Warning
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** เกษตรกร/ ประมง
- **หมายเหตุ:** -

### 25. `Y` - `มารดา รายได้`

- **Alias ที่ยอมรับ:** mother_income
- **ปลายทาง:** `parent_information.monthly_income (parent_type=MOTHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0; หน่วยบาทต่อเดือน
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1200
- **หมายเหตุ:** 0 = ไม่มีรายได้; NULL = ไม่ทราบ/ไม่กรอก

### 26. `Z` - `มารดา สภาพ`

- **Alias ที่ยอมรับ:** mother_life_status
- **ปลายทาง:** `parent_information.life_status (parent_type=MOTHER)`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List
- **Validation:** เช่น มีชีวิตอยู่/เสียชีวิต/ไม่ทราบ
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** มีชีวิตอยู่
- **หมายเหตุ:** -

### 27. `AA` - `สภาพบิดา-มารดา`

- **Alias ที่ยอมรับ:** parents_relationship_status
- **ปลายทาง:** `education_support.parents_relationship_status`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List
- **Validation:** ค่าไม่รู้จักให้ Warning
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** อยู่ด้วยกัน
- **หมายเหตุ:** -

### 28. `AB` - `คนออกเงินเรียน`

- **Alias ที่ยอมรับ:** tuition_payer
- **ปลายทาง:** `education_support.tuition_payer`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Trim; Map Code List
- **Validation:** เช่น บิดา-มารดา/ตนเอง/ญาติ/อื่น ๆ
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** บิดา-มารดา
- **หมายเหตุ:** -

### 29. `AC` - `อุปการะ-ความเกี่ยวข้อง`

- **Alias ที่ยอมรับ:** supporter_relationship
- **ปลายทาง:** `education_support.supporter_relationship`
- **ระดับความจำเป็น:** Conditional
- **Parsing / Normalization:** Trim
- **Validation:** Required เมื่อ tuition_payer เป็นบุคคลอื่น
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** ป้า
- **หมายเหตุ:** -

### 30. `AD` - `อุปการะ-อาชีพ`

- **Alias ที่ยอมรับ:** supporter_occupation
- **ปลายทาง:** `education_support.supporter_occupation`
- **ระดับความจำเป็น:** Conditional
- **Parsing / Normalization:** Trim
- **Validation:** Required เมื่อมีข้อมูลผู้อุปการะ
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** ค้าขาย
- **หมายเหตุ:** -

### 31. `AE` - `อุปการะ-รายได้`

- **Alias ที่ยอมรับ:** supporter_income
- **ปลายทาง:** `education_support.supporter_monthly_income`
- **ระดับความจำเป็น:** Conditional
- **Parsing / Normalization:** ลบ comma/ช่องว่าง; Decimal(12,2)
- **Validation:** >= 0; Required เมื่อมีข้อมูลผู้อุปการะ; หน่วยบาทต่อเดือน
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 15000
- **หมายเหตุ:** -

### 32. `AF` - `พี่น้อง-ทำงาน`

- **Alias ที่ยอมรับ:** sibling_working_count
- **ปลายทาง:** `sibling_summaries.working_count`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Integer
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1
- **หมายเหตุ:** -

### 33. `AG` - `พี่น้อง-ไม่ทำงาน`

- **Alias ที่ยอมรับ:** sibling_not_working_count
- **ปลายทาง:** `sibling_summaries.not_working_count`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Integer
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1
- **หมายเหตุ:** -

### 34. `AH` - `พี่น้อง-เรียน`

- **Alias ที่ยอมรับ:** sibling_studying_count
- **ปลายทาง:** `sibling_summaries.studying_count`
- **ระดับความจำเป็น:** Optional
- **Parsing / Normalization:** Integer
- **Validation:** >= 0
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 1
- **หมายเหตุ:** -

### 35. `AI` - `กยศ`

- **Alias ที่ยอมรับ:** loan_history
- **ปลายทาง:** `education_loan_histories.academic_year_be + amount`
- **ระดับความจำเป็น:** Optional / Repeatable
- **Parsing / Normalization:** Regex: ^\\s*-?\\s*(\\d{4})\\s*:\\s*([0-9,]+(?:\\.\\d{1,2})?)\\s*$; ลบ comma จาก amount
- **Validation:** ปี พ.ศ. 4 หลัก; amount >= 0; ไม่ซ้ำ applicant+year
- **Continuation Row:** อนุญาต; สร้าง Child Record และสืบทอด student_id จาก Applicant Row ก่อนหน้า
- **ตัวอย่าง:** -2565 : 66,000
- **หมายเหตุ:** หนึ่ง Cell = หนึ่งประวัติใน Legacy Template

### 36. `AJ` - `ทุน`

- **Alias ที่ยอมรับ:** scholarship_history
- **ปลายทาง:** `scholarship_histories.academic_year_be + scholarship_name + amount`
- **ระดับความจำเป็น:** Optional / Repeatable
- **Parsing / Normalization:** Regex: ^\\s*-?\\s*(\\d{4})\\s+(.+?)\\s*:\\s*([0-9,]+(?:\\.\\d{1,2})?)\\s*$
- **Validation:** ปี/ชื่อทุน/จำนวนเงินต้องครบ; amount >= 0; ไม่ซ้ำ applicant+year+ชื่อทุน
- **Continuation Row:** อนุญาต; สร้าง Child Record และสืบทอด student_id จาก Applicant Row ก่อนหน้า
- **ตัวอย่าง:** -2565 ทุนตัวอย่าง : 10,000
- **หมายเหตุ:** หนึ่ง Cell = หนึ่งประวัติใน Legacy Template

### 37. `AK` - `พิกัดแผนที่บ้าน`

- **Alias ที่ยอมรับ:** coordinates\|lat_lon
- **ปลายทาง:** `address_coordinates.latitude + longitude`
- **ระดับความจำเป็น:** Conditional Pair
- **Parsing / Normalization:** Split ด้วย comma; Trim; Decimal
- **Validation:** ต้องมี 2 ค่า; latitude -90..90; longitude -180..180
- **Continuation Row:** ต้องว่าง
- **ตัวอย่าง:** 16.3792973, 104.3854202
- **หมายเหตุ:** ห้ามมีเพียงค่าเดียว

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [Scoring Rule Specification](../Criteria/SEMS_Scoring_Rule_Specification.md)<br>
↑ หมวดเอกสาร: [🎨 Design](../README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [SEMS — Applicant Import Mapping Specification](./SEMS_Applicant_Import_Mapping_Specification.md)

<!-- DOC_NAV_END -->
