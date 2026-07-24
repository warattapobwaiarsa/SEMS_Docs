# Import Column Mapping

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary - Workbook Conversion](./README.md) › Import Column Mapping

แหล่งข้อมูล: [`SEMS_Data_Dictionary.xlsx`](../SEMS_Data_Dictionary.xlsx), ชีต `Import Column Mapping`

## 1. `ลำดับ` → `applicants.sequence_no`

- **Required ตอน Import:** No
- **Parsing / Normalization:** แปลงเป็น Integer
- **Validation หลัก:** > 0 ถ้ามี
- **การทำงานในแถวต่อเนื่อง:** ต้องว่างในแถวต่อเนื่อง
- **ตัวอย่างต้นทาง:** 1

## 2. `รหัส` → `applicants.student_id`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim; คงขีดกลาง
- **Validation หลัก:** ^\\d{9}-\\d$; Unique ภายในรอบ
- **การทำงานในแถวต่อเนื่อง:** ว่างได้เฉพาะแถวต่อเนื่องและสืบทอดจากผู้สมัครก่อนหน้า
- **ตัวอย่างต้นทาง:** 663040664-8

## 3. `คำนำหน้า` → `applicants.title`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ต้องอยู่ในชุดค่าที่อนุญาต
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** นาย

## 4. `ชือ` → `applicants.first_name`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim; รองรับ Alias “ชื่อ”
- **Validation หลัก:** ห้ามว่าง
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** สมชาย

## 5. `สกุล` → `applicants.last_name`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ห้ามว่าง
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** ใจดี

## 6. `คณะ` → `applicants.faculty_name`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim; Mapping กับข้อมูลอ้างอิง
- **Validation หลัก:** ห้ามว่าง
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** คณะวิศวกรรมศาสตร์

## 7. `สาขา` → `applicants.major_name`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Trim; Mapping กับข้อมูลอ้างอิง
- **Validation หลัก:** ห้ามว่าง
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** วิศวกรรมเครื่องกล

## 8. `ชั้นปี` → `applicants.year_level`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Integer
- **Validation หลัก:** ช่วงแนะนำ 1–8
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 5

## 9. `วันที่สมัคร` → `applicants.application_date`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Parse เดือนภาษาไทย; ปี พ.ศ.-543; Asia/Bangkok
- **Validation หลัก:** ต้องเป็นวันเวลาที่ถูกต้อง
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 09 ก.ค. 2569 13:36

## 10. `gpa` → `applicants.gpa`

- **Required ตอน Import:** Yes
- **Parsing / Normalization:** Decimal 2 ตำแหน่ง
- **Validation หลัก:** 0.00–4.00
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 3.25

## 11. `โทรศัพท์` → `applicants.phone`

- **Required ตอน Import:** Conditional
- **Parsing / Normalization:** ลบช่องว่างและขีด; Normalize ไทย/E.164
- **Validation หลัก:** อย่างน้อย phone หรือ email
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 0812345678

## 12. `อีเมล์` → `applicants.email`

- **Required ตอน Import:** Conditional
- **Parsing / Normalization:** Trim; lowercase
- **Validation หลัก:** รูปแบบอีเมล; อย่างน้อย phone หรือ email
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** student@kkumail.com

## 13. `ที่พัก` → `applicants.residence_type`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ควร Mapping กับชุดค่า
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** หอพัก มข

## 14. `ค่าเช่าหอ/บ้าน รวมค่าน้ำ-ไฟ` → `applicant_expenses.housing_cost_monthly`

- **Required ตอน Import:** No
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 900

## 15. `ค่าใช้จ่ายส่วนตัว` → `applicant_expenses.personal_expense_monthly`

- **Required ตอน Import:** No
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 4000

## 16. `ค่าอุปกรณ์การศึกษา` → `applicant_expenses.education_equipment_expense`

- **Required ตอน Import:** No
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0; ยืนยันหน่วยเวลา
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1000

## 17. `อุปกรณ์อิเล็กทรอนิกส์ที่มี` → `applicant_expenses.electronic_devices`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ข้อความยาวตามที่กำหนด
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** โทรศัพท์มือถือ

## 18. `รายได้เสริม` → `applicants.supplementary_income_detail`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim; Normalize “ไม่มีรายได้เสริม” ได้
- **Validation หลัก:** ข้อความยาวตามที่กำหนด
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** ไม่มีรายได้เสริม

## 19. `บิดา อายุ` → `parent_information(FATHER).age`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Integer
- **Validation หลัก:** 15–120
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 56

## 20. `บิดา อาชีพ` → `parent_information(FATHER).occupation`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ชุดค่า/อื่น ๆ
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** เกษตรกร/ประมง

## 21. `บิดา รายได้` → `parent_information(FATHER).monthly_income`

- **Required ตอน Import:** No
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0; ยืนยันว่าเป็นรายเดือน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1200

## 22. `บิดา สภาพ` → `parent_information(FATHER).life_status`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim; Mapping Enum
- **Validation หลัก:** ชุดค่ามาตรฐาน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** มีชีวิตอยู่

## 23. `มารดา อายุ` → `parent_information(MOTHER).age`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Integer
- **Validation หลัก:** 15–120
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 54

## 24. `มารดา อาชีพ` → `parent_information(MOTHER).occupation`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim
- **Validation หลัก:** ชุดค่า/อื่น ๆ
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** เกษตรกร/ประมง

## 25. `มารดา รายได้` → `parent_information(MOTHER).monthly_income`

- **Required ตอน Import:** No
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0; ยืนยันว่าเป็นรายเดือน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1200

## 26. `มารดา สภาพ` → `parent_information(MOTHER).life_status`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim; Mapping Enum
- **Validation หลัก:** ชุดค่ามาตรฐาน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** มีชีวิตอยู่

## 27. `สภาพบิดา-มารดา` → `education_support.parents_relationship_status`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim; Mapping Enum
- **Validation หลัก:** ชุดค่ามาตรฐาน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** อยู่ด้วยกัน

## 28. `คนออกเงินเรียน` → `education_support.tuition_payer`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Trim; Mapping Enum
- **Validation หลัก:** ชุดค่ามาตรฐาน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** บิดา-มารดา

## 29. `อุปการะ-ความเกี่ยวข้อง` → `education_support.supporter_relationship`

- **Required ตอน Import:** Conditional
- **Parsing / Normalization:** Trim
- **Validation หลัก:** จำเป็นเมื่อมีผู้อุปการะอื่น
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** ป้า

## 30. `อุปการะ-อาชีพ` → `education_support.supporter_occupation`

- **Required ตอน Import:** Conditional
- **Parsing / Normalization:** Trim
- **Validation หลัก:** จำเป็นเมื่อมีผู้อุปการะ
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** ค้าขาย

## 31. `อุปการะ-รายได้` → `education_support.supporter_monthly_income`

- **Required ตอน Import:** Conditional
- **Parsing / Normalization:** ลบ comma; Decimal
- **Validation หลัก:** >= 0; ยืนยันว่าเป็นรายเดือน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 15000

## 32. `พี่น้อง-ทำงาน` → `sibling_summaries.working_count`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Integer
- **Validation หลัก:** >= 0
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1

## 33. `พี่น้อง-ไม่ทำงาน` → `sibling_summaries.not_working_count`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Integer
- **Validation หลัก:** >= 0
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1

## 34. `พี่น้อง-เรียน` → `sibling_summaries.studying_count`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Integer
- **Validation หลัก:** >= 0
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 1

## 35. `กยศ` → `education_loan_histories.academic_year_be + amount`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Parse รูปแบบ -YYYY : amount; ลบ comma
- **Validation หลัก:** ปี 4 หลัก; amount >= 0; ไม่ซ้ำปี/โครงการ
- **การทำงานในแถวต่อเนื่อง:** อนุญาตและสร้างประวัติใหม่โดยสืบทอด student_id
- **ตัวอย่างต้นทาง:** -2565 : 66,000

## 36. `ทุน` → `scholarship_histories.academic_year_be + scholarship_name + amount`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Parse -YYYY <ชื่อทุน> : amount
- **Validation หลัก:** ปี/ชื่อทุน/จำนวนเงินต้องครบ
- **การทำงานในแถวต่อเนื่อง:** อนุญาตและสร้างประวัติใหม่โดยสืบทอด student_id
- **ตัวอย่างต้นทาง:** -2565 ทุนตัวอย่าง : 10,000

## 37. `พิกัดแผนที่บ้าน` → `address_coordinates.latitude + longitude`

- **Required ตอน Import:** No
- **Parsing / Normalization:** Split ด้วย comma; Trim; Decimal
- **Validation หลัก:** lat -90..90; lon -180..180; ต้องมาคู่กัน
- **การทำงานในแถวต่อเนื่อง:** ต้องว่าง
- **ตัวอย่างต้นทาง:** 16.3792973, 104.3854202

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [Data Dictionary](./01_Data_Dictionary.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [Value Sets](./03_Value_Sets.md)

<!-- DOC_NAV_END -->
