# SEMS Process Flow Specification

| รายการ | รายละเอียด |
|---|---|
| ชื่อระบบ | Scholarship Evaluation Management System (SEMS) |
| รหัสเอกสาร | SEMS-DES-FLOW-001 |
| Version | **v1.2** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Design Team** |
| Status | **Draft for Review** |
| ตำแหน่งไฟล์ | `Design/Architecture/SEMS_Process_Flows.md` |

## 1. วัตถุประสงค์

เอกสารนี้กำหนด Process Flow ของกระบวนการหลักในระบบ SEMS เพื่อใช้เป็นข้อมูลอ้างอิงสำหรับออกแบบหน้าจอ ออกแบบ API กำหนด Business Logic จัดทำ Test Case และตรวจสอบความครบถ้วนของ Requirement

## 2. ขอบเขตและกฎร่วม

1. ระบบยืนยันตัวตนผ่าน KKU SSO โดย SEMS ไม่รับหรือจัดเก็บรหัสผ่าน KKU Account
2. SEMS เป็นผู้ตรวจสอบบัญชีภายใน สถานะ Active บทบาท และสิทธิ์การเข้าถึง
3. ผู้สมัครหนึ่งคนมี Evaluation ที่ยังไม่ถูกยกเลิกได้สูงสุด 3 รายการต่อรอบทุน
4. ผู้ประเมินคนเดิมมี Evaluation ที่ยังไม่ถูกยกเลิกสำหรับผู้สมัครคนเดิมได้ไม่เกิน 1 รายการต่อรอบทุน
5. ใช้เฉพาะ Evaluation สถานะ `Submitted` ในการคำนวณคะแนนสรุป
6. เมื่อมี Submitted ครบ 2 คนในรอบที่ยังเปิด ผู้สมัครมีสถานะ `Minimum Complete`
7. เมื่อมี Submitted ครบ 3 คนในรอบที่ยังเปิด ผู้สมัครมีสถานะ `Fully Complete`
8. เมื่อปิดรอบ ผู้สมัครที่มี Submitted อย่างน้อย 2 คนเป็น `Finalized`
9. เมื่อปิดรอบ ผู้สมัครที่มี Submitted น้อยกว่า 2 คนเป็น `Closed Incomplete` และไม่มีคะแนนสรุปสุดท้าย
10. การแก้ไขผลหลัง Submit ต้องผ่าน Reopen Policy และบันทึก Audit Log
11. การคำนวณคะแนน น้ำหนัก และการปัดเศษให้ยึด Scoring Rule Specification ฉบับที่ได้รับอนุมัติ
12. การทำงานที่กระทบจำนวนผู้ประเมิน คะแนนสรุป หรือสถานะรอบทุนต้องใช้ Database Transaction

## 3. รายการ Process Flow

| Flow ID | Process | ผู้ใช้งานหลัก | ผลลัพธ์สำคัญ |
|---|---|---|---|
| PF-AUTH-001 | Admin Login Flow | Admin | Session สำหรับบทบาท Admin |
| PF-AUTH-002 | Evaluator Login Flow | Evaluator | Session สำหรับบทบาท Evaluator |
| PF-IMP-001 | Import Applicant Flow | Admin | Applicant Import Batch |
| PF-IMP-002 | Import Validation Flow | System/Admin | Validation Result และ Error Report |
| PF-CRI-001 | Criteria Setup Flow | Admin | Criteria Version พร้อมใช้งาน |
| PF-EVA-001 | Evaluator Select Applicant Flow | Evaluator | Evaluation สถานะ Draft |
| PF-EVA-002 | Draft–Review–Submit Flow | Evaluator | Evaluation สถานะ Submitted |
| PF-SCR-001 | Score Calculation Flow | System | Result Summary ล่าสุด |
| PF-SCR-002 | Third Evaluator Recalculation Flow | System | Result Summary จากผู้ประเมิน 3 คน |
| PF-RND-001 | Close Scholarship Round Flow | Admin/System | Finalized หรือ Closed Incomplete |
| PF-RPT-001 | Export Report Flow | Admin | Excel หรือ CSV |
| PF-EVA-003 | Reopen Evaluation Flow | Admin/Evaluator | Evaluation เปิดแก้ไขและคำนวณใหม่ |
| PF-AUTH-003 | SSO Error Flow | System/User | Error Handling และ Audit Event |

---

## 4. PF-AUTH-001: Admin Login Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin เปิดหน้า SEMS"]
    B --> C{"มี SEMS Session<br/>ที่ยังใช้งานได้หรือไม่"}
    C -- ใช่ --> D{"บัญชี Active<br/>และมีบทบาท Admin หรือไม่"}
    C -- ไม่ใช่ --> E["Frontend สร้าง state, nonce,<br/>code_verifier และ code_challenge S256"]
    E --> F["Redirect ไป KKU SSO /authorize"]
    F --> G["ผู้ใช้ยืนยันตัวตนด้วย KKU Account"]
    G --> H["KKU SSO Redirect กลับ Callback พร้อม code"]
    H --> I{"ตรวจสอบ state สำเร็จหรือไม่"}
    I -- ไม่สำเร็จ --> X["ไปยัง SSO Error Flow"]
    I -- สำเร็จ --> J["Backend แลก code ที่ /token<br/>พร้อม code_verifier"]
    J --> K{"ตรวจสอบ ID Token,<br/>signature, issuer, audience,<br/>expiry และ nonce สำเร็จหรือไม่"}
    K -- ไม่สำเร็จ --> X
    K -- สำเร็จ --> L["อ่าน Claims จาก ID Token<br/>หรือเรียก /userinfo"]
    L --> M["ค้นหา SEMS User จากตัวระบุถาวร"]
    M --> N{"พบบัญชีและสถานะ Active หรือไม่"}
    N -- ไม่พบ/Inactive --> O["ปฏิเสธการเข้าใช้<br/>บันทึก Login Failure"]
    N -- ใช่ --> P{"มีบทบาท Admin หรือไม่"}
    P -- ไม่ใช่ --> Q["Login สำเร็จตามบทบาทจริง<br/>แต่ปฏิเสธ Admin Route"]
    P -- ใช่ --> R["สร้าง SEMS Session"]
    R --> S["บันทึก Login Success Audit Event"]
    S --> T["Redirect ไป Admin Dashboard"]
    D -- ใช่ --> T
    D -- ไม่ใช่ --> U["ยกเลิก Session และปฏิเสธการเข้าถึง"]
    O --> V([สิ้นสุด])
    Q --> V
    U --> V
    T --> V
```

### เงื่อนไขสำคัญ

- ต้องตรวจสอบสิทธิ์ซ้ำที่ Backend ทุก Request ไม่อาศัยเฉพาะการซ่อนเมนู
- Audit Log ต้องไม่บันทึก password, access token, refresh token หรือ client secret
- การเข้าหน้า Admin ด้วยบัญชี Evaluator ให้ตอบ `403 Forbidden`

---

## 5. PF-AUTH-002: Evaluator Login Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Evaluator เปิดหน้า SEMS"]
    B --> C{"มี Session ที่ยังใช้งานได้หรือไม่"}
    C -- ใช่ --> D{"บัญชี Active และมีสิทธิ์ Evaluator หรือไม่"}
    C -- ไม่ใช่ --> E["สร้าง state, nonce และ PKCE S256"]
    E --> F["Redirect ไป KKU SSO"]
    F --> G["ผู้ใช้ยืนยันตัวตน"]
    G --> H["รับ Authorization Code ที่ Callback"]
    H --> I{"state ถูกต้องหรือไม่"}
    I -- ไม่ --> X["ไปยัง SSO Error Flow"]
    I -- ใช่ --> J["แลก Code เป็น Token"]
    J --> K{"ID Token และ nonce ถูกต้องหรือไม่"}
    K -- ไม่ --> X
    K -- ใช่ --> L["อ่านข้อมูลผู้ใช้จาก Claims หรือ /userinfo"]
    L --> M{"พบบัญชี SEMS หรือไม่"}
    M -- ไม่ --> N["แสดงข้อความว่ายังไม่ได้รับสิทธิ์<br/>ให้ติดต่อผู้ดูแลระบบ"]
    M -- ใช่ --> O{"บัญชี Active หรือไม่"}
    O -- ไม่ --> P["ปฏิเสธการเข้าใช้และบันทึกเหตุการณ์"]
    O -- ใช่ --> Q{"มีบทบาท Evaluator หรือ Admin<br/>ที่ได้รับสิทธิ์ประเมินหรือไม่"}
    Q -- ไม่ --> R["Access Denied"]
    Q -- ใช่ --> S["สร้าง Session และโหลดรอบทุน Open"]
    S --> T["Redirect ไป Evaluator Dashboard"]
    D -- ใช่ --> T
    D -- ไม่ --> U["ยกเลิก Session และ Access Denied"]
    N --> V([สิ้นสุด])
    P --> V
    R --> V
    U --> V
    T --> V
```

---

## 6. PF-IMP-001: Import Applicant Flow

> ข้อเสนอเชิงออกแบบ: อนุญาตให้นำเข้าข้อมูลในรอบสถานะ `Draft` เป็นหลัก หากต้องนำเข้าในรอบ `Open` ต้องกำหนดสิทธิ์และผลกระทบเพิ่มเติมอย่างชัดเจน

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin เปิดเมนู Import Applicant"]
    B --> C["เลือกรอบทุนเป้าหมาย"]
    C --> D{"รอบทุนอนุญาตให้นำเข้าหรือไม่"}
    D -- ไม่ --> E["ปฏิเสธและแจ้งสถานะรอบที่รองรับ"]
    D -- ใช่ --> F["อัปโหลดไฟล์ CSV หรือ Excel"]
    F --> G{"ชนิดไฟล์และขนาดไฟล์ถูกต้องหรือไม่"}
    G -- ไม่ --> H["แจ้ง UNSUPPORTED_FILE_TYPE<br/>หรือ IMPORT_FILE_TOO_LARGE"]
    G -- ใช่ --> I["สร้าง Import Batch สถานะ Uploaded"]
    I --> J["อ่าน Header และตัวอย่างข้อมูล"]
    J --> K["แสดง Column Mapping"]
    K --> L["Admin ตรวจสอบหรือแก้ Mapping"]
    L --> M{"Mapping ฟิลด์บังคับครบหรือไม่"}
    M -- ไม่ --> N["แจ้ง REQUIRED_COLUMN_NOT_MAPPED"]
    M -- ใช่ --> O["แปลงข้อมูลเป็น Staging Records"]
    O --> P["เรียก Import Validation Flow"]
    P --> Q{"พบ Error หรือไม่"}
    Q -- ใช่ --> R["แสดง Preview พร้อมเลขแถว<br/>Error Code และคำอธิบาย"]
    R --> S{"Admin อัปโหลดไฟล์ใหม่<br/>หรือแก้ Mapping หรือไม่"}
    S -- ใช่ --> J
    S -- ไม่ --> T["ยกเลิก Import Batch"]
    Q -- ไม่ --> U["แสดงสรุปจำนวนรายการที่จะนำเข้า"]
    U --> V{"Admin ยืนยันนำเข้าหรือไม่"}
    V -- ไม่ --> T
    V -- ใช่ --> W["เริ่ม Database Transaction"]
    W --> X["บันทึก Applicant และข้อมูลที่เกี่ยวข้อง"]
    X --> Y{"บันทึกสำเร็จทุก Record หรือไม่"}
    Y -- ไม่ --> Z["Rollback และบันทึก Import Failed"]
    Y -- ใช่ --> AA["Commit Transaction"]
    AA --> AB["บันทึกชื่อไฟล์ ผู้นำเข้า เวลา<br/>จำนวนสำเร็จ และผล Validation"]
    AB --> AC["ตั้ง Import Batch เป็น Completed"]
    AC --> AD([สิ้นสุด])
    E --> AD
    H --> AD
    N --> AD
    T --> AD
    Z --> AD
```

---

## 7. PF-IMP-002: Import Validation Flow

```mermaid
flowchart TD
    A([รับ Staging Records]) --> B["Normalize ชื่อคอลัมน์ ช่องว่าง<br/>รูปแบบตัวเลข และค่าว่าง"]
    B --> C["ระบุ Primary Row และ Continuation Row"]
    C --> D{"Continuation Row<br/>มี Primary Row ที่เชื่อมโยงได้หรือไม่"}
    D -- ไม่ --> E["เพิ่ม ORPHAN_CONTINUATION_ROW"]
    D -- ใช่ --> F["รวมข้อมูลหลายแถวเป็น Applicant เดียว"]
    E --> F
    F --> G["ตรวจฟิลด์บังคับ"]
    G --> H{"ข้อมูลบังคับครบหรือไม่"}
    H -- ไม่ --> I["เพิ่ม REQUIRED_FIELD_MISSING"]
    H -- ใช่ --> J["ตรวจรูปแบบรหัสนักศึกษา GPA วันที่<br/>โทรศัพท์ อีเมล และข้อมูลตัวเลข"]
    I --> J
    J --> K{"รูปแบบถูกต้องหรือไม่"}
    K -- ไม่ --> L["เพิ่ม Error Code ตามฟิลด์<br/>เช่น INVALID_GPA หรือ INVALID_DATE"]
    K -- ใช่ --> M["แปลงวันที่ พ.ศ. เป็น ค.ศ.<br/>และแปลงชนิดข้อมูล"]
    L --> M
    M --> N["ตรวจพิกัด latitude และ longitude"]
    N --> O{"พิกัดอยู่ในช่วงที่กำหนดหรือไม่"}
    O -- ไม่ --> P["เพิ่ม INVALID_COORDINATE"]
    O -- ใช่ --> Q["แยกข้อมูล กยศ. และประวัติทุนหลายปี"]
    P --> Q
    Q --> R["ตรวจข้อมูลซ้ำภายในไฟล์"]
    R --> S{"ซ้ำภายในไฟล์หรือไม่"}
    S -- ใช่ --> T["เพิ่ม DUPLICATE_STUDENT_IN_FILE"]
    S -- ไม่ --> U["ตรวจข้อมูลซ้ำกับรอบทุนในฐานข้อมูล"]
    T --> U
    U --> V{"ซ้ำกับฐานข้อมูลหรือไม่"}
    V -- ใช่ --> W["เพิ่ม DUPLICATE_STUDENT"]
    V -- ไม่ --> X["ตรวจ Referential และ Business Rules"]
    W --> X
    X --> Y["จัดกลุ่มผลเป็น Valid, Warning และ Error"]
    Y --> Z["สร้าง Validation Summary<br/>พร้อมเลขแถวและค่าที่ผิด"]
    Z --> AA{"มี Error ระดับ Blocker หรือไม่"}
    AA -- ใช่ --> AB["ส่งผล Validation Failed"]
    AA -- ไม่ --> AC["ส่งผล Validation Passed"]
    AB --> AD([คืนผลให้ Import Flow])
    AC --> AD
```

### Error Code ขั้นต่ำ

| Error Code | ความหมาย |
|---|---|
| `REQUIRED_FIELD_MISSING` | ข้อมูลบังคับว่าง |
| `REQUIRED_COLUMN_NOT_MAPPED` | ยังไม่ได้จับคู่คอลัมน์บังคับ |
| `INVALID_STUDENT_ID` | รหัสนักศึกษาผิดรูปแบบ |
| `INVALID_GPA` | GPA ไม่ใช่ตัวเลขหรืออยู่นอกช่วง 0.00–4.00 |
| `INVALID_DATE` | วันที่ไม่สามารถแปลงได้ |
| `INVALID_PHONE` | เบอร์โทรศัพท์ผิดรูปแบบ |
| `INVALID_EMAIL` | อีเมลผิดรูปแบบ |
| `INVALID_COORDINATE` | พิกัดผิดรูปแบบหรืออยู่นอกช่วง |
| `DUPLICATE_STUDENT_IN_FILE` | ผู้สมัครซ้ำภายในไฟล์ |
| `DUPLICATE_STUDENT` | ผู้สมัครซ้ำในรอบทุน |
| `ORPHAN_CONTINUATION_ROW` | แถวต่อเนื่องไม่มีแถวหลัก |
| `UNSUPPORTED_FILE_TYPE` | ชนิดไฟล์ Import ไม่รองรับ |
| `IMPORT_FILE_TOO_LARGE` | ขนาดไฟล์ Import เกินกำหนด |

---

## 8. PF-CRI-001: Criteria Setup Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin เลือกรอบทุน"]
    B --> C{"รอบทุนอยู่ในสถานะ Draft หรือไม่"}
    C -- ไม่ --> D["ตรวจ Criteria Change Policy"]
    D --> E{"มีสิทธิ์สร้าง Version ใหม่หรือไม่"}
    E -- ไม่ --> F["ปฏิเสธการแก้ไขเกณฑ์"]
    E -- ใช่ --> G["Clone Criteria เป็น Version ใหม่"]
    C -- ใช่ --> H["สร้าง Criteria Set ใหม่<br/>หรือแก้ไข Draft Version"]
    G --> I["กำหนดรหัส ชื่อ คำอธิบาย<br/>คะแนนต่ำสุด คะแนนเต็ม น้ำหนัก<br/>ลำดับ และ Required"]
    H --> I
    I --> J["ตรวจค่ารายเกณฑ์"]
    J --> K{"min <= max, น้ำหนักถูกต้อง<br/>รหัสไม่ซ้ำ และลำดับครบหรือไม่"}
    K -- ไม่ --> L["แสดง Validation Error"]
    L --> I
    K -- ใช่ --> M["ตรวจผลรวมคะแนนและน้ำหนัก"]
    M --> N{"เป็นไปตาม Scoring Rule หรือไม่"}
    N -- ไม่ --> O["แจ้ง SCORE_TOTAL_INVALID<br/>หรือ WEIGHT_TOTAL_INVALID"]
    O --> I
    N -- ใช่ --> P{"มี Evaluation ที่เริ่มใช้งาน<br/>Criteria Version นี้แล้วหรือไม่"}
    P -- ใช่ --> Q["Lock Version เดิม<br/>ห้ามแก้ไขแบบ In-place"]
    Q --> R{"Version ใหม่ได้รับอนุมัติ<br/>ให้ใช้กับรายการใหม่หรือไม่"}
    R -- ไม่ --> S["เก็บเป็น Draft Version"]
    R -- ใช่ --> T["กำหนด Effective Policy<br/>และบันทึกผู้อนุมัติ"]
    P -- ไม่ --> U["Activate Criteria Version"]
    T --> U
    U --> V["บันทึก Audit Log"]
    V --> W([สิ้นสุด])
    F --> W
    S --> W
```

### ข้อควรยืนยัน

- เกณฑ์ที่มี Evaluation ใช้งานแล้วควรถูกล็อกถาวร
- การเปลี่ยน Criteria Version ระหว่างรอบต้องกำหนดว่าจะใช้กับ Evaluation ใหม่เท่านั้น หรือห้ามเปลี่ยนจนกว่าจะสร้างรอบใหม่
- ผลรวมของน้ำหนักและหลักการปัดเศษต้องอ้างอิง Scoring Rule Specification

---

## 9. PF-EVA-001: Evaluator Select Applicant Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Evaluator เปิดรายชื่อผู้สมัคร"]
    B --> C{"บัญชี Active หรือไม่"}
    C -- ไม่ --> D["Access Denied"]
    C -- ใช่ --> E["เลือกรอบทุนที่ Open"]
    E --> F["ค้นหาด้วยรหัสนักศึกษา ชื่อ หรือนามสกุล"]
    F --> G["แสดงข้อมูลขั้นต่ำสำหรับการเลือก"]
    G --> H["Evaluator เลือกผู้สมัคร"]
    H --> I["Backend เริ่ม Transaction<br/>และ Lock Applicant-Round"]
    I --> J{"รอบทุนยัง Open หรือไม่"}
    J -- ไม่ --> K["Rollback: ROUND_NOT_OPEN"]
    J -- ใช่ --> L{"ผู้ประเมินมี Evaluation<br/>ที่ยังไม่ถูกยกเลิกอยู่แล้วหรือไม่"}
    L -- ใช่ --> M["Rollback: DUPLICATE_EVALUATOR"]
    L -- ไม่ --> N["นับ Evaluation ที่ยังไม่ถูกยกเลิก"]
    N --> O{"จำนวน < 3 หรือไม่"}
    O -- ไม่ --> P["Rollback: EVALUATOR_LIMIT_REACHED"]
    O -- ใช่ --> Q["สร้าง Evaluation สถานะ Draft<br/>ผูก Applicant, Round, Evaluator และ Criteria Version"]
    Q --> R["Commit Transaction"]
    R --> S["สร้างสิทธิ์เข้าถึงข้อมูลละเอียดและเอกสาร"]
    S --> T["เปิดหน้า Evaluation Form"]
    T --> U([สิ้นสุด])
    D --> U
    K --> U
    M --> U
    P --> U
```

### Concurrency Control

การตรวจจำนวนผู้ประเมินและการสร้าง Evaluation ต้องอยู่ใน Transaction เดียวกัน เพื่อป้องกันอาจารย์หลายคนเลือกผู้สมัครพร้อมกันจนเกิน 3 คน

---

## 10. PF-EVA-002: Draft–Review–Submit Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Evaluator เปิด Evaluation ของตนเอง"]
    B --> C{"สถานะเป็น Draft<br/>หรือ Reopened หรือไม่"}
    C -- ไม่ --> D["เปิดแบบ Read-only"]
    C -- ใช่ --> E["แสดงข้อมูลผู้สมัคร เอกสาร<br/>Criteria และแบบฟอร์ม"]
    E --> F["กรอกคะแนนและความคิดเห็น"]
    F --> G["ตรวจช่วงคะแนนฝั่ง Client"]
    G --> H{"ผู้ใช้กด Save Draft หรือ Review"}
    H -- Save Draft --> I["ส่งข้อมูลไป Backend"]
    I --> J{"ตรวจ Owner, Round, Status<br/>และ Validation ผ่านหรือไม่"}
    J -- ไม่ --> K["แสดง Error และไม่บันทึก"]
    J -- ใช่ --> L["บันทึก Draft และ updated_at"]
    L --> E
    H -- Review --> M["ตรวจความครบถ้วนฝั่ง Client"]
    M --> N{"ข้อมูลครบหรือไม่"}
    N -- ไม่ --> O["แสดงรายการที่ต้องแก้ไข"]
    O --> E
    N -- ใช่ --> P["แสดง Review Before Submit"]
    P --> Q{"Evaluator ยืนยัน Submit หรือไม่"}
    Q -- ไม่ --> E
    Q -- ใช่ --> R["Backend เริ่ม Transaction"]
    R --> S{"Owner ถูกต้อง บัญชี Active<br/>รอบ Open และสถานะแก้ไขได้หรือไม่"}
    S -- ไม่ --> T["Rollback และแจ้ง Error"]
    S -- ใช่ --> U["ตรวจ Required, ช่วงคะแนน<br/>ความคิดเห็น และ Criteria Version"]
    U --> V{"ผ่าน Validation หรือไม่"}
    V -- ไม่ --> W["Rollback และส่ง Field Errors"]
    V -- ใช่ --> X["คำนวณคะแนนรวมรายผู้ประเมิน"]
    X --> Y["เปลี่ยนสถานะเป็น Submitted<br/>บันทึก submitted_at และ Snapshot"]
    Y --> Z["Commit Transaction"]
    Z --> AA["บันทึก Audit Event"]
    AA --> AB["เรียก Score Calculation Flow"]
    AB --> AC["แสดง Submit Success แบบ Read-only"]
    D --> AD([สิ้นสุด])
    K --> AD
    T --> AD
    W --> AD
    AC --> AD
```

---

## 11. PF-SCR-001: Score Calculation Flow

```mermaid
flowchart TD
    A([Trigger: Submit, Reopen,<br/>Cancel หรือ Close Round]) --> B["โหลด Evaluation ของ Applicant-Round"]
    B --> C["กรองเฉพาะสถานะ Submitted<br/>และไม่ถูกยกเลิก"]
    C --> D["ตรวจผู้ประเมินไม่ซ้ำกัน<br/>และจำนวนไม่เกิน 3"]
    D --> E["คำนวณคะแนนรวมของแต่ละ Evaluator<br/>ตาม Criteria Version และ Scoring Rule"]
    E --> F["นับจำนวน Submitted"]
    F --> G{"Submitted เท่ากับ 0 หรือไม่"}
    G -- ใช่ --> H["ลบ/ไม่สร้าง Result Summary<br/>สถานะ Not Started หรือ In Progress<br/>ตามจำนวน Draft"]
    G -- ไม่ --> I{"Submitted น้อยกว่า 2 หรือไม่"}
    I -- ใช่ --> J["ยังไม่สร้างคะแนนสรุป<br/>สถานะ In Progress"]
    I -- ไม่ --> K["คำนวณ Aggregate Score<br/>จาก Submitted 2–3 คน"]
    K --> L["ปัดเศษตาม Scoring Rule"]
    L --> M["Upsert Result Summary<br/>เก็บ count, score, version และ calculated_at"]
    M --> N{"รอบทุน Open หรือ Closed"}
    N -- Open --> O{"Submitted = 2 หรือ 3"}
    O -- 2 --> P["สถานะ Minimum Complete"]
    O -- 3 --> Q["สถานะ Fully Complete"]
    N -- Closed --> R{"Submitted >= 2 หรือไม่"}
    R -- ใช่ --> S["สถานะ Finalized<br/>ยืนยัน Summary ล่าสุดเป็นผลสุดท้าย"]
    R -- ไม่ --> T["สถานะ Closed Incomplete<br/>ไม่มี Final Score"]
    H --> U["ปรับ Dashboard และ Report View"]
    J --> U
    P --> U
    Q --> U
    S --> U
    T --> U
    U --> V["บันทึก Calculation Audit/Version"]
    V --> W([สิ้นสุด])
```

### หลักการคำนวณ

- Draft, Reopened ที่ยังไม่ Submit และรายการที่ถูกยกเลิกต้องไม่ถูกนำมาคำนวณ
- Result Summary มีได้ไม่เกิน 1 รายการต่อ Applicant-Round แต่ควรมี `calculation_version` หรือประวัติการคำนวณ
- สูตร น้ำหนัก ค่าเฉลี่ย และการปัดเศษต้องอ่านจาก Scoring Rule Specification ที่อนุมัติแล้ว

---

## 12. PF-SCR-002: Third Evaluator Recalculation Flow

```mermaid
flowchart TD
    A([ผู้ประเมินคนที่ 3 ยืนยัน Submit]) --> B["Backend ตรวจ Owner และ Validation"]
    B --> C{"รอบทุนยัง Open หรือไม่"}
    C -- ไม่ --> D["ปฏิเสธ ROUND_NOT_OPEN"]
    C -- ใช่ --> E["เริ่ม Transaction และ Lock Applicant-Round"]
    E --> F["นับ Submitted ก่อนรายการปัจจุบัน"]
    F --> G{"มี Submitted จากผู้ประเมินไม่ซ้ำกัน 2 คนหรือไม่"}
    G -- ไม่ --> H["ดำเนินการ Submit ปกติ<br/>แล้วใช้ Score Calculation Flow"]
    G -- ใช่ --> I{"จำนวน Evaluation ที่ใช้งานอยู่ <= 3<br/>และไม่มีผู้ประเมินซ้ำหรือไม่"}
    I -- ไม่ --> J["Rollback และแจ้ง Constraint Error"]
    I -- ใช่ --> K["บันทึก Evaluation คนที่ 3 เป็น Submitted"]
    K --> L["โหลด Submitted ทั้ง 3 รายการ"]
    L --> M["คำนวณคะแนนรวมรายผู้ประเมิน"]
    M --> N["คำนวณ Aggregate ใหม่จาก 3 คน"]
    N --> O["เพิ่ม Calculation Version<br/>และแทนที่ Result Summary ล่าสุด"]
    O --> P["เปลี่ยนสถานะ Minimum Complete<br/>เป็น Fully Complete"]
    P --> Q["Commit Transaction"]
    Q --> R["ปรับ Dashboard, Summary และ Report View"]
    R --> S["บันทึก Recalculation Audit Event"]
    S --> T([สิ้นสุด])
    D --> T
    H --> T
    J --> T
```

---

## 13. PF-RND-001: Close Scholarship Round Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin เปิดหน้ารอบทุน"]
    B --> C["เลือกคำสั่ง Close Round"]
    C --> D{"รอบทุนอยู่ในสถานะ Open หรือไม่"}
    D -- ไม่ --> E["ปฏิเสธ INVALID_ROUND_TRANSITION"]
    D -- ใช่ --> F["ระบบสรุปจำนวน Not Started,<br/>In Progress, Minimum Complete<br/>และ Fully Complete"]
    F --> G["แสดงรายชื่อผู้สมัครที่ Submitted < 2"]
    G --> H{"Admin ยืนยันปิดรอบหรือไม่"}
    H -- ไม่ --> I["ยกเลิกการดำเนินการ"]
    H -- ใช่ --> J["เริ่ม Transaction และ Lock Round"]
    J --> K["เปลี่ยน Round เป็น Closed"]
    K --> L["ปิดการสร้าง Evaluation ใหม่<br/>และปิดการ Submit เพิ่มเติม"]
    L --> M["ประมวลผลผู้สมัครทีละราย"]
    M --> N{"Submitted >= 2 หรือไม่"}
    N -- ใช่ --> O["คำนวณ/ยืนยัน Result Summary ล่าสุด"]
    O --> P["เปลี่ยนสถานะเป็น Finalized"]
    N -- ไม่ --> Q["ล้าง Final Score ถ้ามี<br/>และเปลี่ยนเป็น Closed Incomplete"]
    P --> R{"ยังมีผู้สมัครถัดไปหรือไม่"}
    Q --> R
    R -- ใช่ --> M
    R -- ไม่ --> S["ปรับ Dashboard และ Report Snapshot"]
    S --> T["บันทึกผู้ปิดรอบ เวลา และ Audit Event"]
    T --> U["Commit Transaction"]
    U --> V([สิ้นสุด])
    E --> V
    I --> V
```

### ผลหลังปิดรอบ

- ห้ามสร้าง Evaluation ใหม่
- ห้าม Submit เพิ่มเติม
- ผู้สมัครที่ Submitted อย่างน้อย 2 คนเป็น `Finalized`
- ผู้สมัครที่ Submitted น้อยกว่า 2 คนเป็น `Closed Incomplete`
- การแก้ไขภายหลังต้องผ่าน Reopen Policy และอาจต้องเปิดรอบตามกระบวนการอนุมัติ

---

## 14. PF-RPT-001: Export Report Flow

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin เปิดเมนู Report"]
    B --> C["เลือกรอบทุน ตัวกรอง คอลัมน์<br/>และรูปแบบ Excel หรือ CSV"]
    C --> D{"มีสิทธิ์ Export หรือไม่"}
    D -- ไม่ --> E["Access Denied และบันทึกเหตุการณ์"]
    D -- ใช่ --> F["ตรวจความถูกต้องของพารามิเตอร์"]
    F --> G{"พารามิเตอร์ถูกต้องหรือไม่"}
    G -- ไม่ --> H["แสดง INVALID_EXPORT_PARAMETER"]
    G -- ใช่ --> I["Query Applicant, Evaluation,<br/>Criteria และ Result Summary"]
    I --> J["ใช้เฉพาะ Submitted ในสูตรคะแนน<br/>แต่แสดงสถานะ Draft/Submitted ตาม Template"]
    J --> K["สร้าง Dataset ตาม Fixed Template"]
    K --> L["ตรวจจำนวนแถว คะแนนรวม<br/>และสถานะกับฐานข้อมูล"]
    L --> M{"Validation ผ่านหรือไม่"}
    M -- ไม่ --> N["ยกเลิกไฟล์และบันทึก EXPORT_DATA_MISMATCH"]
    M -- ใช่ --> O{"รูปแบบไฟล์"}
    O -- Excel --> P["สร้างไฟล์ .xlsx"]
    O -- CSV --> Q["สร้างไฟล์ .csv พร้อม Encoding ที่กำหนด"]
    P --> R["สร้าง Export Log"]
    Q --> R
    R --> S["บันทึกผู้ส่งออก เวลา รอบทุน<br/>ตัวกรอง จำนวนแถว และ File Hash"]
    S --> T["ส่งไฟล์ให้ดาวน์โหลด"]
    T --> U([สิ้นสุด])
    E --> U
    H --> U
    N --> U
```

---

## 15. PF-EVA-003: Reopen Evaluation Flow

> Confirmed response: owner requests (or staff acts on behalf with reason); Head/delegate independently approves; preserve immutable submitted revision; technical Admin cannot self-approve.

```mermaid
flowchart TD
    A([เริ่มต้น]) --> B["Admin รับคำขอแก้ไขผล Submitted"]
    B --> C["เลือก Evaluation และระบุเหตุผล"]
    C --> D{"Evaluation อยู่ในสถานะ Submitted หรือไม่"}
    D -- ไม่ --> E["ปฏิเสธ INVALID_EVALUATION_STATE"]
    D -- ใช่ --> F{"คำขอได้รับอนุมัติตาม Reopen Policy หรือไม่"}
    F -- ไม่ --> G["ปฏิเสธและบันทึกเหตุผล"]
    F -- ใช่ --> H{"รอบทุนอยู่ในสถานะ Open หรือไม่"}
    H -- ไม่ --> I{"มีการอนุมัติเปิดรอบ<br/>หรือ Exception Process หรือไม่"}
    I -- ไม่ --> J["ปฏิเสธ ROUND_NOT_OPEN"]
    I -- ใช่ --> K["เปิดรอบ/สิทธิ์ชั่วคราวตามนโยบาย"]
    H -- ใช่ --> L["เริ่ม Transaction"]
    K --> L
    L --> M["เก็บ Snapshot ของ Submitted Version เดิม"]
    M --> N["บันทึก Revision เดิมแบบ immutable<br/>และเปลี่ยนเป็น Reopened/Revision Pending"]
    N --> O["เปลี่ยนเป็น Draft สำหรับเจ้าของ Evaluation"]
    O --> P["บันทึกผู้อนุมัติ เหตุผล เวลา<br/>และ Reopen Version"]
    P --> Q["คำนวณ Result Summary ใหม่<br/>โดยไม่ใช้รายการที่ถูกเปิดแก้ไข"]
    Q --> R["Commit Transaction"]
    R --> S["คืน editable copy เป็น Draft<br/>และแจ้ง Evaluator เจ้าของ"]
    S --> T["Evaluator แก้คะแนน/ความคิดเห็น"]
    T --> U["ดำเนิน Draft–Review–Submit Flow"]
    U --> V["เรียก Score Calculation Flow"]
    V --> W["บันทึกผลต่างก่อนและหลังแก้ไข"]
    W --> X([สิ้นสุด])
    E --> X
    G --> X
    J --> X
```

### Audit Data ที่ควรจัดเก็บ

- Evaluation ID และ Version เดิม
- ผู้ร้องขอ ผู้อนุมัติ และผู้แก้ไข
- เหตุผลการ Reopen
- เวลา Reopen และเวลา Submit ใหม่
- คะแนนและความคิดเห็นก่อน–หลัง
- ผลกระทบต่อ Result Summary และสถานะผู้สมัคร

---

## 16. PF-AUTH-003: SSO Error Flow

```mermaid
flowchart TD
    A([เกิดข้อผิดพลาดระหว่าง SSO]) --> B{"ประเภทข้อผิดพลาด"}
    B -- KKU SSO ไม่พร้อมใช้งาน --> C["แสดง SSO_SERVICE_UNAVAILABLE<br/>พร้อมปุ่มลองใหม่ภายหลัง"]
    B -- ผู้ใช้ยกเลิกหรือไม่ยินยอม --> D["แสดง LOGIN_CANCELLED"]
    B -- state ไม่ตรง --> E["ยกเลิก Login Transaction<br/>แสดง INVALID_STATE"]
    B -- Token Exchange ล้มเหลว --> F["แสดง TOKEN_EXCHANGE_FAILED"]
    B -- ID Token/Signature ไม่ถูกต้อง --> G["แสดง INVALID_ID_TOKEN"]
    B -- nonce ไม่ตรง --> H["แสดง INVALID_NONCE"]
    B -- /userinfo ล้มเหลว --> I["แสดง USERINFO_UNAVAILABLE"]
    B -- Claim สำคัญไม่ครบ --> J["แสดง REQUIRED_CLAIM_MISSING"]
    B -- ไม่มีบัญชี SEMS --> K["แสดง SEMS_ACCOUNT_NOT_PROVISIONED"]
    B -- บัญชี Inactive --> L["แสดง SEMS_ACCOUNT_INACTIVE"]
    B -- ไม่มีบทบาทที่อนุญาต --> M["แสดง ACCESS_DENIED"]
    B -- สร้าง Session ไม่สำเร็จ --> N["แสดง SESSION_CREATION_FAILED"]
    E --> O["ลบ state, nonce, code_verifier<br/>และข้อมูล Login ชั่วคราว"]
    F --> O
    G --> O
    H --> O
    I --> O
    J --> O
    N --> O
    C --> P["บันทึก Login Failure Audit"]
    D --> P
    O --> P
    K --> P
    L --> P
    M --> P
    P --> Q["ห้ามบันทึก Token หรือข้อมูลลับ"]
    Q --> R{"ผู้ใช้สามารถแก้ไขเองได้หรือไม่"}
    R -- ลองใหม่ได้ --> S["แสดงปุ่มกลับหน้า Login"]
    R -- ต้องให้ Admin แก้ --> T["แสดงช่องทางติดต่อผู้ดูแลระบบ<br/>พร้อม Correlation ID"]
    S --> U([สิ้นสุด])
    T --> U
```

### แนวทาง Error Handling

- ข้อผิดพลาดด้าน `state`, `nonce`, signature และ token ต้องยกเลิกกระบวนการทันที
- ข้อความที่แสดงต่อผู้ใช้ไม่ควรเปิดเผย token, stack trace, client secret หรือรายละเอียดภายใน
- Log ควรมี `traceId`, เวลา, endpoint, error category และ user identifier เท่าที่จำเป็น
- เมื่อ KKU SSO ไม่พร้อมใช้งาน ควรแยกจากกรณีบัญชี SEMS ไม่มีสิทธิ์ เพื่อให้ผู้ใช้แก้ปัญหาได้ถูกจุด

---

## 17. Traceability กับ Requirement หลัก

| Requirement/Rule | Process Flow ที่ครอบคลุม |
|---|---|
| KKU SSO, Session, RBAC | PF-AUTH-001, PF-AUTH-002, PF-AUTH-003 |
| Import CSV/Excel, Mapping, Preview, Validation | PF-IMP-001, PF-IMP-002 |
| Criteria Versioning และ Lock หลังเริ่มประเมิน | PF-CRI-001 |
| ผู้ประเมินไม่ซ้ำและไม่เกิน 3 คน | PF-EVA-001 |
| Draft, Review, Submit | PF-EVA-002 |
| ใช้เฉพาะ Submitted ในการคำนวณ | PF-SCR-001 |
| คำนวณใหม่เมื่อผู้ประเมินคนที่ 3 Submit | PF-SCR-002 |
| Finalized และ Closed Incomplete | PF-RND-001 |
| Excel/CSV Export และ Export Audit | PF-RPT-001 |
| Reopen หลัง Submit | PF-EVA-003 |

## 18. ประเด็นที่ต้องยืนยันก่อนอนุมัติเอกสาร

1. อนุญาตให้นำเข้าผู้สมัครเฉพาะรอบ `Draft` หรืออนุญาตในรอบ `Open` ด้วย
2. Criteria Version ใหม่สามารถเริ่มใช้กลางรอบได้หรือไม่

3. ผู้มีอำนาจอนุมัติ Reopen Evaluation คือใคร
4. เมื่อรอบ `Closed` ต้องการแก้ Evaluation จะเปิดรอบกลับเป็น `Open` หรือใช้ Exception เฉพาะรายการ
5. ความคิดเห็นเป็นข้อมูลบังคับก่อน Submit หรือไม่
6. สูตรคะแนน น้ำหนัก และหลักการปัดเศษฉบับสุดท้าย
7. Template และ Encoding ของ CSV
8. ระยะเวลาจัดเก็บ Export File, Import File และ Audit Log
9. รูปแบบ Logout ที่ใช้: ออกจาก SEMS เท่านั้น หรือ Full KKU SSO Logout

## Confirmed additional controlled flows

### PF-COR-001 — Controlled Correction

`Admin request → verify application/version → reject student/round/type change → authorize → store before/after snapshot + reason → apply transaction → recalculate affected summaries → audit`.

### PF-RND-002 — Round Reopen and report replacement

`Head/System Owner request → designated approval → reject Archived → mark prior Final snapshot Superseded → reopen Closed round → permitted corrections/resubmissions → recalculate → create new immutable Final snapshot`.

### PF-DOC-001 — Quarantine and malware scan

`Validate extension/MIME/signature/size → store private Quarantined → scan → Clean enables authorized short-lived download; Rejected/Unavailable remains inaccessible → audit`.

### PF-AUTH-004 — Pre-provisioned account and inactive account

`KKU callback → find pre-provisioned SEMS account → bind stable sub on first login → deny USER_NOT_PROVISIONED or inactive → enforce 30-minute idle/8-hour absolute session → revoke on inactive`.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.3 | 2026-07-24 | SEMS Design Team | Confirmed reopen and added Controlled Correction, round/report, quarantine and account/session flows. |
| v1.2 | 2026-07-24 | SEMS Design Team | Aligned import and closed-round errors with module-specific canonical codes. |
| v1.1 | 2026-07-23 | SEMS Design Team | Standardized observability correlation on `traceId`. |
| v1.0 | 2026-07-23 | SEMS Design Team | Initial process flow specification draft. |
