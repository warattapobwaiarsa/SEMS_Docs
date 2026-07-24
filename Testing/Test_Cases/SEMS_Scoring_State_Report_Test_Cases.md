# SEMS Scoring, State, Dashboard and Report Test Cases

| Metadata | Value |
| :--- | :--- |
| Version | **v0.5** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

[START HERE](../../START_HERE.md) › [🧪 Testing](../README.md) › SEMS Scoring, State, Dashboard and Report Test Cases

## 1. Criteria Baseline

Criteria sample มีคะแนนเต็มรวม 100 คะแนน โดย option ที่เป็น `-` ใช้แทนไม่มีค่า/ไม่เลือกและไม่ควรถือเป็นคะแนน valid สำหรับ criterion ที่บังคับตอน Submit

| No. | Criterion | Max | ตัวอย่างค่าคะแนน |
|---:|---|---:|---|
| 1 | ค่าเทอม | 10 | 10, 5, 0 |
| 2 | ค่าใช้จ่ายประจำวัน: แหล่งส่งเสีย | 10 | 10, 5, 0 |
| 3 | ทำงานพิเศษ | 10 | 10, 5, 0 |
| 4 | การนำทุนไปใช้ประโยชน์ | 20 | 20, 15, 10, 5 |
| 5 | ค่าใช้จ่ายประจำวัน: จำนวนเงิน | 10 | 10, 5, 0 |
| 6 | ค่าที่พัก | 10 | 10, 5, 0 |
| 7 | การเดินทางมาเรียน | 5 | 5, 2, 0 |
| 8 | ผลการเรียน | 5 | 5, 3, 1, 0 |
| 9 | ดุลพินิจอาจารย์ | 10 | 0–10 ตาม rule |
| 10 | ส่วนร่วมกับคณะ/มหาวิทยาลัย | 10 | 10 หรือค่าตาม criteria version |

## 2. Evaluator Score Tests

### SCR-D-001 All Maximum

**ข้อมูลนำเข้า (Input):** ทุก criterion = max

**ผลที่คาดหวัง (Expected):** evaluator total = 100

### SCR-D-002 All Minimum

**ข้อมูลนำเข้า (Input):** ทุก criterion = min

**ผลที่คาดหวัง (Expected):** evaluator total = 5 เพราะ `CRT-04` มีคะแนนต่ำสุด 5 และทุกเกณฑ์บังคับ

### SCR-D-002A Embedded Point Is Not Weighted Twice

**ข้อมูลนำเข้า (Input):** คะแนน 10 เกณฑ์รวม 75 และ metadata `weight_percent` รวม 100

**ผลที่คาดหวัง (Expected):** evaluator total = 75; ห้ามคูณคะแนน option ด้วย `weight_percent` ซ้ำ

### SCR-D-003 Mixed Lookup Options

**ผลที่คาดหวัง (Expected):** total เท่ากับผลรวม option จริง ไม่ใช้ display order หรือข้อความคล้ายกันผิดรายการ

### SCR-D-004 Boundary Below/Above

**Inputs:** -0.01, max+0.01, string, NaN, Infinity

**ผลที่คาดหวัง (Expected):** `SCORE_OUT_OF_RANGE`/validation error; DB unchanged

### SCR-D-005 Required Criterion Missing

**ผลที่คาดหวัง (Expected):** Save Draft ได้หรือไม่ได้ตาม draft policy แต่ Submit ต้อง reject; ระบุ criterion ที่ขาด

### SCR-D-006 Criterion Version Binding

**ผลที่คาดหวัง (Expected):** EvaluationScore ทุก row อ้าง criterion/version ที่ active ตอนสร้าง evaluation; criteria version ใหม่ไม่เปลี่ยนคะแนนย้อนหลัง

### SCR-D-007 Recalculate Evaluator Total Server-side

**ข้อมูลนำเข้า (Input):** client ส่ง total ที่ดัดแปลง

**ผลที่คาดหวัง (Expected):** backend ไม่เชื่อ client total; คำนวณจาก score rows เท่านั้น

## 3. Aggregation Tests

### SCR-D-008 One Submitted Only

**ผลที่คาดหวัง (Expected):** submitted count=1, state=`IN_PROGRESS`, ไม่มี Result Summary ที่ถือเป็น complete/final

### SCR-D-009 One Submitted + One Draft

**ผลที่คาดหวัง (Expected):** aggregate ใช้ 1 Submitted เท่านั้นและยังไม่สร้าง complete summary

### SCR-D-010 Two Submitted

**ข้อมูลนำเข้า (Input):** evaluator totals 80 และ 90

**ผลที่คาดหวัง (Expected):** submitted count=2; `MINIMUM_COMPLETE`; summary ตรงสูตรอนุมัติ; หาก average = 85.00

### SCR-D-011 Two Submitted + One Draft

**ผลที่คาดหวัง (Expected):** summary ยังเท่ากับผล 2 Submitted; Draft ของคนที่ 3 ไม่เปลี่ยน score/state

### SCR-D-012 Third Submitted

**ข้อมูลนำเข้า (Input):** third total=70

**ผลที่คาดหวัง (Expected):** submitted count=3; `FULLY_COMPLETE`; recompute จาก 3 คน; หาก average = 80.00

### SCR-D-013 Duplicate Evaluator Corrupt Fixture

**Purpose:** defense-in-depth test ด้วยการพยายาม insert duplicate ผ่าน DB/API

**ผลที่คาดหวัง (Expected):** constraint ปฏิเสธ; aggregate distinct evaluator IDs และแจ้ง data integrity error หากพบ legacy corruption

### SCR-D-014 Cancelled Submitted/Reopened History

**ผลที่คาดหวัง (Expected):** ใช้เฉพาะ current active Submitted ตาม policy; historical/cancelled version ไม่ถูกนับซ้ำ

### SCR-D-015 One Result Summary Only

**ขั้นตอน (Steps):** trigger recalculation หลายครั้ง/พร้อมกัน

**ผลที่คาดหวัง (Expected):** unique applicant_round key; update version/timestamp; no duplicate summary

### SCR-D-016 Rounding

**Dataset:** Decimal totals `80.00`, `80.01` ให้ average `80.005`

**ผลที่คาดหวัง (Expected):** ปัดเฉพาะ Applicant Summary เป็น `80.01` แบบ `HALF_UP`; DB/UI/Export เท่ากัน และห้ามใช้ binary floating point

## 4. State Transition Tests

| ID | Active/Draft | Submitted | Round | Expected |
|---|---:|---:|---|---|
| STA-D-001 | 0 | 0 | Open | `NOT_STARTED` |
| STA-D-002 | 1 Draft | 0 | Open | `IN_PROGRESS` |
| STA-D-003 | 0 | 1 | Open | `IN_PROGRESS` |
| STA-D-004 | 2 Draft | 1 | Open | `IN_PROGRESS` |
| STA-D-005 | any | 2 | Open | `MINIMUM_COMPLETE` |
| STA-D-006 | any | 3 | Open | `FULLY_COMPLETE` |
| STA-D-007 | any | ≥2 | Closed | Finalized |
| STA-D-008 | any | <2 | Closed | `CLOSED_INCOMPLETE` |
| STA-D-009 | 1 Cancelled only | 0 | Open | `NOT_STARTED` |
| STA-D-010 | 2 Submitted + 1 Cancelled | 2 | Open | `MINIMUM_COMPLETE` |

### Transition Guards

- Draft → Submitted: owner, active account, round Open, validation complete
- Submitted → Reopened: authorized policy only
- Closed round: no new selection/submit
- Archived round: read-only

## 5. Dashboard Tests

### DSH-D-001 Count by Submitted 0/1/2/3

**ผลที่คาดหวัง (Expected):** group counts sum to total applicants in selected round

### DSH-D-002 Count by State

**ผลที่คาดหวัง (Expected):** state counts sum to total; no applicant in multiple state buckets

### DSH-D-003 Score Visualization

**ผลที่คาดหวัง (Expected):** only Submitted-based summary; `NOT_STARTED`/`IN_PROGRESS` without complete summary excludedหรือแสดง no score ตาม design

### DSH-D-004 Third Submit Refresh

**ผลที่คาดหวัง (Expected):** `MINIMUM_COMPLETE` count -1, `FULLY_COMPLETE` +1; score chart updates; no stale cache beyond SLA

### DSH-D-005 Close Round Refresh

**ผลที่คาดหวัง (Expected):** open states map to Finalized/`CLOSED_INCOMPLETE`; counts reconcile

## 6. Report/Export Tests

### REP-D-001 Excel Column and Order

ตรวจ provisional RD-021 template: applicant identity, evaluator names, criterion scores, evaluator totals, comments, evaluator count, submitted count, state, summary score และ round metadata

### REP-D-002 CSV Encoding and Escaping

**ผลที่คาดหวัง (Expected):** UTF-8, Thai readable, commas/newlines/quotes in comments escaped correctly

### REP-D-003 DB Reconciliation

For each row compare:

- applicant/round key
- distinct submitted evaluator IDs
- criterion scores and evaluator totals
- submitted count
- applicant state
- summary score/version

**ผลที่คาดหวัง (Expected):** exact match; no hidden spreadsheet formula dependency required to obtain correct values

### REP-D-004 Draft and Cancelled Exclusion

**ผลที่คาดหวัง (Expected):** อาจแสดงสถานะ Draft ราย evaluator ได้หาก template ต้องการ แต่ห้ามนำคะแนนเข้าสรุป; cancelled ไม่ถูกนับ active/submitted

### REP-D-005 Third Submit

**ผลที่คาดหวัง (Expected):** export หลัง third submit แสดง 3 evaluators, `FULLY_COMPLETE` และ summary ใหม่

### REP-D-006 Finalized

**ผลที่คาดหวัง (Expected):** Closed + ≥2 แสดง Finalized และ final summary

### REP-D-007 `CLOSED_INCOMPLETE`

**ผลที่คาดหวัง (Expected):** state=`CLOSED_INCOMPLETE`; final score blank/null; submitted count จริง

### REP-D-008 Role Restriction

**ผลที่คาดหวัง (Expected):** evaluator direct export endpoint = 403; Admin export success

### REP-D-009 Export Audit

**ผลที่คาดหวัง (Expected):** event มี actor, round, format, timestamp, filter, row count และ status; ไม่เก็บ file content/token

### REP-D-010 Concurrent Data Change During Export

**Decision:** report ต้องใช้ snapshot/transaction หรือระบุ as-of time

**ผลที่คาดหวัง (Expected):** file ภายในชุดเดียวกัน consistent ไม่ครึ่งเก่า/ครึ่งใหม่

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.5 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.4 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.3 | 2026-07-24 | SEMS QA Team | Clarified that report-template expectations remain provisional under RD-021. |
| v0.2 | 2026-07-23 | SEMS QA Team | Corrected minimum total to 5 and added embedded-point and Decimal HALF_UP regression cases. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial scoring, state, dashboard and report test draft. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS Import Test Cases](./SEMS_Import_Test_Cases.md)<br>
↑ หมวดเอกสาร: [🧪 Testing](../README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [SEMS Security, RBAC and SSO Test Cases](./SEMS_Security_RBAC_SSO_Test_Cases.md)

<!-- DOC_NAV_END -->
