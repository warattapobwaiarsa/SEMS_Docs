# SEMS — Data Dictionary และ Import Column Mapping

| รายการ | รายละเอียด |
| :--- | :--- |
| Version | **v0.2** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Design Team** |
| Status | **Draft — Pre-Baseline** |
| Workbook | [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](./SEMS_Data_Dictionary_Import_Mapping.xlsx) |

## ขอบเขต

เอกสารชุดนี้เริ่มจาก **Applicant Import** ซึ่งอ้างอิงไฟล์ [`Data_import_to_web.xlsx`](./Data_import_to_web.xlsx) โดยยังไม่รวม Data Dictionary ของการประเมิน คะแนน และรายงานทั้งหมด

## ลำดับการทำงาน

1. กำหนด Target Entities
2. กำหนด Data Dictionary ของแต่ละ Field
3. จับคู่ Source Column กับ Target Field
4. กำหนด Normalize และ Validation Rule
5. แยกข้อมูลหลายค่า เช่น กยศ. และทุนย้อนหลังเป็น Child Rows
6. ยืนยัน Open Decisions
7. ล็อก Baseline v1.0 แล้วนำไปทำ ER Diagram, Prisma Schema และ Import API

## Target Entities

| Entity | หน้าที่ |
|---|---|
| `import_batches` | เก็บประวัติการนำเข้าหนึ่งครั้ง |
| `import_rows` | เก็บข้อมูลดิบและผลตรวจสอบรายแถว |
| `applicants` | ข้อมูลระบุตัวผู้สมัครที่ใช้ข้ามรอบทุน |
| `round_applications` | Snapshot ข้อมูลผู้สมัครในรอบทุน |
| `application_parents` | ข้อมูลบิดาและมารดา |
| `application_guardians` | ข้อมูลผู้อุปการะ |
| `student_loan_histories` | ประวัติ กยศ. แบบหลายรายการ |
| `scholarship_histories` | ประวัติทุนย้อนหลังแบบหลายรายการ |

## กฎสำคัญของ Mapping

- `รหัส` ต้องอ่านเป็น Text และใช้ร่วมกับ `round_id` เป็น Business Key
- `ลำดับ` ใช้เพื่อแสดงผลและ Audit เท่านั้น ไม่ใช้เป็น Key
- โทรศัพท์และเลขบัตรต้องห้าม Scientific Notation
- ช่องว่างและ `-` แปลงเป็น `NULL`; ค่า `0` ต้องคงเป็นศูนย์
- `กยศ` และ `ทุน` ไม่ควรเก็บในคอลัมน์ข้อความเดียวในฐานข้อมูล แต่แยกเป็นหลายแถว
- Continuation Row รองรับเฉพาะ Legacy Import และต้องผูกกับ Applicant Row ก่อนหน้าได้แน่นอน
- รอบทุน (`round_id`) ให้ผู้ดูแลเลือกจากหน้าจอก่อน Import ไม่ต้องกรอกซ้ำในไฟล์
- ข้อมูลดิบทุกแถวควรเก็บใน `import_rows.raw_payload` เพื่อ Audit

## จุดที่ต้องยืนยันก่อน Baseline

1. ผู้สมัครหนึ่งคนสมัครหลายประเภททุนในรอบเดียวได้หรือไม่
2. วันที่สมัครเป็น Required หรือไม่
3. ค่าอุปกรณ์การศึกษาเป็นต่อเดือน ต่อภาค หรือยอดรวม
4. ต้องจัดเก็บเลขบัตรประชาชนหรือไม่
5. Reference Values ทางการ
6. ระยะเวลารองรับ Continuation Row
7. Duplicate Import อัปเดตฟิลด์ใดได้บ้าง
8. รูปแบบวันที่และโทรศัพท์ที่รองรับ
9. ประวัติ กยศ./ทุนเป็นระดับ Applicant หรือ Snapshot ต่อรอบ
10. รายการ Hard Required สุดท้าย

รายละเอียดครบถ้วนอยู่ในไฟล์ [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](./SEMS_Data_Dictionary_Import_Mapping.xlsx) และฉบับอ่านบน GitHub แยกตามชีตอยู่ที่ [`SEMS_Data_Dictionary_Import_Mapping/README.md`](./SEMS_Data_Dictionary_Import_Mapping/README.md)

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.2 | 2026-07-23 | SEMS Design Team | Added links to the GitHub-readable per-sheet Markdown conversion. |
| v0.1 | 2026-07-23 | SEMS Design Team | จัดทำ Draft ของ Data Dictionary และ Import Column Mapping สำหรับ Applicant Import |
