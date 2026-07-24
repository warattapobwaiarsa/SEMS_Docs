# SEMS — Data Dictionary & Import Column Mapping (Applicant Import)

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

[START HERE](../../../START_HERE.md) › [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md) › SEMS — Data Dictionary & Import Column Mapping (Applicant Import)

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `00_README`

| รายการ | รายละเอียด |
| --- | --- |
| Version | Draft v0.1 |
| Scope | Applicant Import จาก Data_import_to_web(1).xlsx |
| Purpose | กำหนดโครงสร้างข้อมูลเป้าหมาย การจับคู่คอลัมน์ และ Validation ก่อนออกแบบ ER Diagram/API |
| Source | SEMS Requirement Decision Register Answered, Proposal, Data_import_to_web(1).xlsx, Criteria(1).xlsx |
| Key Business Rule | Application uses `round_id + scholarship_type_id + student_id` as the business key |
| Import Strategy | Preview → Validate → Confirm → Transactional Import → Audit |
| Legacy Rule | Continuation Row is limited to UAT and the first production transition round |
| Null Rule | ช่องว่างและ '-' เป็น NULL; ค่า 0 ต้องเก็บเป็น 0 ไม่ใช่ NULL |
| Identifier Rule | รหัสนักศึกษาและโทรศัพท์อ่านเป็น Text; Release 1 ไม่รับหรือเก็บ national ID |
| Next Review | Formal baseline approval and pending operational measurements/records |
| Next Artifact | ER Diagram, Prisma Schema และ Import Template ฉบับใหม่ |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
↑ หมวดเอกสาร: [SEMS Data Dictionary & Import Mapping - Workbook Conversion](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../../../START_HERE.md)<br>
→ อ่านต่อ: [01 ENTITY MODEL](./01_ENTITY_MODEL.md)

<!-- DOC_NAV_END -->
