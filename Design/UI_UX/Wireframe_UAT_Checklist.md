# SEMS Wireframe UAT Checklist

| Metadata | Value |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Design Team** |
| Status | **Draft — Ready for UAT** |

**วัตถุประสงค์:** ใช้ให้ตัวแทนผู้ใช้งานตรวจ Wireframe ก่อนเริ่มพัฒนา Frontend
**ผู้ทดสอบที่แนะนำ:** Admin อย่างน้อย 2 คน และ Evaluator อย่างน้อย 2 คน

## วิธีทดสอบ

1. ให้ผู้ทดสอบทำ Task โดยผู้ดำเนินการไม่บอกตำแหน่งปุ่มล่วงหน้า
2. บันทึกเวลาที่ใช้ จุดที่หยุดคิด จุดที่คลิกผิด และคำถามที่ผู้ทดสอบถาม
3. หลังจบแต่ละ Task ให้คะแนนความง่าย 1-5
4. แยกข้อเสนอแนะเป็น Critical, Major, Minor และ Nice-to-have

## A. Admin Tasks

| ID | Task | Expected Outcome | ผ่าน/ไม่ผ่าน | เวลา | คะแนน 1-5 | หมายเหตุ |
|---|---|---|---|---|---|---|
| A-01 | Login ด้วย KKU Account | เข้าสู่ Admin Dashboard | | | | |
| A-02 | สร้างรอบทุนใหม่ | รอบทุนอยู่สถานะ Draft | | | | |
| A-03 | อัปโหลดไฟล์ Data_import_to_web | ระบบอ่าน Header และไปหน้า Mapping | | | | |
| A-04 | Map คอลัมน์ `ชือ` เป็น `first_name` | Mapping ถูกต้องและแสดง Conversion | | | | |
| A-05 | ตรวจ continuation rows ของ กยศ./ทุน | ระบบรวมแถวต่อเนื่องกับผู้สมัครแถวหลัก | | | | |
| A-06 | ตรวจ Import Error | พบเลขแถว Error Code และวิธีแก้ | | | | |
| A-07 | ยืนยัน Import | เห็นจำนวนผู้สมัครนำเข้าสำเร็จ | | | | |
| A-08 | เปิดรายละเอียดผู้สมัคร | เห็นข้อมูล ครอบครัว ประวัติ และเอกสาร | | | | |
| A-09 | สร้าง/ตรวจชุดเกณฑ์ | คะแนนเต็มและ Required ถูกต้อง | | | | |
| A-10 | เปิดรอบทุน | Evaluator สามารถเห็นรายชื่อผู้สมัคร | | | | |
| A-11 | ตรวจผู้สมัครที่ Submitted 2/3 | สถานะ Minimum Complete และมีคะแนนสรุป | | | | |
| A-12 | ตรวจหลังผู้ประเมินคนที่ 3 Submit | สถานะ Fully Complete และคะแนนสรุปคำนวณใหม่ | | | | |
| A-13 | ปิดรอบทุน | เห็น Finalized และ Closed Incomplete ก่อนยืนยัน | | | | |
| A-14 | Export Excel/CSV | ได้รายงานตาม Filter และมีประวัติ Export | | | | |

## B. Evaluator Tasks

| ID | Task | Expected Outcome | ผ่าน/ไม่ผ่าน | เวลา | คะแนน 1-5 | หมายเหตุ |
|---|---|---|---|---|---|---|
| E-01 | Login ด้วย KKU Account | เข้าสู่หน้าเลือกผู้สมัคร | | | | |
| E-02 | ค้นหาผู้สมัครด้วยรหัส/ชื่อ | พบผู้สมัครและเห็นจำนวนผู้ประเมิน | | | | |
| E-03 | เลือกผู้สมัคร | สร้าง Evaluation สถานะ Draft | | | | |
| E-04 | ดูข้อมูลและเอกสาร | เข้าถึงเฉพาะผู้สมัครที่เลือก | | | | |
| E-05 | ให้คะแนนทุกเกณฑ์ | ระบบตรวจ min/max และ Required | | | | |
| E-06 | บันทึก Draft | เห็นเวลาบันทึกล่าสุดและกลับมาทำต่อได้ | | | | |
| E-07 | Review Before Submit | เห็นคะแนน ความคิดเห็น และคะแนนรวมครบ | | | | |
| E-08 | ยืนยัน Submit | สถานะเป็น Submitted และแก้ไม่ได้ | | | | |
| E-09 | พยายามเลือกผู้สมัครเดิมซ้ำ | ระบบปฏิเสธและพาไป Evaluation เดิม | | | | |
| E-10 | พยายามเลือกผู้สมัคร 3/3 | ปุ่มถูกปิดหรือระบบแจ้งว่าเต็ม | | | | |

## C. Questions After Testing

ให้คะแนน 1-5 และบันทึกเหตุผล

| คำถาม | คะแนน | เหตุผล/ข้อเสนอแนะ |
|---|---|---|
| เมนูและคำศัพท์เข้าใจง่าย | | |
| ขั้นตอน Import ต่อเนื่องและไม่สับสน | | |
| หน้า Column Mapping ใช้งานง่าย | | |
| Error Report บอกวิธีแก้เพียงพอ | | |
| รายชื่อและรายละเอียดผู้สมัครหาได้ง่าย | | |
| หน้าประเมินหน้าเดียวช่วยลดการสลับหน้าจอ | | |
| การบันทึก Draft และ Submit ชัดเจน | | |
| สถานะ 0/3, 1/3, 2/3, 3/3 เข้าใจง่าย | | |
| หน้าสรุปผลตอบคำถามของงานทุน | | |
| Export รายงานมีตัวเลือกเพียงพอ | | |
| ความพึงพอใจโดยรวม | | |

## D. Issue Log

| Issue ID | Screen | รายละเอียด | Severity | ข้อเสนอแก้ไข | ผู้รับผิดชอบ | สถานะ |
|---|---|---|---|---|---|---|
| UI-001 | | | Critical/Major/Minor/Nice-to-have | | | Open |

## E. Approval

- [ ] Admin Representative Approved
- [ ] Evaluator Representative Approved
- [ ] Requirement Owner Approved
- [ ] Open Decisions ได้รับคำตอบหรือมีผู้รับผิดชอบ/กำหนดเวลา
- [ ] Critical และ Major Issues ถูกแก้ใน Wireframe รุ่นถัดไป

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v1.1 | 2026-07-23 | SEMS Design Team | Removed trailing whitespace for automated documentation checks; approval remains pending. |
| v1.0 | 2026-07-23 | SEMS Design Team | Initial wireframe UAT checklist draft. |
