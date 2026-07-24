# Value Sets

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary - Workbook Conversion](./README.md) › Value Sets

แหล่งข้อมูล: [`SEMS_Data_Dictionary.xlsx`](../SEMS_Data_Dictionary.xlsx), ชีต `Value Sets`

## Requirement Status

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| ข้อมูลจากไฟล์ | ปรากฏโดยตรงในไฟล์ตัวอย่างหรือ Proposal | ใช้งาน | - |
| ข้อเสนอแนะ | โครงสร้างที่เพิ่มเพื่อรองรับฐานข้อมูล/Audit/Security | ใช้งาน | - |
| ต้องยืนยัน | ต้องให้เจ้าของงานทุนยืนยันก่อน Freeze Schema | ใช้งาน | - |

## Parent Type

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| FATHER | บิดา | ใช้งาน | - |
| MOTHER | มารดา | ใช้งาน | - |

## Scholarship Record Status

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| APPLIED | สมัครทุน | เสนอ | ไฟล์ปัจจุบันยังไม่แยกสถานะ |
| RECEIVED | ได้รับทุน | เสนอ | ไฟล์ปัจจุบันยังไม่แยกสถานะ |
| UNKNOWN | ไม่ทราบ/ข้อมูลเดิมไม่ระบุ | เสนอ | - |

## Import Batch Status

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| PREVIEWED | แสดงตัวอย่างแล้ว | เสนอ | - |
| VALIDATED | ตรวจสอบผ่านและรอยืนยัน | เสนอ | - |
| IMPORTED | นำเข้าสำเร็จทั้งหมด | เสนอ | - |
| PARTIAL | นำเข้าสำเร็จบางส่วน | เสนอ | - |
| FAILED | นำเข้าไม่สำเร็จ | เสนอ | - |
| CANCELLED | ผู้ใช้ยกเลิก | เสนอ | - |

## Import Row Type

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| APPLICANT | แถวหลักที่มี student_id | เสนอ | - |
| CONTINUATION | แถวต่อเนื่องที่มีเฉพาะ กยศ./ทุน | เสนอ | - |
| BLANK | แถวว่างทั้งหมดและข้ามได้ | เสนอ | - |
| INVALID | แถวไม่ตรงรูปแบบและนำเข้าไม่ได้ | เสนอ | - |

## Validation Status

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| VALID | ไม่มีปัญหา | เสนอ | - |
| WARNING | นำเข้าได้แต่ควรตรวจสอบ | เสนอ | - |
| ERROR | ต้องแก้ไขก่อนนำเข้า | เสนอ | - |
| SKIPPED | ระบบข้ามแถว | เสนอ | - |

## Document MIME

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| application/pdf | ไฟล์ PDF | จาก Proposal | - |
| image/jpeg | รูปภาพ JPG/JPEG | จาก Proposal | - |
| image/png | รูปภาพ PNG | จาก Proposal | - |

## Coordinate Source

| Code / Value | คำอธิบาย | สถานะ | หมายเหตุ |
| --- | --- | --- | --- |
| IMPORT | นำเข้าจาก Excel/CSV | เสนอ | - |
| MANUAL | ผู้ดูแลกรอกเอง | เสนอ | - |
| MAP_PICKER | เลือกจากแผนที่ | เสนอ | - |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [Import Column Mapping](./02_Import_Column_Mapping.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [Design Decisions](./04_Design_Decisions.md)

<!-- DOC_NAV_END -->
