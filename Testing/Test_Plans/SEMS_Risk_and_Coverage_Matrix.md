# SEMS Risk and Coverage Matrix

| Metadata | Value |
| :--- | :--- |
| Version | **v0.1** |
| Last Updated | **2026-07-23** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

## 1. Scoring Model

- Likelihood: 1–5
- Impact: 1–5
- Risk Score = Likelihood × Impact
- 15–25 = Critical, 8–14 = High, 4–7 = Medium, 1–3 = Low

## 2. Risk Register

| Risk ID | ความเสี่ยง | L | I | Score | ระดับ | Control/Test Coverage |
|---|---|---:|---:|---:|---|---|
| R-01 | ผู้ประเมินคนเดิมสร้าง Evaluation ซ้ำ | 4 | 5 | 20 | Critical | DB unique constraint + SEL-001/002 + concurrent duplicate request |
| R-02 | คำขอพร้อมกันทำให้ผู้ประเมินเกิน 3 คน | 4 | 5 | 20 | Critical | transaction/lock + SEL-003/004 + stress concurrency |
| R-03 | Draft ถูกนำไปคำนวณคะแนน/รายงาน | 4 | 5 | 20 | Critical | SCR-002, REP-003, DSH-003 |
| R-04 | คนที่ 3 Submit แต่ Summary ไม่คำนวณใหม่ | 4 | 5 | 20 | Critical | SCR-004/005, REP-004, state transition |
| R-05 | ปิดรอบแล้วสถานะ/คะแนนสุดท้ายผิด | 3 | 5 | 15 | Critical | RND-006/007, STA-005/006 |
| R-06 | ผู้ประเมินเปิดข้อมูลหรือเอกสารนอกสิทธิ์ | 4 | 5 | 20 | Critical | SEC-007–011, API ownership test, IDOR test |
| R-07 | Import หลายแถวผูก กยศ./ทุนผิดคน | 4 | 5 | 20 | Critical | IMP-010–014 + reconciliation |
| R-08 | Import ข้อมูลผิดรูปแบบแต่ผ่านเข้าฐานข้อมูล | 4 | 4 | 16 | Critical | IMP-004–009, transaction tests |
| R-09 | Report/CSV/Excel ไม่ตรงฐานข้อมูล | 3 | 5 | 15 | Critical | REP-001–008 + DB reconciliation |
| R-10 | คะแนนเกินขอบเขตหรือสูตรผิด | 3 | 5 | 15 | Critical | CRT-004–008, SCR-001–010 |
| R-11 | SSO callback ถูกปลอม state/nonce หรือบัญชี inactive เข้าได้ | 3 | 5 | 15 | Critical | AUTH-003–008 |
| R-12 | Criteria เปลี่ยนหลังเริ่มประเมินทำให้คะแนนย้อนหลังเปลี่ยน | 3 | 5 | 15 | Critical | CRT-009–012, version binding |
| R-13 | Cancelled Evaluation ยังถูกนับ หรือไม่คืน slot | 3 | 4 | 12 | High | SEL-007/008, SCR-003 |
| R-14 | Submit ซ้ำสร้างข้อมูลหรือ audit ซ้ำผิดปกติ | 3 | 4 | 12 | High | EVA-007/008, idempotency |
| R-15 | Dashboard count ไม่ตรง state จริง | 3 | 4 | 12 | High | DSH-001–005 |
| R-16 | File upload ชนิด/ขนาดผิดหรือ path traversal | 3 | 5 | 15 | Critical | DOC-002–006, SEC-012 |
| R-17 | Audit Log มี token/secret/PII เกินจำเป็น | 2 | 5 | 10 | High | AUD-005, SEC-013 |
| R-18 | Migration/seed ทำให้ constraint หาย | 2 | 5 | 10 | High | schema verification + deployment smoke |

## 3. Requirement-to-Test Coverage

| Capability | Unit | DB | API | E2E | Security | Main Case IDs |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Login/Session | ✓ |  | ✓ | ✓ | ✓ | AUTH-001–012 |
| RBAC/Ownership | ✓ |  | ✓ | ✓ | ✓ | RBAC-001–008, SEC-007–011 |
| Round State | ✓ | ✓ | ✓ | ✓ |  | RND-001–008, STA-005–006 |
| Import/Mapping | ✓ | ✓ | ✓ | ✓ | ✓ | IMP-001–018 |
| Document | ✓ |  | ✓ | ✓ | ✓ | DOC-001–007, SEC-012 |
| Criteria/Version | ✓ | ✓ | ✓ | ✓ |  | CRT-001–012 |
| Evaluator Selection | ✓ | ✓ | ✓ | ✓ | ✓ | SEL-001–010 |
| Draft/Review/Submit | ✓ | ✓ | ✓ | ✓ | ✓ | EVA-001–012 |
| Scoring/Aggregation | ✓ | ✓ | ✓ | ✓ |  | SCR-001–012 |
| Applicant State | ✓ | ✓ | ✓ | ✓ |  | STA-001–008 |
| Dashboard | ✓ | ✓ | ✓ | ✓ |  | DSH-001–005 |
| Report/Export | ✓ | ✓ | ✓ | ✓ | ✓ | REP-001–010 |
| Audit | ✓ | ✓ | ✓ | ✓ | ✓ | AUD-001–006 |

## 4. P0 Release Gate

Release ห้ามผ่านหากกรณีต่อไปนี้ไม่ผ่าน:

- SEL-001, SEL-003, SEL-004
- EVA-004, EVA-006, EVA-007
- SCR-002, SCR-004, SCR-005
- STA-003, STA-004, STA-005, STA-006
- IMP-004, IMP-007, IMP-010, IMP-013
- SEC-007, SEC-008, SEC-010
- REP-001, REP-003, REP-004
- AUTH-003, AUTH-004, AUTH-006
