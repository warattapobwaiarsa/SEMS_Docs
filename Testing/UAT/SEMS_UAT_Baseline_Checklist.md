# Checklist การทดสอบการยอมรับ Requirement Baseline ของ SEMS

| Metadata | Value |
|---|---|
| Version | **v0.3** |
| Last Updated | **2026-07-24** |
| Status | **Draft — Participants and Dates Pending Formal Record** |

บทบาทขั้นต่ำตาม RD-042 ได้แก่ ผู้ประเมินอย่างน้อย 2 คน ผู้ใช้จาก Scholarship Office/`ADMIN` 2 คน และผู้แทน IT/infrastructure 1 คนสำหรับสถานการณ์ deployment/backup ห้ามกรอกชื่อหรือวันที่โดยไม่มีบันทึกจริง

- [ ] ใบสมัครหลายประเภททุนและการจัดการ business-key triplet ซ้ำ
- [ ] Blocking validation ก่อนเปิดรอบและการ Import ขณะรอบเป็น `OPEN`
- [ ] การแก้ไขแบบควบคุม (Controlled Correction) และ identity triplet ที่แก้ไม่ได้
- [ ] การยกเลิก `DRAFT`, การอนุมัติ Reopen และการเก็บ revision เดิม
- [ ] Embedded Point, ค่าเฉลี่ยผู้ประเมิน 2/3 คน และ `ROUND_HALF_UP`
- [ ] การปิดรอบเมื่อผลไม่ครบ, การ Reopen รอบ `CLOSED` และการปฏิเสธรอบ `ARCHIVED`
- [ ] รายงานภายใน/ปกปิดข้อมูล และ snapshot แบบ Final/Superseded
- [ ] การ provision บัญชี การแยกข้อมูลผู้ประเมิน และการหมดอายุของ session
- [ ] ขนาดไฟล์ Quarantine การสแกน malware และ secure download
- [ ] การ restore/reconcile backup ร่วมกับผู้แทน IT
- [ ] ไม่มี National ID ในทุก flow ของ Release 1

| บทบาท | ชื่อ | วันที่ | หลักฐาน/ผล |
|---|---|---|---|
| Evaluator 1 | Pending Formal Record | Pending Formal Record | Pending |
| Evaluator 2 | Pending Formal Record | Pending Formal Record | Pending |
| Scholarship Office/Admin 1 | Pending Formal Record | Pending Formal Record | Pending |
| Scholarship Office/Admin 2 | Pending Formal Record | Pending Formal Record | Pending |
| IT/Infrastructure | Pending Formal Record | Pending Formal Record | Pending |

## Related Documents

- Next: [Deployment Overview](../../Deployment/README.md)
- Pending evidence: [Requirement Baseline Approval Record](../../Requirements/Approvals/Requirement_Baseline_Approval_Record.md)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.2 | 2026-07-24 | SEMS QA Team | Added lifecycle navigation to deployment context and the pending requirement-baseline approval record. |
| v0.1 | 2026-07-24 | SEMS QA Team | Prepared confirmed-response UAT checklist without inventing participants or dates. |
