# SEMS Functional Test Case Catalog

| Metadata | Value |
| :--- | :--- |
| Version | **v0.6** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

[START HERE](../../START_HERE.md) › [🧪 Testing](../README.md) › SEMS Functional Test Case Catalog

ตารางนี้เป็น Master Catalog สำหรับ traceability และ regression รายละเอียดกรณีเสี่ยงสูงอยู่ในไฟล์เฉพาะด้าน

## Authentication and User Management

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| AUTH-001 | Admin login ผ่าน KKU SSO และบัญชี SEMS Active | P1 | API/E2E | session ถูกสร้างและ role=Admin | FR-AUT-001..010 | — |
| AUTH-002 | Evaluator login ผ่าน KKU SSO และ Active | P1 | API/E2E | เข้า evaluator landing page | FR-AUT-001..010 | — |
| AUTH-003 | KKU login สำเร็จแต่บัญชี SEMS Inactive | P0 | API/E2E | 403 `USER_INACTIVE`, ไม่มี session ใช้งาน | FR-AUT-001..010 | — |
| AUTH-004 | KKU identity ไม่มีบัญชี/role SEMS | P0 | API/E2E | ปฏิเสธและไม่ auto-provision โดยไม่มีนโยบาย | FR-AUT-001..010 | — |
| AUTH-005 | callback state ไม่ตรง | P0 | API/Security | ปฏิเสธ ไม่แลก token/สร้าง session | FR-AUT-001..010 | — |
| AUTH-006 | nonce ไม่ตรงหรือ ID token invalid | P0 | API/Security | ปฏิเสธและ audit login failure | FR-AUT-001..010 | — |
| AUTH-007 | code verifier PKCE ผิด | P0 | Integration | login ไม่สำเร็จ | FR-AUT-001..010 | — |
| AUTH-008 | session หมดอายุ | P1 | API/E2E | 401 และ redirect login | FR-AUT-001..010 | — |
| AUTH-009 | logout per-app | P1 | E2E | SEMS session สิ้นสุด | FR-AUT-001..010 | — |
| AUTH-010 | เรียก API โดยไม่มี session | P0 | API | 401 `AUTH_REQUIRED` | FR-AUT-001..010 | — |
| AUTH-011 | Admin deactivate evaluator ที่มี Draft | P1 | API/E2E | login/action ใหม่ถูกปฏิเสธ; Draft เก็บไว้ | FR-AUT-001..010 | — |
| AUTH-012 | เปลี่ยน role มีผลต่อ session เดิม | P1 | Security | สิทธิ์ถูก refresh/revoked ตาม policy | FR-AUT-001..010 | — |

## Scholarship Round

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| RND-001 | Admin สร้างรอบ Draft | P1 | API/E2E | round ถูกสร้างและ audit | FR-RND-001..009 | RD-023 |
| RND-002 | Evaluator พยายามสร้าง/แก้รอบ | P0 | RBAC | 403 | FR-RND-001..009 | RD-023 |
| RND-003 | เปิดรอบเมื่อ criteria ยังไม่สมบูรณ์ | P1 | API | reject พร้อม validation | FR-RND-001..009 | RD-023 |
| RND-004 | Evaluator เลือก applicant ใน Draft round | P0 | API | 409 `ROUND_NOT_OPEN` | FR-RND-001..009 | RD-023 |
| RND-005 | Evaluator เลือก/Submit ใน Closed round | P0 | API | 409 `ROUND_NOT_OPEN` | FR-RND-001..009 | RD-023 |
| RND-006 | ปิดรอบที่ Submitted ≥2 | P0 | Integration | Finalized | FR-RND-001..009 | RD-023 |
| RND-007 | ปิดรอบที่ Submitted <2 | P0 | Integration | `CLOSED_INCOMPLETE`; no final score | FR-RND-001..009 | RD-023 |
| RND-008 | แก้/ลบรอบที่มีผลประเมิน | P1 | API | จำกัดตาม policy และ audit | FR-RND-001..009 | RD-023 |

## Import and Applicant

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| IMP-001 | Upload Excel ที่รองรับ | P1 | E2E | อ่าน sheet/header ได้ | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-002 | Upload CSV UTF-8 | P1 | E2E | preview ถูกต้อง | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-003 | Column mapping 37 คอลัมน์ | P1 | E2E | mapping ถูกเก็บกับ batch | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-004 | Required field missing | P0 | Unit/API | `REQUIRED_FIELD_MISSING` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-005 | GPA ต่ำกว่า 0/สูงกว่า 4 | P0 | Unit/API | `INVALID_GPA` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-006 | วันที่พ.ศ.ภาษาไทย valid | P1 | Unit/API | convert เป็น ค.ศ.ถูกต้อง | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-007 | Invalid date | P0 | Unit/API | `INVALID_DATE` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-008 | student_id ซ้ำในไฟล์ | P0 | API | `DUPLICATE_STUDENT` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-009 | invalid coordinate | P0 | Unit/API | `INVALID_COORDINATE` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-010 | multi-row continuation | P0 | Integration | group child histories ถูกคน | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-011 | orphan continuation | P0 | Unit/API | `ORPHAN_CONTINUATION_ROW` | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-012 | `ชือ` header alias | P1 | Mapping | map เป็น first_name ได้ | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-013 | Confirm import มี blocking errors | P0 | API | rollback/reject ตาม policy | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-014 | Import history | P1 | API/E2E | filename, user, time, counts ถูกต้อง | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-015 | Search applicant by student_id/name | P1 | E2E | match เฉพาะ round | FR-IMP-001..015 | RD-017..020, RD-024..029 |
| IMP-016 | Applicant data isolated by round | P0 | API | ไม่ปะปนข้ามรอบ | FR-IMP-001..015 | RD-017..020, RD-024..029 |

## Documents

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| DOC-001 | Admin upload PDF/JPG/PNG valid | P1 | API/E2E | metadata + storage reference ถูกต้อง | FR-DOC-001..006 | RD-022 |
| DOC-002 | Unsupported extension/MIME | P0 | Security | 415 `DOCUMENT_TYPE_UNSUPPORTED` | FR-DOC-001..006 | RD-022 |
| DOC-003 | File เกินขนาด | P1 | API | 413 `DOCUMENT_TOO_LARGE` | FR-DOC-001..006 | RD-022 |
| DOC-004 | Evaluator ดูเอกสาร applicant ที่เลือก | P1 | API/E2E | สำเร็จผ่าน backend auth | FR-DOC-001..006 | RD-022 |
| DOC-005 | Evaluator ดูเอกสาร applicant ที่ไม่เลือก | P0 | Security | 403/404 | FR-DOC-001..006 | RD-022 |
| DOC-006 | Direct storage URL/path | P0 | Security | เข้าไม่ได้โดยข้าม backend | FR-DOC-001..006 | RD-022 |
| DOC-007 | Delete/replace document audit | P1 | API | history ตรวจสอบได้ | FR-DOC-001..006 | RD-022 |

## Criteria

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| CRT-001 | สร้าง criteria set ให้ round | P1 | API/E2E | version/draft ถูกต้อง | FR-CRI-001..012 | RD-012..014 |
| CRT-002 | Criteria code/order/required fields | P1 | Unit/API | validation ผ่าน | FR-CRI-001..012 | RD-012..014 |
| CRT-003 | คะแนนรวมเต็ม 100 ตาม sample | P0 | Unit | max sum=100 | FR-CRI-001..012 | RD-012..014 |
| CRT-004 | คะแนนต่ำกว่า min | P0 | Unit/API | `SCORE_OUT_OF_RANGE` | FR-CRI-001..012 | RD-012..014 |
| CRT-005 | คะแนนสูงกว่า max | P0 | Unit/API | `SCORE_OUT_OF_RANGE` | FR-CRI-001..012 | RD-012..014 |
| CRT-006 | ค่า `-`/null ใน required criterion ตอน Submit | P0 | API | reject incomplete | FR-CRI-001..012 | RD-012..014 |
| CRT-007 | ค่า option map เป็นคะแนนถูกต้อง | P0 | Unit | lookup exact | FR-CRI-001..012 | RD-012..014 |
| CRT-008 | free score ดุลพินิจ boundary 0/10 | P0 | Unit/API | accept boundaries | FR-CRI-001..012 | RD-012..014 |
| CRT-009 | แก้ criteria หลังเริ่มมี Evaluation | P0 | API | `CRITERIA_LOCKED` | FR-CRI-001..012 | RD-012..014 |
| CRT-010 | สร้าง criteria version ใหม่ | P1 | API | old evaluation ยังอ้าง version เดิม | FR-CRI-001..012 | RD-012..014 |
| CRT-011 | Round ใช้ active criteria เดียว | P0 | DB | constraint | FR-CRI-001..012 | RD-012..014 |
| CRT-012 | EvaluationScore อ้าง criterion version ถูกต้อง | P0 | DB | FK/version binding | FR-CRI-001..012 | RD-012..014 |

## Selection and Evaluation

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| SEL-001 | evaluator เดิมเลือกซ้ำ | P0 | DB/API | `DUPLICATE_EVALUATION` | FR-EVA-001..003 | RD-001..005 |
| SEL-002 | double-click จาก evaluator เดิม | P0 | Concurrency | record เดียว | FR-EVA-001..003 | RD-001..005 |
| SEL-003 | คนที่ 4 เลือก | P0 | DB/API | `EVALUATOR_LIMIT_REACHED` | FR-EVA-001..003 | RD-001..005 |
| SEL-004 | สองคนแย่ง slot ที่ 3 | P0 | Concurrency | สำเร็จ 1, reject 1 | FR-EVA-001..003 | RD-001..005 |
| SEL-005 | inactive evaluator เลือก | P0 | API | `USER_INACTIVE` | FR-EVA-001..003 | RD-001..005 |
| SEL-006 | existing Draft เปิดกลับมา | P1 | E2E | edit record เดิม | FR-EVA-001..003 | RD-001..005 |
| SEL-007 | cancel Draft ที่อนุญาต | P1 | API | record inactive + audit | FR-EVA-001..003 | RD-001..005 |
| SEL-008 | cancelled record คืน slot | P0 | DB/API | evaluator ใหม่เลือกได้ | FR-EVA-001..003 | RD-001..005 |
| SEL-009 | evaluator ประเมินหลาย applicant | P1 | API/E2E | allowed | FR-EVA-001..003 | RD-001..005 |
| SEL-010 | applicant ครบ 2 Submitted ยังรับคนที่ 3 | P0 | API | allowed เมื่อ Open/slot<3 | FR-EVA-001..003 | RD-001..005 |
| EVA-001 | Save partial Draft | P1 | API/E2E | save ได้ตาม draft validation | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-002 | แก้ Draft ของตนเอง | P1 | API/E2E | สำเร็จ | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-003 | แก้ Draft ของผู้อื่น | P0 | RBAC | 403 | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-004 | Draft ไม่เข้า aggregate | P0 | Unit/Integration | excluded | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-005 | Review แสดงคะแนน/ความคิดเห็นครบ | P1 | E2E | data ตรง Draft ล่าสุด | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-006 | Submit valid evaluation | P0 | API/E2E | status=`SUBMITTED`, immutable | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-007 | Submit ซ้ำ | P0 | API | deterministic reject/idempotent | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-008 | แก้ Submitted โดยไม่ Reopen | P0 | API | reject | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-009 | Reopen โดยผู้ไม่มีสิทธิ์ | P0 | RBAC | 403 | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-010 | Reopen ตาม policy | P1 | API | state/audit ถูกต้อง | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-011 | Submit ขณะ round ปิดระหว่างหน้า Review | P0 | Concurrency | reject; no partial submit | FR-EVA-004..018 | RD-004, RD-008..011 |
| EVA-012 | Browser refresh/back หลัง Submit | P1 | E2E | ไม่ส่งซ้ำ/ไม่กลับ Draft | FR-EVA-004..018 | RD-004, RD-008..011 |

## Scoring, State, Dashboard and Report

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| SCR-001 | evaluator total min/max | P0 | Unit | 5 และ 100 ถูกต้อง; embedded point ไม่ถูกคูณ weight ซ้ำ | FR-SCO-001..012 | RD-004..014 |
| SCR-002 | Draft excluded | P0 | Unit/Integration | ไม่ใช้ | FR-SCO-001..012 | RD-004..014 |
| SCR-003 | Cancelled excluded | P0 | Unit/Integration | ไม่ใช้ | FR-SCO-001..012 | RD-004..014 |
| SCR-004 | 2 Submitted create summary | P0 | Integration | `MINIMUM_COMPLETE` | FR-SCO-001..012 | RD-004..014 |
| SCR-005 | 3rd Submitted recalculates | P0 | Integration | `FULLY_COMPLETE` + new score | FR-SCO-001..012 | RD-004..014 |
| SCR-006 | ผู้ประเมินไม่ซ้ำกันเท่านั้น | P0 | DB/Unit | duplicate ไม่เพิ่ม count | FR-SCO-001..012 | RD-004..014 |
| SCR-007 | one ResultSummary/applicant/round | P0 | DB | unique constraint | FR-SCO-001..012 | RD-004..014 |
| SCR-008 | rounding boundary | P0 | Unit | ตรง provisional RD-011 rule | FR-SCO-001..012 | RD-004..014 |
| SCR-009 | criteria version binding | P0 | Unit/DB | score from correct version | FR-SCO-001..012 | RD-004..014 |
| SCR-010 | concurrent submissions update summary | P0 | Concurrency | no lost update | FR-SCO-001..012 | RD-004..014 |
| STA-001 | 0 active = `NOT_STARTED` | P1 | Unit | state correct | FR-SCO-008..012 | RD-006..007 |
| STA-002 | active + Submitted<2 = `IN_PROGRESS` | P1 | Unit | state correct | FR-SCO-008..012 | RD-006..007 |
| STA-003 | 2 Submitted/Open = `MINIMUM_COMPLETE` | P0 | Unit | state correct | FR-SCO-008..012 | RD-006..007 |
| STA-004 | 3 Submitted/Open = `FULLY_COMPLETE` | P0 | Unit | state correct | FR-SCO-008..012 | RD-006..007 |
| STA-005 | Closed + Submitted≥2 = Finalized | P0 | Unit/Integration | final score | FR-SCO-008..012 | RD-006..007 |
| STA-006 | Closed + Submitted<2 = `CLOSED_INCOMPLETE` | P0 | Unit/Integration | no final score | FR-SCO-008..012 | RD-006..007 |
| DSH-001 | counts by Submitted 0/1/2/3 | P1 | Integration | DB-reconciled | FR-DSH-001..003 | RD-004..007 |
| DSH-002 | counts by applicant state | P1 | Integration | DB-reconciled | FR-DSH-001..003 | RD-004..007 |
| DSH-003 | score chart excludes Draft | P0 | Integration | Submitted only | FR-DSH-001..003 | RD-004..007 |
| DSH-004 | third submit refreshes counts/chart | P0 | Integration/E2E | current data | FR-DSH-001..003 | RD-004..007 |
| DSH-005 | filter by round | P1 | E2E | no cross-round data | FR-DSH-001..003 | RD-004..007 |
| REP-001 | Excel matches DB | P0 | Reconciliation | exact values | FR-RPT-001..009 | RD-021..022 |
| REP-002 | CSV matches DB | P0 | Reconciliation | exact values | FR-RPT-001..009 | RD-021..022 |
| REP-003 | Draft/Cancelled excluded | P0 | Reconciliation | excluded | FR-RPT-001..009 | RD-021..022 |
| REP-004 | third submit reflected | P0 | Reconciliation | updated summary | FR-RPT-001..009 | RD-021..022 |
| REP-005 | state and submitted count displayed | P1 | E2E | correct | FR-RPT-001..009 | RD-021..022 |
| REP-006 | `CLOSED_INCOMPLETE` has no final score | P0 | Reconciliation | blank/null | FR-RPT-001..009 | RD-021..022 |
| REP-007 | export role restriction | P0 | RBAC | evaluator denied | FR-RPT-001..009 | RD-021..022 |
| REP-008 | export audit event | P1 | API | user/time/round/format | FR-RPT-001..009 | RD-021..022 |
| REP-009 | empty round export | P2 | E2E | valid headers/no error | FR-RPT-001..009 | RD-021..022 |
| REP-010 | Thai text/encoding | P1 | File | Excel/CSV readable | FR-RPT-001..009 | RD-021..022 |

## Audit and Non-functional

| ID | Scenario | P | Level | Expected Result | Linked Requirement | Linked Decision |
|---|---|:---:|---|---|---|---|
| AUD-001 | Login success/failure | P1 | Integration | event with actor/time/result | FR-AUD-001..004 | RD-008, RD-021..022 |
| AUD-002 | Selection success/reject | P1 | Integration | event detail sufficient | FR-AUD-001..004 | RD-008, RD-021..022 |
| AUD-003 | Draft/Submit/Reopen/Cancel | P1 | Integration | old/new status | FR-AUD-001..004 | RD-008, RD-021..022 |
| AUD-004 | Import/Export | P1 | Integration | batch/round/file metadata | FR-AUD-001..004 | RD-008, RD-021..022 |
| AUD-005 | Token/password/secret not logged | P0 | Security | redacted/absent | FR-AUD-001..004 | RD-008, RD-021..022 |
| AUD-006 | Audit access restricted | P0 | RBAC | evaluator denied | FR-AUD-001..004 | RD-008, RD-021..022 |
| NFR-001 | Import target volume | P1 | Performance | within agreed SLA/no timeout | Section 4 NFR | — |
| NFR-002 | 20 concurrent evaluator sessions | P1 | Performance | no data violation | Section 4 NFR | — |
| NFR-003 | Export target volume | P1 | Performance | complete file within SLA | Section 4 NFR | — |
| NFR-004 | retry after transient DB error | P1 | Resilience | no duplicate record | Section 4 NFR | — |
| NFR-005 | backup/restore preserves constraints | P1 | Recovery | data/summary/audit intact | Section 4 NFR | — |

## Related Documents

- เอกสารที่เกี่ยวข้อง: [SEMS UAT Baseline Checklist](../UAT/SEMS_UAT_Baseline_Checklist.md)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.6 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v0.5 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.4 | 2026-07-24 | SEMS QA Team | Added explicit navigation from functional test specifications to the pending UAT checklist. |
| v0.3 | 2026-07-24 | SEMS QA Team | Aligned inactive-user and applicant-document errors with the canonical inventory and retained provisional scoring status. |
| v0.2 | 2026-07-23 | SEMS QA Team | Added Linked Requirement/Linked Decision columns, canonical duplicate code and corrected scoring range to 5–100. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial functional test catalog draft. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS Test Data and Environment Plan](../Test_Plans/SEMS_Test_Data_and_Environment_Plan.md)<br>
↑ หมวดเอกสาร: [🧪 Testing](../README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [SEMS High Risk Test Cases](./SEMS_High_Risk_Test_Cases.md)

<!-- DOC_NAV_END -->
