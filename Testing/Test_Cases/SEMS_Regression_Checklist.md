# SEMS Regression Checklist

| Metadata | Value |
| :--- | :--- |
| Version | **v0.1** |
| Last Updated | **2026-07-23** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

ใช้ checklist นี้หลัง merge feature สำคัญ แก้ defect P0/P1 เปลี่ยน schema หรือก่อน release

## Smoke — ทุก Build

- [ ] Admin login/logout สำเร็จ
- [ ] Evaluator login/logout สำเร็จ
- [ ] Inactive account เข้าไม่ได้
- [ ] Admin เปิดรายการ round ได้
- [ ] Evaluator เห็นเฉพาะ Open round
- [ ] Import valid file และ preview ได้
- [ ] Evaluator เลือก applicant และสร้าง Draft ได้
- [ ] Save Draft แล้วเปิดกลับมาได้
- [ ] Submit คนที่ 1 แล้ว state=In Progress
- [ ] Submit คนที่ 2 แล้ว state=Minimum Complete
- [ ] Submit คนที่ 3 แล้ว state=Fully Complete และ summary เปลี่ยน
- [ ] Export Excel/CSV ได้โดย Admin

## P0 Data Integrity

- [ ] evaluator เดิมเลือกซ้ำไม่ได้
- [ ] evaluator คนที่ 4 เลือกไม่ได้
- [ ] concurrent requests ไม่ทำ active evaluations >3
- [ ] double-click ไม่สร้าง duplicate
- [ ] cancelled evaluation ไม่ถูกนับและคืน slot
- [ ] Result Summary มี 1 row ต่อ applicant/round
- [ ] Draft ไม่เข้า score/dashboard/export
- [ ] third submit recompute ถูกต้อง
- [ ] close complete → Finalized
- [ ] close incomplete → Closed Incomplete/no final score

## Import

- [ ] required field error มี row/column/code
- [ ] GPA boundaries
- [ ] Buddhist date conversion
- [ ] student_id duplicate
- [ ] coordinate validation
- [ ] continuation row grouping
- [ ] orphan continuation rejected
- [ ] confirm import ไม่ duplicate เมื่อ retry
- [ ] ImportBatch counts reconcile

## RBAC/Security

- [ ] evaluator เข้า Admin API ไม่ได้
- [ ] evaluator แก้/submit evaluation ผู้อื่นไม่ได้
- [ ] evaluator เปิด document ของ applicant ที่ไม่ได้เลือกไม่ได้
- [ ] direct storage path เข้าไม่ได้
- [ ] submitted result read-only
- [ ] no token/secret in logs
- [ ] API errors ไม่มี stack trace/internal path

## Criteria/Scoring

- [ ] criteria max total=100 สำหรับ version ตัวอย่าง
- [ ] min/max score boundaries
- [ ] required criteria ก่อน submit
- [ ] server recalculates evaluator total
- [ ] criteria locked/versioned หลังเริ่มใช้
- [ ] rounding ตรง approved rule ทุก layer

## Dashboard/Report

- [ ] submitted buckets 0/1/2/3 sum to total applicants
- [ ] state buckets sum to total applicants
- [ ] score visualization uses Submitted only
- [ ] Excel and CSV row count/key/value match DB
- [ ] Thai text/comments encoded correctly
- [ ] export audit event exists

## Deployment/Recovery

- [ ] migration clean database สำเร็จ
- [ ] migration existing test database สำเร็จ
- [ ] seed repeatable
- [ ] constraints/indexes อยู่ครบหลัง migration
- [ ] backup/restore retains evaluations, summary, audit and document references
- [ ] environment secrets ไม่อยู่ใน source/build artifact
