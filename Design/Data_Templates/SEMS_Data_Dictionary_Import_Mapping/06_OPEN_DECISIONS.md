# 06 OPEN DECISIONS

| Metadata | Value |
| :--- | :--- |
| Version | **v1.0** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `06_OPEN_DECISIONS`

| Decision ID | ประเด็นที่ต้องยืนยันก่อน Baseline | ข้อเสนอปัจจุบัน | ผลกระทบ | Owner | สถานะ |
| --- | --- | --- | --- | --- | --- |
| DD-OD-001 | หนึ่งคนสมัครหลายประเภททุนในรอบเดียวได้หรือไม่ | หากได้ ให้ Business Key เป็น round_id + scholarship_type_id + student_id | Unique Constraint / Import Duplicate | งานทุน | Open |
| DD-OD-002 | วันที่สมัครเป็นข้อมูลบังคับหรือไม่ | Recommended; ว่างได้ตอน Import หากกระบวนการไม่ใช้ | Validation | งานทุน | Open |
| DD-OD-003 | ค่าอุปกรณ์การศึกษาเป็นต่อเดือน ต่อภาค หรือยอดรวม | เพิ่มหน่วยเวลาใน Template ใหม่ | ชื่อ Field / รายงาน / เกณฑ์ | งานทุน | Open |
| DD-OD-004 | ต้องจัดเก็บเลขบัตรประชาชนใน SEMS หรือไม่ | ไม่อยู่ใน Import หลัก; หากจำเป็นให้แยก Restricted Flow และเข้ารหัส | PDPA / Security / Database | เจ้าของข้อมูล | Open |
| DD-OD-005 | Reference Values ทางการของที่พัก สถานะครอบครัว และผู้จ่ายค่าเรียน | รวบรวมค่าจริงและอนุมัติ Code List | Validation / UI Filter | งานทุน | Open |
| DD-OD-006 | จะรองรับ Continuation Row ถึงเมื่อใด | Template ใหม่แยก Sheet; Legacy รองรับช่วงเปลี่ยนผ่าน | Importer Complexity | งานทุน/ทีมพัฒนา | Open |
| DD-OD-007 | Duplicate กับข้อมูลเดิมอนุญาต Update ฟิลด์ใดบ้าง | Default Skip; Update เฉพาะก่อนมี Evaluation | Data Integrity / Audit | งานทุน | Open |
| DD-OD-008 | รูปแบบวันที่และโทรศัพท์ที่ต้องรองรับอย่างเป็นทางการ | Template ISO และ Text; Legacy parser เฉพาะรูปแบบประกาศ | Validation / Test Cases | งานทุน/ทีมพัฒนา | Open |
| DD-OD-009 | ประวัติ กยศ./ทุนเป็นข้อมูลระดับ Applicant หรือ Snapshot รายรอบ | เก็บระดับ Applicant พร้อม source import และแสดงในทุกรอบ | Data Model / Duplicate | งานทุน | Open |
| DD-OD-010 | Hard Required และ Required before Evaluation รายการสุดท้าย | ใช้รายการใน Draft นี้เป็นฐานประชุม | Import Acceptance | งานทุน/ผู้ประเมิน | Open |
