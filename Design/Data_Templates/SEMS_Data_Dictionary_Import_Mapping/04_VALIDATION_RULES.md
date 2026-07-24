# 04 VALIDATION RULES

| Metadata | Value |
| :--- | :--- |
| Version | **v1.0** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Status | **Reference - Converted from Workbook** |

แหล่งข้อมูล: [`SEMS_Data_Dictionary_Import_Mapping.xlsx`](../SEMS_Data_Dictionary_Import_Mapping.xlsx), ชีต `04_VALIDATION_RULES`

> **Confirmed Release 1 validation:** duplicate rows in one file are errors; existing application defaults to Skip; automatic Upsert is forbidden. Normal update is allowed only before any Evaluation and cannot change student, round or scholarship type. After an Evaluation exists, score-affecting changes require Controlled Correction. Hard Import / Required Before Evaluation / Optional field levels are defined by RD-028.

| Rule ID | ระดับ | ใช้กับ | เงื่อนไข | ผลเมื่อไม่ผ่าน | ข้อความที่แสดง | สถานะ |
| --- | --- | --- | --- | --- | --- | --- |
| VAL-001 | ERROR | รหัส, ชื่อ, สกุล, คณะ, สาขา, ชั้นปี | Hard Required ต้องไม่ว่างและไม่ใช่ '-' | Reject row | ข้อมูลบังคับไม่ครบ | Draft |
| VAL-002 | ERROR | รหัส | ห้ามมีรหัสนักศึกษาซ้ำภายในไฟล์เดียวกันใน Applicant Row | Reject duplicate rows | พบรหัสนักศึกษาซ้ำในไฟล์ | Draft |
| VAL-003 | ERROR/CHOICE | รหัส + รอบทุน | พบผู้สมัครเดิมในรอบทุน | Default Skip; Update ได้เฉพาะตามสิทธิ์และยังไม่มี Evaluation | มีข้อมูลผู้สมัครในรอบทุนแล้ว | จาก RD-018 |
| VAL-004 | ERROR | Continuation Row | แถวที่ไม่มีรหัสต้องมีเฉพาะ กยศ./ทุน และต้องมี Applicant Row ก่อนหน้า | Reject row | ไม่สามารถระบุเจ้าของประวัติได้ | Draft |
| VAL-005 | ERROR | รหัส/โทรศัพท์/เลขบัตร | ห้ามเป็น Scientific Notation หรือค่าตัวเลขที่สูญเสียหลัก | Reject field/row | ข้อมูลระบุตัวตนถูก Excel แปลงรูปแบบ | Draft |
| VAL-006 | ERROR | วันที่สมัคร | ต้อง Parse ได้จากรูปแบบที่ประกาศ | Reject row or leave null per final policy | รูปแบบวันที่ไม่ถูกต้องหรือกำกวม | Draft |
| VAL-007 | ERROR | GPA | ค่าระหว่าง 0.00 ถึง 4.00 | Reject field; block Evaluation | GPA ต้องอยู่ระหว่าง 0.00–4.00 | Draft |
| VAL-008 | ERROR | ค่าใช้จ่าย/รายได้/จำนวนเงิน | ต้องเป็นตัวเลข >= 0 | Reject field/row | จำนวนเงินต้องไม่ติดลบ | Draft |
| VAL-009 | ERROR | ชั้นปี/อายุ/จำนวนพี่น้อง | ต้องเป็นจำนวนเต็มในช่วงที่กำหนด | Reject field/row | ค่าต้องเป็นจำนวนเต็มที่ถูกต้อง | Draft |
| VAL-010 | WARNING | คำนำหน้า/ที่พัก/สถานะครอบครัว/ผู้จ่ายค่าเรียน | ค่าไม่อยู่ใน Reference Values | Import raw value หรือให้ผู้ใช้เลือกแก้ | พบค่าที่ไม่อยู่ในรายการมาตรฐาน | รอยืนยัน Reference |
| VAL-011 | ERROR | อีเมล | รูปแบบอีเมลไม่ถูกต้อง | Reject field or row per policy | รูปแบบอีเมลไม่ถูกต้อง | Draft |
| VAL-012 | ERROR | โทรศัพท์ | หลัง Normalize ต้องมี 9–15 หลัก | Reject field or row per policy | หมายเลขโทรศัพท์ไม่ถูกต้อง | Draft |
| VAL-013 | WARNING | กยศ | แยกปีและจำนวนเงินไม่ได้ แต่ยังมี raw_text | เก็บ raw_text; ไม่สร้าง structured values | ไม่สามารถแยกรายละเอียด กยศ. ได้ทั้งหมด | Draft |
| VAL-014 | WARNING | ทุน | แยกปี ชื่อทุน หรือจำนวนเงินไม่ได้ แต่ยังมี raw_text | เก็บ raw_text; ไม่สร้าง structured values บางส่วน | ไม่สามารถแยกรายละเอียดทุนได้ทั้งหมด | Draft |
| VAL-015 | WARNING/ERROR | พิกัดแผนที่บ้าน | ต้องเป็น URL หรือ latitude,longitude ที่อยู่ในช่วง | เก็บ raw; structured fields เป็น NULL หรือ Reject ตาม policy | พิกัดหรือลิงก์แผนที่ไม่ถูกต้อง | Draft |
| VAL-016 | NORMALIZE | ทุกคอลัมน์ | Trim; ช่องว่างและ '-' เป็น NULL ยกเว้นฟิลด์ที่ '-' มีความหมายจริง | Normalize | - | Draft |
| VAL-017 | ERROR | Header | Header ที่จำเป็นต้องพบครบ หรือจับคู่ผ่าน Alias ได้ | Block Preview confirmation | ไม่พบคอลัมน์ที่จำเป็น | Draft |
| VAL-018 | ERROR | Update Import | ห้ามแก้ฟิลด์สำคัญผ่าน Import เมื่อมี Evaluation แล้ว | Reject update | ผู้สมัครเริ่มถูกประเมินแล้ว ไม่อนุญาตให้อัปเดตด้วย Import | จาก RD-018 |
