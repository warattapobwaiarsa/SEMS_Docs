# 06 HISTORICAL OPEN DECISIONS — RESOLUTION STATUS

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md) › 06 HISTORICAL OPEN DECISIONS — RESOLUTION STATUS

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `06_OPEN_DECISIONS`

| Decision ID | ประเด็นที่ต้องยืนยันก่อน Baseline | ข้อเสนอปัจจุบัน | ผลกระทบ | Owner | สถานะ |
| --- | --- | --- | --- | --- | --- |
| DD-OD-001 | หนึ่งคนสมัครหลายประเภททุนในรอบเดียวได้หรือไม่ | Yes; business key `round_id + scholarship_type_id + student_id` | Unique Constraint / Import Duplicate | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-002 | วันที่สมัครเป็นข้อมูลบังคับหรือไม่ | Required Before Evaluation | Validation | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-003 | ค่าอุปกรณ์การศึกษาเป็นต่อเดือน ต่อภาค หรือยอดรวม | ต่อภาคการศึกษา; ทุก amount มี period/unit | ชื่อ Field / รายงาน / เกณฑ์ | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-004 | ต้องจัดเก็บเลขบัตรประชาชนใน SEMS หรือไม่ | No storage in Release 1 | PDPA / Security / Database | เจ้าของข้อมูล | Confirmed Response — Pending Formal Record |
| DD-OD-005 | Reference Values ทางการ | Versioned DB Code Lists; used values become Inactive, never deleted | Validation / UI Filter | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-006 | จะรองรับ Continuation Row ถึงเมื่อใด | UAT and first production transition round only | Importer Complexity | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |
| DD-OD-007 | Duplicate กับข้อมูลเดิมอนุญาต Update ฟิลด์ใดบ้าง | Default Skip; explicit update before Evaluation; Controlled Correction after | Data Integrity / Audit | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-008 | รูปแบบวันที่และโทรศัพท์ที่รองรับ | ISO/Text new template; declared legacy formats normalize in Preview | Validation / Test Cases | งานทุน/ทีมพัฒนา | Confirmed Response — Pending Formal Record |
| DD-OD-009 | ประวัติ กยศ./ทุนเป็นข้อมูลระดับ Applicant หรือ Snapshot รายรอบ | Snapshot per application/round; one aggregated loan amount per academic year | Data Model / Duplicate | งานทุน | Confirmed Response — Pending Formal Record |
| DD-OD-010 | Hard Required และ Required before Evaluation | Three levels defined in RD-028 | Import Acceptance | งานทุน/ผู้ประเมิน | Confirmed Response — Pending Formal Record |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [05 REFERENCE VALUES](./05_REFERENCE_VALUES.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ ขั้นตอนถัดไป: ตรวจสถานะมติแล้วอัปเดต [SEMS — Data Dictionary และ Import Column Mapping](../SEMS_Data_Dictionary_Import_Mapping_Guide.md)

<!-- DOC_NAV_END -->
