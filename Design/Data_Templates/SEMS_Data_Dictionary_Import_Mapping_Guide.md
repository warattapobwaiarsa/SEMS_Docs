# SEMS — Data Dictionary และ Import Column Mapping

| รายการ | รายละเอียด |
| :--- | :--- |
| Version | **v0.4** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Design Team** |
| Status | **Baseline Candidate — Pending Formal Approval** |
| Workbook | [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](./SEMS_Data_Dictionary_Import_Mapping.xlsx) |

[START HERE](../../START_HERE.md) › [🎨 Design](../README.md) › SEMS — Data Dictionary และ Import Column Mapping

## ขอบเขต

เอกสารชุดนี้เริ่มจาก **Applicant Import** ซึ่งอ้างอิงไฟล์ [`Data_import_to_web.xlsx`](./Data_import_to_web.xlsx) โดยยังไม่รวม Data Dictionary ของการประเมิน คะแนน และรายงานทั้งหมด

## ลำดับการทำงาน

1. กำหนด Target Entities
2. กำหนด Data Dictionary ของแต่ละ Field
3. จับคู่ Source Column กับ Target Field
4. กำหนด Normalize และ Validation Rule
5. แยกข้อมูลหลายค่า เช่น กยศ. และทุนย้อนหลังเป็น Child Rows
6. Apply confirmed Decision Register rules and record remaining formal evidence/measurements
7. Obtain formal baseline approval, then issue v1.0 and implement ER/Prisma/Import API

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

## Confirmed-response resolutions for the baseline candidate

1. Multiple scholarship types are allowed; key is `round_id + scholarship_type_id + student_id`.
2. Application date is Required Before Evaluation.
3. Education equipment is per semester; all amounts carry a period/unit.
4. National ID is not stored in Release 1.
5. Reference values use versioned database Code Lists.
6. Continuation rows end after UAT and the first production transition round.
7. Duplicate defaults Skip; explicit update only before Evaluation; Controlled Correction after.
8. New dates are ISO; declared legacy formats normalize in Preview.
9. Loan/scholarship histories are per-application round snapshots.
10. Required levels follow RD-028.

รายละเอียดครบถ้วนอยู่ในไฟล์ [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](./SEMS_Data_Dictionary_Import_Mapping.xlsx) และฉบับอ่านบน GitHub แยกตามชีตอยู่ที่ [`SEMS_Data_Dictionary_Import_Mapping/README.md`](./SEMS_Data_Dictionary_Import_Mapping/README.md)

## Related Documents

- Next UI flow: [Wireframe Specification](../UI_UX/SEMS_Wireframe_Specification.md#6-detailed-wireframes) — Upload, Mapping, Preview and Error Report screens

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.4 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.3 | 2026-07-24 | SEMS Design Team | Added direct navigation from import mapping guidance to the corresponding wireframe flow. |
| v0.2 | 2026-07-23 | SEMS Design Team | Added links to the GitHub-readable per-sheet Markdown conversion. |
| v0.1 | 2026-07-23 | SEMS Design Team | จัดทำ Draft ของ Data Dictionary และ Import Column Mapping สำหรับ Applicant Import |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — Applicant Import Mapping Specification](./SEMS_Applicant_Import_Mapping_Specification.md)<br>
↑ หมวดเอกสาร: [🎨 Design](../README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [Design/UI_UX](../UI_UX/README.md)

<!-- DOC_NAV_END -->
