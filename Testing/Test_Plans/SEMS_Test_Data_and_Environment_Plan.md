# SEMS Test Data and Environment Plan

| Metadata | Value |
| :--- | :--- |
| Version | **v0.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

## 1. หลักการ

- ใช้ข้อมูลจำลองหรือ anonymized data เท่านั้น
- Test Data ต้องสร้างซ้ำได้ด้วย seed/script
- ห้ามเก็บ password, client secret, access token หรือเอกสารจริงใน repository
- ทุก Test Run ต้องระบุ dataset version
- ข้อมูล DB, Result Summary, Dashboard และ Export ต้องมี key ที่ reconciliation ได้ เช่น `round_id`, `student_id`, `evaluation_id`

## 2. User Dataset

| Data ID | Role | Status | วัตถุประสงค์ |
|---|---|---|---|
| U-ADM-01 | Admin | Active | จัดการรอบ Import Criteria Report |
| U-ADM-02 | Admin | Active | ทดสอบ audit และงานคู่ขนาน |
| U-EVA-01 | Evaluator | Active | ผู้ประเมินคนที่ 1 |
| U-EVA-02 | Evaluator | Active | ผู้ประเมินคนที่ 2 |
| U-EVA-03 | Evaluator | Active | ผู้ประเมินคนที่ 3 |
| U-EVA-04 | Evaluator | Active | ผู้ประเมินคนที่ 4/คำขอแข่งขัน |
| U-EVA-05 | Evaluator | Inactive | ทดสอบ USER_INACTIVE |
| U-NONE-01 | No SEMS role | N/A | KKU ยืนยันตัวตนได้แต่ไม่มีสิทธิ์ SEMS |

## 3. Scholarship Round Dataset

| Data ID | Status | Criteria | Applicant | ใช้ทดสอบ |
|---|---|---|---:|---|
| R-DRAFT-01 | Draft | Draft criteria | 0 | แก้ไขก่อนเปิด/ห้าม evaluator เลือก |
| R-OPEN-01 | Open | Active v1 | ≥12 | Core Flow |
| R-CLOSED-01 | Closed | Active v1 | ≥4 | close state, access restriction |
| R-ARCH-01 | Archived | Historical | ≥2 | read-only/history |

## 4. Applicant/Evaluation State Dataset

| Data ID | Active Evaluations | Submitted | Expected State เมื่อ Open | Expected State เมื่อ Closed |
|---|---:|---:|---|---|
| A-00 | 0 | 0 | `NOT_STARTED` | `CLOSED_INCOMPLETE` |
| A-D1 | 1 Draft | 0 | `IN_PROGRESS` | `CLOSED_INCOMPLETE` |
| A-S1 | 1 Submitted | 1 | `IN_PROGRESS` | `CLOSED_INCOMPLETE` |
| A-S2 | 2 Submitted | 2 | `MINIMUM_COMPLETE` | Finalized |
| A-D2S1 | 2 Draft + 1 Submitted | 1 | `IN_PROGRESS` | `CLOSED_INCOMPLETE` |
| A-S2D1 | 2 Submitted + 1 Draft | 2 | `MINIMUM_COMPLETE` | Finalized; Draft ห้ามกลายเป็น final |
| A-S3 | 3 Submitted | 3 | `FULLY_COMPLETE` | Finalized |
| A-CANCEL | 2 Submitted + 1 Cancelled | 2 | `MINIMUM_COMPLETE`; มี slot ว่าง | Finalized |

## 5. Scoring Dataset

Criteria sample มีหัวข้อคะแนนเต็มรวม 100:

| Criterion | Max |
|---|---:|
| ค่าเทอม | 10 |
| ค่าใช้จ่ายประจำวัน: แหล่งส่งเสีย | 10 |
| ทำงานพิเศษ | 10 |
| การนำทุนไปใช้ประโยชน์ | 20 |
| ค่าใช้จ่ายประจำวัน: จำนวนเงิน | 10 |
| ค่าที่พัก | 10 |
| การเดินทางมาเรียน | 5 |
| ผลการเรียน | 5 |
| ดุลพินิจอาจารย์ | 10 |
| ส่วนร่วมกับคณะ/มหาวิทยาลัย | 10 |
| **รวม** | **100** |

### Reference Vectors

| Vector | คะแนนรวม | ใช้ทดสอบ |
|---|---:|---|
| S-MIN | 0 | min boundary |
| S-MID | 50 | normal |
| S-HIGH | 80 | evaluator 1 |
| S-HIGH2 | 90 | evaluator 2 |
| S-THIRD | 70 | evaluator 3/recalculation |
| S-MAX | 100 | max boundary |

> เมื่อสูตร aggregate ได้รับอนุมัติ ให้บันทึก expected summary แบบ exact value ตัวอย่าง หากใช้ค่าเฉลี่ย: 80 และ 90 → 85.00; เพิ่ม 70 → 80.00

## 6. Import Dataset

| File ID | เนื้อหา | Expected |
|---|---|---|
| I-VALID-01 | Excel 37 คอลัมน์ ข้อมูล base row เดียว | Import success |
| I-VALID-02 | CSV encoding UTF-8 | Import success |
| I-MULTI-01 | base row + 3 continuation rows ใน กยศ./ทุน | 1 applicant + child histories ครบ |
| I-HEADER-01 | หัวคอลัมน์ `ชือ` | mapping alias ไป `first_name` หรือให้ผู้ใช้ map ได้ |
| I-DATE-01 | `09 ก.ค. 2569 13:36` | แปลงเป็น ค.ศ. และเวลาเดียวกัน |
| I-GPA-LOW | GPA -0.01 | INVALID_GPA |
| I-GPA-HIGH | GPA 4.01 | INVALID_GPA |
| I-COORD-01 | `16.37929729279832, 104.38542017283481` | valid lat/lng |
| I-COORD-02 | `95, 181` | INVALID_COORDINATE |
| I-DUP-01 | student_id ซ้ำในไฟล์ | DUPLICATE_STUDENT |
| I-DUP-02 | student_id มีอยู่ในรอบแล้ว | reject/update ตาม policy |
| I-ORPHAN-01 | แถวแรกมีเฉพาะ กยศ./ทุน | ORPHAN_CONTINUATION_ROW |
| I-PHONE-01 | `0810000001` | เก็บ leading zero เป็น string |
| I-PHONE-02 | `8.10000001E8` | reject/normalize ตาม mapping policy |
| I-LOAN-01 | `-2565 : 66,000` | year=2565, amount=66000 |
| I-SCH-01 | `-2567 ทุน ข : 10,000` | year=2567, name=ทุน ข, amount=10000 |

## 7. Document Dataset

| File ID | Type | Expected |
|---|---|---|
| F-PDF-01 | valid PDF | upload/view |
| F-JPG-01 | valid JPG | upload/view |
| F-PNG-01 | valid PNG | upload/view |
| F-EXE-01 | executable renamed `.pdf` | reject MIME mismatch |
| F-BIG-01 | file > configured max | DOCUMENT_TOO_LARGE |
| F-PATH-01 | filename `../../secret.pdf` | sanitized/reject; no traversal |
| F-CORRUPT-01 | corrupt PDF | reject or store with clear unsupported-preview state per policy |

## 8. Concurrency Harness

- ใช้ barrier ให้ request เริ่มพร้อมกันจริง
- Scenario A: Applicant มี 2 active evaluations; U-EVA-03 และ U-EVA-04 เลือกพร้อมกัน
- Scenario B: U-EVA-01 double-click/ส่ง 2 request พร้อมกัน
- Scenario C: evaluator 2 และ 3 Submit ใกล้พร้อมกัน แล้วตรวจ Result Summary version/updated_at
- ตรวจทั้ง API response, DB row count, unique constraints, audit และ dashboard eventual consistency

## 9. Environment Checklist

- [ ] Database migration ล่าสุด
- [ ] Seed version ตรงกับ test run
- [ ] Test File Storage ว่างหรือ namespace แยก
- [ ] SSO test client redirect URI ถูกต้อง
- [ ] System clock/timezone กำหนดชัดเจน (`Asia/Bangkok` แนะนำสำหรับ UI)
- [ ] Background job/queue เปิดเหมือน Production หากมี
- [ ] Export library/font/locale ตรง Production
- [ ] Log redaction เปิดใช้งาน
- [ ] Backup ก่อน destructive test
- [ ] Reset script ผ่านหลัง test run

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.2 | 2026-07-24 | SEMS QA Team | Aligned inactive-user and applicant-document size fixtures with canonical error codes. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial test data and environment plan draft. |
