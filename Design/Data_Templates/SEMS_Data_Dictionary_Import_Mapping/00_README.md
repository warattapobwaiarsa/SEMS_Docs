# SEMS — Data Dictionary & Import Column Mapping (Applicant Import)

| Metadata | Value |
| :--- | :--- |
| Version | **v1.0** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `00_README`

| รายการ | รายละเอียด |
| --- | --- |
| Version | Draft v0.1 |
| Scope | Applicant Import จาก Data_import_to_web(1).xlsx |
| Purpose | กำหนดโครงสร้างข้อมูลเป้าหมาย การจับคู่คอลัมน์ และ Validation ก่อนออกแบบ ER Diagram/API |
| Source | SEMS Requirement Decision Register Answered, Proposal, Data_import_to_web(1).xlsx, Criteria(1).xlsx |
| Key Business Rule | ผู้สมัครในรอบทุนใช้ round_id + student_id เป็น Business Key (รอยืนยันกรณีหลายประเภททุน) |
| Import Strategy | Preview → Validate → Confirm → Transactional Import → Audit |
| Legacy Rule | Continuation Row อนุญาตเฉพาะแถวที่มี กยศ./ทุนและผูกกับ Applicant Row ก่อนหน้า |
| Null Rule | ช่องว่างและ '-' เป็น NULL; ค่า 0 ต้องเก็บเป็น 0 ไม่ใช่ NULL |
| Identifier Rule | รหัสนักศึกษา โทรศัพท์ และเลขบัตรต้องอ่านเป็น Text และห้าม Scientific Notation |
| Next Review | ยืนยัน Open Decisions ใน Sheet 06 ก่อนล็อก Baseline v1.0 |
| Next Artifact | ER Diagram, Prisma Schema และ Import Template ฉบับใหม่ |
