# 03 IMPORT MAPPING

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md) › 03 IMPORT MAPPING

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `03_IMPORT_MAPPING`

> **Release 1 override (RD-015, RD-025, RD-029):** every application mapping includes `scholarship_type_id`; duplicate identity is `round_id + scholarship_type_id + student_id`. National ID is not a mapped field and must not be persisted, logged or exported.

## 1. `ลำดับ` → `round_applications.source_sequence`

- **Header Alias:** No., sequence
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; parse integer
- **Validation:** >= 1
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 1
- **หมายเหตุ:** ใช้เพื่อแสดงผล/Audit ไม่ใช่ Unique Key

## 2. `รหัส` → `applicants + round_applications.student_id; resolve applicant_id`

- **Header Alias:** รหัสนักศึกษา, student_id
- **Mapping Type:** Direct + Lookup
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Trim; preserve as Text
- **Validation:** ห้าม Scientific Notation; ตรวจซ้ำในไฟล์และรอบทุน
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** 683040000-1
- **หมายเหตุ:** Business Key: round_id + scholarship_type_id + student_id

## 3. `คำนำหน้า` → `applicants.title`

- **Header Alias:** title
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map reference
- **Validation:** ค่าที่ไม่รู้จักเป็น Warning
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** นาย
- **หมายเหตุ:** -

## 4. `ชือ` → `applicants.first_name`

- **Header Alias:** ชื่อ, first_name
- **Mapping Type:** Direct
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Trim
- **Validation:** ห้ามว่าง
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** aaa
- **หมายเหตุ:** Template ใหม่ควรแก้ Header เป็น 'ชื่อ'

## 5. `สกุล` → `applicants.last_name`

- **Header Alias:** นามสกุล, last_name
- **Mapping Type:** Direct
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Trim
- **Validation:** ห้ามว่าง
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** aaaa
- **หมายเหตุ:** -

## 6. `คณะ` → `round_applications.faculty_name_snapshot`

- **Header Alias:** faculty
- **Mapping Type:** Direct
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Trim
- **Validation:** ห้ามว่าง
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** คณะวิศวกรรมศาสตร์
- **หมายเหตุ:** -

## 7. `สาขา` → `round_applications.major_name_snapshot`

- **Header Alias:** major
- **Mapping Type:** Direct
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Trim
- **Validation:** ห้ามว่าง
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** วิศวกรรมเครื่องกล
- **หมายเหตุ:** -

## 8. `ชั้นปี` → `round_applications.year_level`

- **Header Alias:** year_level
- **Mapping Type:** Direct
- **Source Required:** Yes
- **Required Level:** Hard Required
- **Normalization:** Parse integer
- **Validation:** 1–8 หรือช่วงที่ยืนยัน
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** 5
- **หมายเหตุ:** -

## 9. `วันที่สมัคร` → `round_applications.applied_at`

- **Header Alias:** applied_at, application_date
- **Mapping Type:** Direct + Parse
- **Source Required:** Required before Evaluation
- **Required Level:** Recommended
- **Normalization:** Parse ISO/Thai/Excel Date; timezone Asia/Bangkok
- **Validation:** ค่ากำกวม/แปลงไม่ได้เป็น Error
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 09 ก.ค. 2569 13:36
- **หมายเหตุ:** Template ใหม่ใช้ YYYY-MM-DD HH:mm

## 10. `gpa` → `round_applications.gpa`

- **Header Alias:** GPA
- **Mapping Type:** Direct
- **Source Required:** Before Evaluation
- **Required Level:** Required before Evaluation
- **Normalization:** Parse decimal
- **Validation:** 0.00–4.00
- **Null Handling:** ว่างได้ตอน Import แต่ห้ามเปิดประเมิน
- **ตัวอย่างจากไฟล์:** 0 / 3.02
- **หมายเหตุ:** -

## 11. `โทรศัพท์` → `applicants.phone`

- **Header Alias:** เบอร์โทร, phone
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Keep as Text; remove spaces/hyphens
- **Validation:** 9–15 digits; Scientific Notation เป็น Error
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 081000001
- **หมายเหตุ:** ไฟล์เดิมอาจเสียรูปเป็น 8.10000001E8

## 12. `อีเมล์` → `applicants.email`

- **Header Alias:** อีเมล, email
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Lowercase; Trim
- **Validation:** Email format
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** aaa@kkumail.com
- **หมายเหตุ:** -

## 13. `ที่พัก` → `round_applications.residence_type`

- **Header Alias:** residence
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map reference
- **Validation:** ค่าที่ไม่รู้จักเป็น Warning
- **Null Handling:** '-' เป็น NULL
- **ตัวอย่างจากไฟล์:** หอพัก มข
- **หมายเหตุ:** -

## 14. `ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ` → `round_applications.housing_monthly_cost`

- **Header Alias:** housing_cost
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 900
- **หมายเหตุ:** หน่วย: บาท/เดือน

## 15. `ค่าใช้จ่ายส่วนตัว` → `round_applications.personal_monthly_cost`

- **Header Alias:** personal_expense
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 4000
- **หมายเหตุ:** หน่วย: บาท/เดือน

## 16. `ค่าอุปกรณ์การศึกษา` → `round_applications.education_material_cost`

- **Header Alias:** education_material_cost
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 1000
- **หมายเหตุ:** ต้องยืนยันว่าเป็นต่อเดือน/ภาค/ปี

## 17. `อุปกรณ์อิเล็กทรอนิกส์ที่มี` → `round_applications.electronic_devices`

- **Header Alias:** devices
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim
- **Validation:** -
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** โทรศัพท์มือถือ
- **หมายเหตุ:** -

## 18. `รายได้เสริม` → `round_applications.additional_income_description; has_additional_income`

- **Header Alias:** additional_income
- **Mapping Type:** Direct + Derived
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; derive Boolean
- **Validation:** ไม่มีรายได้เสริม=false; ข้อความอื่น=true
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** ไม่มีรายได้เสริม
- **หมายเหตุ:** ไม่ควรทิ้งข้อความเดิม

## 19. `บิดา อายุ` → `application_parents.age (parent_type=FATHER)`

- **Header Alias:** father_age
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Parse integer
- **Validation:** 0–120
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 56
- **หมายเหตุ:** -

## 20. `บิดา อาชีพ` → `application_parents.occupation (FATHER)`

- **Header Alias:** father_occupation
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim
- **Validation:** -
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** เกษตรกร/ ประมง
- **หมายเหตุ:** -

## 21. `บิดา รายได้` → `application_parents.monthly_income (FATHER)`

- **Header Alias:** father_income
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL ไม่ใช่ 0
- **ตัวอย่างจากไฟล์:** 1200
- **หมายเหตุ:** -

## 22. `บิดา สภาพ` → `application_parents.life_status (FATHER)`

- **Header Alias:** father_status
- **Mapping Type:** Split + Reference Map
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map ALIVE/DECEASED/UNKNOWN
- **Validation:** Reference Value
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** มีชีวิตอยู่
- **หมายเหตุ:** -

## 23. `มารดา อายุ` → `application_parents.age (parent_type=MOTHER)`

- **Header Alias:** mother_age
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Parse integer
- **Validation:** 0–120
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 54
- **หมายเหตุ:** -

## 24. `มารดา อาชีพ` → `application_parents.occupation (MOTHER)`

- **Header Alias:** mother_occupation
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim
- **Validation:** -
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** เกษตรกร/ ประมง
- **หมายเหตุ:** -

## 25. `มารดา รายได้` → `application_parents.monthly_income (MOTHER)`

- **Header Alias:** mother_income
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL ไม่ใช่ 0
- **ตัวอย่างจากไฟล์:** 1200
- **หมายเหตุ:** -

## 26. `มารดา สภาพ` → `application_parents.life_status (MOTHER)`

- **Header Alias:** mother_status
- **Mapping Type:** Split + Reference Map
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map ALIVE/DECEASED/UNKNOWN
- **Validation:** Reference Value
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** มีชีวิตอยู่
- **หมายเหตุ:** -

## 27. `สภาพบิดา-มารดา` → `round_applications.parents_household_status`

- **Header Alias:** parents_status
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map reference
- **Validation:** Reference Value รอยืนยัน
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** อยู่ด้วยกัน
- **หมายเหตุ:** -

## 28. `คนออกเงินเรียน` → `round_applications.education_funder`

- **Header Alias:** education_funder
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; map reference
- **Validation:** Reference Value รอยืนยัน
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** บิดา-มารดา
- **หมายเหตุ:** -

## 29. `อุปการะ-ความเกี่ยวข้อง` → `application_guardians.relationship`

- **Header Alias:** guardian_relationship
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim
- **Validation:** -
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** -
- **หมายเหตุ:** สร้าง Guardian Row เมื่อมีอย่างน้อยหนึ่งช่อง

## 30. `อุปการะ-อาชีพ` → `application_guardians.occupation`

- **Header Alias:** guardian_occupation
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim
- **Validation:** -
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** -
- **หมายเหตุ:** -

## 31. `อุปการะ-รายได้` → `application_guardians.monthly_income`

- **Header Alias:** guardian_income
- **Mapping Type:** Split to Child Row
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Remove commas; parse decimal
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL ไม่ใช่ 0
- **ตัวอย่างจากไฟล์:** -
- **หมายเหตุ:** -

## 32. `พี่น้อง-ทำงาน` → `round_applications.siblings_working_count`

- **Header Alias:** siblings_working
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Parse integer
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 1
- **หมายเหตุ:** -

## 33. `พี่น้อง-ไม่ทำงาน` → `round_applications.siblings_not_working_count`

- **Header Alias:** siblings_not_working
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Parse integer
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 1
- **หมายเหตุ:** -

## 34. `พี่น้อง-เรียน` → `round_applications.siblings_studying_count`

- **Header Alias:** siblings_studying
- **Mapping Type:** Direct
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Parse integer
- **Validation:** >= 0
- **Null Handling:** ว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 1
- **หมายเหตุ:** -

## 35. `กยศ` → `student_loan_histories.academic_year_be; amount; loan_type; raw_text`

- **Header Alias:** student_loan_history
- **Mapping Type:** Parse to Multiple Child Rows
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; parse year/amount; keep raw text
- **Validation:** Parse ไม่ได้เป็น Warning/Error ตามนโยบาย
- **Null Handling:** '-' และว่างไม่สร้างแถว
- **ตัวอย่างจากไฟล์:** -2565 : 66,000
- **หมายเหตุ:** Continuation Row ผูกกับผู้สมัครแถวก่อนหน้า

## 36. `ทุน` → `scholarship_histories.academic_year_be; scholarship_name; amount; raw_text`

- **Header Alias:** scholarship_history
- **Mapping Type:** Parse to Multiple Child Rows
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; parse year/name/amount; keep raw text
- **Validation:** Parse ไม่ได้เป็น Warning/Error ตามนโยบาย
- **Null Handling:** '-' และว่างไม่สร้างแถว
- **ตัวอย่างจากไฟล์:** -2565 กองทุน... : 10,000
- **หมายเหตุ:** Template ใหม่ควรแยก Sheet

## 37. `พิกัดแผนที่บ้าน` → `round_applications.home_location_raw; home_map_url; home_latitude; home_longitude`

- **Header Alias:** home_location, map_url
- **Mapping Type:** Direct + Derived
- **Source Required:** No
- **Required Level:** Optional
- **Normalization:** Trim; detect URL or lat,lng
- **Validation:** Latitude/Longitude range หรือ URL format
- **Null Handling:** '-' และว่างเป็น NULL
- **ตัวอย่างจากไฟล์:** 16.379297..., 104.385420...
- **หมายเหตุ:** ข้อมูลตำแหน่งเป็น Sensitive

## 38. Historical national-ID mapping proposal — not implemented

- **Release 1:** `Out of Scope for Release 1 — requires separate lawful-need and security approval`
- No alias, target column, normalization or persistence exists in the Release 1 importer.
- If a source file contains such a column/value, Preview reports it as unsupported and Confirm does not persist or log the value.

## 39. `[System-supplied]` → `import_batches + round_applications.round_id + scholarship_type_id`

- **Header Alias:** round_id
- **Mapping Type:** System
- **Source Required:** Yes
- **Required Level:** System Required
- **Normalization:** เลือกจาก UI
- **Validation:** รอบต้องอนุญาต Import
- **Null Handling:** ห้ามว่าง
- **ตัวอย่างจากไฟล์:** -
- **หมายเหตุ:** ไม่ควรให้ผู้ใช้กรอกซ้ำทุกแถว

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [02 DATA DICTIONARY](./02_DATA_DICTIONARY.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [04 VALIDATION RULES](./04_VALIDATION_RULES.md)

<!-- DOC_NAV_END -->
