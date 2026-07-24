# 01 ENTITY MODEL

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md) › 01 ENTITY MODEL

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `01_ENTITY_MODEL`

| Entity | หน้าที่ | Parent / Related Entity | Cardinality | Key / Creation Rule | หมายเหตุ |
| --- | --- | --- | --- | --- | --- |
| import_batches | ประวัติการนำเข้า 1 ครั้ง | scholarship_rounds | N:1 | ระบบสร้างเมื่อผู้ดูแลเริ่ม Import | เก็บชื่อไฟล์ ผู้ดำเนินการ เวลา สถานะ และผลรวมการนำเข้า |
| import_rows | ข้อมูลดิบและผลตรวจสอบรายแถว | import_batches | N:1 | หนึ่งรายการต่อแถวจากไฟล์ต้นทาง | เก็บ raw payload เพื่อ Audit และรองรับ Continuation Row |
| applicants | ข้อมูลระบุตัวนักศึกษาที่ใช้ข้ามใบสมัคร | - | - | รหัสนักศึกษาเป็น Business Identifier | UUID เป็น Primary Key; Release 1 ไม่เก็บเลขบัตรประชาชน |
| scholarship_types | ประเภททุนที่ Admin จัดการในแต่ละรอบ | scholarship_rounds | N:1 | Unique: round_id + code | มีเพดานจำนวนเงินและสถานะ Active/Inactive |
| round_applications | ใบสมัครอิสระต่อรอบและประเภททุน | applicants / scholarship_rounds / scholarship_types | N:1 | Unique: round_id + scholarship_type_id + student_id | เก็บ Snapshot คณะ สาขา ชั้นปี GPA เอกสาร Evaluation และ Result Summary ของใบสมัครนั้น |
| application_parents | ข้อมูลบิดาและมารดาของผู้สมัครในรอบทุน | round_applications | N:1 | parent_type = FATHER หรือ MOTHER | แยกเป็นแถวเพื่อไม่ต้องสร้างคอลัมน์ซ้ำในฐานข้อมูล |
| application_guardians | ข้อมูลผู้อุปการะหรือผู้ดูแล | round_applications | N:1 | สร้างเมื่อมีข้อมูล | เก็บความเกี่ยวข้อง อาชีพ และรายได้ |
| student_loan_histories | Snapshot ประวัติ กยศ. ต่อใบสมัคร | round_applications | N:1 | หนึ่งยอดรวมต่อปีการศึกษา | Template ใหม่แยก Sheet; Legacy เฉพาะ UAT และ production transition round แรก |
| scholarship_histories | Snapshot ประวัติทุนต่อใบสมัคร | round_applications | N:1 | หนึ่งแถวต่อหนึ่งทุน | แยกปี ชื่อทุน จำนวนเงิน และข้อความดิบ |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — Data Dictionary & Import Column Mapping (Applicant Import)](./00_README.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [02 DATA DICTIONARY](./02_DATA_DICTIONARY.md)

<!-- DOC_NAV_END -->
