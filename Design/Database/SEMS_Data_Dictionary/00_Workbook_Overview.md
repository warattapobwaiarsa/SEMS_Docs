# Workbook Overview

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary - Workbook Conversion](./README.md) › Workbook Overview

แหล่งข้อมูล: [`SEMS_Data_Dictionary.xlsx`](../SEMS_Data_Dictionary.xlsx), ชีต `README`

ขอบเขต: โครงสร้างข้อมูลผู้สมัครและกระบวนการนำเข้า จากไฟล์ Data_import_to_web และข้อเสนอโครงการ SEMS

## สรุป

| รายการ | ค่า |
| --- | --- |
| จำนวนฟิลด์ทั้งหมด | 115 |
| จำนวนกลุ่มข้อมูล | 10 |
| ข้อมูลจากไฟล์/Proposal | 44 |
| ข้อเสนอแนะ | 62 |
| ต้องยืนยัน | 9 |

## สถานะข้อกำหนด

| สถานะ | ความหมาย |
| --- | --- |
| ข้อมูลจากไฟล์ | ข้อมูลปรากฏในไฟล์ตัวอย่าง |
| ข้อมูลจากไฟล์/Proposal | สอดคล้องทั้งไฟล์ตัวอย่างและ Proposal |
| ข้อเสนอแนะ | เพิ่มเพื่อให้ Schema ใช้งานจริง ตรวจสอบย้อนหลัง และปลอดภัย |
| ต้องยืนยัน | ต้องยืนยันกับงานทุนก่อน Freeze Schema |
| Conditional | บังคับเมื่อเข้าเงื่อนไข เช่น มีผู้อุปการะ หรือมีพิกัดหนึ่งค่า |
| Yes (System) | ระบบสร้างหรือกำหนดค่าอัตโนมัติ ไม่ได้มาจากผู้ใช้ |

## กฎสำคัญสำหรับโครงสร้างไฟล์ตัวอย่าง

1. แถวที่มีรหัสนักศึกษาเป็นแถวหลักของผู้สมัคร
2. แถวที่รหัสนักศึกษาว่าง แต่มีข้อมูล กยศ. หรือทุน เป็นแถวต่อเนื่องของผู้สมัครก่อนหน้า
3. แถวต่อเนื่องที่ไม่มีผู้สมัครก่อนหน้าเป็น Error
4. กยศ. หนึ่งปีและทุนหนึ่งรายการต้องถูกแยกเป็น Child Record
5. แถวว่างทั้งหมดให้ข้าม แต่ควรนับจำนวนเพื่อ Audit
6. ไฟล์จริงควรผ่าน Preview และ Validation ก่อนยืนยันนำเข้า

## แหล่งอ้างอิง

| แหล่งอ้างอิง | รายละเอียด |
| --- | --- |
| Data_import_to_web(1).xlsx | หัวคอลัมน์จริง 37 คอลัมน์และตัวอย่างแถวต่อเนื่อง |
| SEMS-project-proposal(1).pdf | ขอบเขต Import, Applicant, Document, History, Validation และ Data Protection |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS Data Dictionary - Workbook Conversion](./README.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [Data Dictionary](./01_Data_Dictionary.md)

<!-- DOC_NAV_END -->
