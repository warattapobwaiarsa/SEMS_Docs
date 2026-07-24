# 05 REFERENCE VALUES

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md) › 05 REFERENCE VALUES

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `05_REFERENCE_VALUES`

| Reference Group | Source Value | Normalized Code | Display Value | สถานะ | หมายเหตุ |
| --- | --- | --- | --- | --- | --- |
| TITLE | นาย | MR | นาย | Provisional | - |
| TITLE | นาง | MRS | นาง | Provisional | - |
| TITLE | นางสาว | MS | นางสาว | Provisional | - |
| PARENT_LIFE_STATUS | มีชีวิตอยู่ | ALIVE | มีชีวิตอยู่ | Provisional | - |
| PARENT_LIFE_STATUS | ถึงแก่กรรม | DECEASED | ถึงแก่กรรม | Provisional | - |
| PARENT_LIFE_STATUS | - | UNKNOWN | ไม่ทราบ | Provisional | ใช้เมื่อธุรกิจยืนยันให้ Normalize ค่าไม่ระบุ |
| ROW_TYPE | มีรหัสนักศึกษา | APPLICANT | Applicant Row | Design | - |
| ROW_TYPE | ไม่มีรหัสแต่มี กยศ./ทุน | CONTINUATION | Continuation Row | Legacy | - |
| ROW_TYPE | ไม่มีข้อมูลทุกคอลัมน์ | EMPTY | Empty Row | Design | ข้ามแถว |
| ADDITIONAL_INCOME | ไม่มีรายได้เสริม | FALSE | ไม่มีรายได้เสริม | Provisional | - |
| ADDITIONAL_INCOME | ข้อความอื่นที่ไม่ว่าง | TRUE | มี/อาจมีรายได้เสริม | Provisional | เก็บข้อความเดิมด้วย |
| RESIDENCE_TYPE | หอพัก มข | KKU_DORM | หอพักมหาวิทยาลัย | Provisional | ต้องรวบรวมค่าจริงเพิ่มเติม |
| RESIDENCE_TYPE | บ้านบิดา/มารดา | PARENT_HOME | บ้านบิดาหรือมารดา | Provisional | - |
| RESIDENCE_TYPE | อื่นๆ | OTHER | อื่น ๆ | Provisional | - |
| EDUCATION_FUNDER | บิดา-มารดา | PARENTS | บิดาและมารดา | Provisional | - |
| EDUCATION_FUNDER | บิดา | FATHER | บิดา | Provisional | - |
| EDUCATION_FUNDER | มารดา | MOTHER | มารดา | Provisional | - |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [04 VALIDATION RULES](./04_VALIDATION_RULES.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [06 HISTORICAL OPEN DECISIONS — RESOLUTION STATUS](./06_OPEN_DECISIONS.md)

<!-- DOC_NAV_END -->
