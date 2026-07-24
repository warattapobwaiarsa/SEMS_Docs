# นโยบายการกำกับดูแลเอกสารโครงการ SEMS

| รายการ | รายละเอียด |
| :--- | :--- |
| ชื่อเอกสาร | Documentation Governance Policy |
| Version | **v1.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| สถานะ | ฉบับใช้งาน |

## 1. วัตถุประสงค์ (Purpose)

นโยบายฉบับนี้กำหนดมาตรฐานกลางสำหรับการจัดเก็บ การอัปเดต และการควบคุมเวอร์ชันเอกสารของโครงการ **Scholarship Evaluation Management System (SEMS)** เพื่อให้เอกสารค้นหาได้ง่าย มีข้อมูลล่าสุด และสามารถตรวจสอบประวัติการเปลี่ยนแปลงได้

นโยบายนี้มีวัตถุประสงค์เพื่อป้องกันปัญหาต่อไปนี้:

- ไฟล์ชื่อซ้ำหรือมีหลายสำเนาโดยไม่ทราบว่าไฟล์ใดเป็นฉบับล่าสุด
- เอกสารไม่สอดคล้องกับ Scope, Business Logic หรือการทำงานปัจจุบันของระบบ
- เลขเวอร์ชันในเอกสาร, README และผัง Repository ไม่ตรงกัน
- การเพิ่ม ย้าย หรือลบเอกสารโดยไม่มีประวัติให้ตรวจสอบย้อนหลัง

นโยบายนี้ใช้กับเอกสารทุกประเภทใน Repository เช่น Markdown, PDF, Word, Excel, รูปภาพ และไฟล์ประกอบอื่น ๆ

## 2. นโยบายการระบุเวอร์ชัน (Versioning Policy)

### 2.1 รูปแบบเวอร์ชัน

เอกสารใช้รูปแบบ **`vX.Y`** โดย `X` คือ Major Version และ `Y` คือ Minor Version

| ประเภท | ตัวอย่าง | ใช้เมื่อ |
| :--- | :---: | :--- |
| **Pre-baseline** | `v0.1` → `v0.2` | Working Draft / Pre-baseline ที่ยังไม่อนุมัติ |
| **First official** | `v1.0` | First Approved หรือ First Official Release เท่านั้น |
| **Minor** | `v1.0` → `v1.1` | แก้ไขที่ไม่เปลี่ยนสาระหลักหลังออกฉบับทางการ |
| **Major** | `v1.x` → `v2.0` | เปลี่ยน Scope, Business Logic หรือกระบวนการสำคัญหลังออกฉบับทางการ |

ข้อกำหนดเพิ่มเติม:

- เอกสาร Draft ก่อน Baseline เริ่มที่ **`v0.1`** และเพิ่ม `v0.x` ตามการแก้ไข
- ห้ามเปลี่ยนเป็น `v1.0`, Current หรือ Approved จนมีหลักฐานการอนุมัติ/การออกฉบับทางการ
- เลขเวอร์ชันของเอกสารแต่ละฉบับเป็นอิสระจากเลขเวอร์ชันของ Repository และ README
- เมื่อเพิ่ม แก้ไข ย้าย หรือลบเอกสาร ให้ปรับ Minor Version ของ README หรือ Index ที่ได้รับผลกระทบ
- ห้ามสร้างสำเนาชื่อเช่น `final`, `final2`, `latest` หรือ `new`; ให้ใช้เลขเวอร์ชันและ Revision History แทน

### 2.2 มาตรฐาน Header ของเอกสาร Markdown

เอกสาร Markdown (`.md`) ทุกฉบับต้องมีข้อมูลอย่างน้อยดังนี้:

```markdown
| รายการ | รายละเอียด |
| :--- | :--- |
| Version | **v1.0** |
| Last Updated | **YYYY-MM-DD** |
| Author | **ชื่อบุคคลหรือทีมผู้รับผิดชอบ** |
```

- `Version` ต้องตรงกับเวอร์ชันที่ระบุใน README และ `REPOSITORY_TREE.md`
- `Last Updated` ใช้รูปแบบวันที่ `YYYY-MM-DD`
- `Author` ระบุผู้จัดทำ ผู้แก้ไขหลัก หรือทีมที่รับผิดชอบ

สำหรับไฟล์ที่ไม่ใช่ Markdown ให้บันทึก Version, Last Updated และผู้รับผิดชอบไว้ใน README ของโฟลเดอร์ที่จัดเก็บไฟล์นั้น

### 2.3 มาตรฐาน Revision History

README และไฟล์ Index ทุกฉบับต้องมีตาราง **Revision History** อย่างน้อยในรูปแบบต่อไปนี้:

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.0 | YYYY-MM-DD | ชื่อผู้รับผิดชอบ | สร้างเอกสารฉบับแรก |

รายการล่าสุดต้องอยู่ด้านบน และคำอธิบายต้องระบุว่าเพิ่ม แก้ไข ย้าย หรือลบเอกสารใด

## 3. ขั้นตอนการอัปเดตเอกสาร (Document Update Workflow)

### ขั้นตอนที่ 1: จัดหมวดหมู่เอกสาร

เอกสารใหม่ต้องอยู่ในหนึ่งในสี่หมวดหมู่หลัก:

| หมวดหมู่ | ขอบเขต |
| :--- | :--- |
| 📋 **Requirements** | PRD, SRS, proposals, user stories และ meeting notes |
| 🎨 **Design** | Architecture, API, database, scoring criteria, data templates และ UI/UX |
| 🧪 **Testing** | Test plans, test cases และ UAT |
| 🚀 **Deployment** | Setup guides, system manuals และ user manuals |

หากไม่แน่ใจ ให้เลือกหมวดหมู่ตามวัตถุประสงค์หลักของเอกสาร และหลีกเลี่ยงการเก็บสำเนาเดียวกันไว้หลายหมวดหมู่

### ขั้นตอนที่ 2: กำหนดหรือปรับเวอร์ชัน

1. กำหนดเอกสารใหม่ที่ยังไม่ผ่าน Baseline เป็น `v0.1`; ใช้ `v1.0` เฉพาะ First Approved หรือ First Official Release
2. ประเมินการเปลี่ยนแปลงว่าเป็น Major หรือ Minor
3. อัปเดต Version, Last Updated และ Author
4. เพิ่มรายการใน Revision History

### ขั้นตอนที่ 3: อัปเดต Index และ Repository Tree

เมื่อมีการเพิ่ม แก้ไข ย้าย หรือลบไฟล์ ต้องดำเนินการดังนี้:

1. อัปเดต `README.md` ของโฟลเดอร์ที่ได้รับผลกระทบ
2. อัปเดต Root `README.md` หากรายการเอกสารสำคัญหรือโครงสร้างหลักเปลี่ยน
3. อัปเดต `REPOSITORY_TREE.md` ให้ตรงกับเส้นทางจริง
4. ระบุ Version Tag ของไฟล์สำคัญใน `REPOSITORY_TREE.md`
5. ตรวจสอบว่า Markdown links ทุกลิงก์เปิดไปยังไฟล์ที่มีอยู่จริง

### ขั้นตอนที่ 4: สร้าง Change Summary

Commit, Pull Request หรือรายงานสรุปการอัปเดตต้องระบุอย่างน้อย:

รูปแบบ Commit Message, Branch และ Pull Request ให้ปฏิบัติตาม [`CONTRIBUTING.md`](./CONTRIBUTING.md)

| รายการ | รายละเอียดที่ต้องระบุ |
| :--- | :--- |
| Added | ไฟล์ที่เพิ่มและเวอร์ชันเริ่มต้น |
| Updated | ไฟล์ที่แก้ไขและเวอร์ชันใหม่ |
| Moved | เส้นทางเดิมและเส้นทางใหม่ |
| Removed | ไฟล์ที่ลบและเหตุผล |
| Indexes | README และ Index ที่ปรับปรุง |

ตัวอย่าง:

```text
Added: Design/API/example.md (v1.0)
Updated: Design/README.md (v1.1 → v1.2)
Updated: REPOSITORY_TREE.md (v1.1 → v1.2)
```

## 4. กฎการป้องกันและข้อห้าม (Safety Guidelines & Constraints)

### 4.1 การลบหรือย้ายไฟล์

- ห้ามลบหรือย้ายไฟล์โดยไม่มีเหตุผลและไม่มีการบันทึก
- ก่อนย้ายไฟล์ ต้องตรวจสอบ README, Index และลิงก์ที่อ้างถึงไฟล์เดิม
- การย้ายหรือลบต้องระบุใน Revision History และ Change Summary
- หากเอกสารยังมีคุณค่าทางประวัติศาสตร์แต่ไม่ใช้งานแล้ว ให้พิจารณาระบุสถานะ `Deprecated` หรือจัดเก็บในพื้นที่ Archive ที่ทีมอนุมัติ แทนการลบทันที

### 4.2 ข้อมูลลับและข้อมูลส่วนบุคคล

ห้ามบันทึกข้อมูลต่อไปนี้ใน Repository:

- Password, Access Token, Refresh Token, API Key, Secret Key หรือ Client Secret
- ข้อมูลส่วนบุคคลจริงของผู้สมัครทุน เช่น ชื่อ เลขประจำตัว ที่อยู่ เบอร์โทรศัพท์ อีเมล ผลการเรียน หรือข้อมูลทางการเงิน
- ข้อมูลการประเมินจริงที่สามารถเชื่อมโยงกลับไปยังบุคคลได้
- ไฟล์ Configuration ที่มี Credential หรือค่าลับของระบบ

เอกสาร ตัวอย่าง และ Data Template ต้องใช้ **Mock Data**, ค่าจำลอง หรือ Placeholder เท่านั้น เช่น `student@example.com`, `STUDENT_ID_001` และ `<CLIENT_SECRET>`

หากพบข้อมูลลับหรือข้อมูลจริง ให้หยุดเผยแพร่ไฟล์ แจ้งผู้รับผิดชอบ และดำเนินการลบข้อมูลออกจากประวัติ Repository ตามกระบวนการรักษาความปลอดภัยของโครงการ

## 5. นโยบายภาษาและคำศัพท์ (Language and Terminology Policy)

### 5.1 หลักการ Thai-first

- ใช้ภาษาไทยเป็นหลักสำหรับคำอธิบาย วัตถุประสงค์ ขั้นตอน เงื่อนไข เหตุผล ความเสี่ยง และผลที่คาดหวังซึ่งจัดทำสำหรับอาจารย์ที่ปรึกษา เจ้าหน้าที่งานทุน ผู้ประเมิน Product Owner และผู้มีส่วนเกี่ยวข้องทั่วไป
- ชื่อมาตรฐาน เทคโนโลยี และคำศัพท์ทางเทคนิคอาจใช้ภาษาอังกฤษ โดยแนะนำคำไทยร่วมกับคำมาตรฐานในวงเล็บหรือ backticks เมื่อกล่าวครั้งแรก
- หลีกเลี่ยงประโยคที่สลับภาษาโดยไม่จำเป็น เช่น “Admin ทำการ Manage และ Close Round”; ให้เขียนว่า “ผู้ดูแลระบบจัดการและปิดรอบทุน”
- ไฟล์และข้อความอ้างอิงทางประวัติศาสตร์ไม่ต้องแปลย้อนหลัง หากการแก้ไขอาจทำให้ไม่ตรงกับหลักฐานหรือต้นฉบับ

### 5.2 ตัวระบุทางเทคนิค

รายการต่อไปนี้ต้องคงภาษาอังกฤษ รูปแบบตัวพิมพ์ และการสะกดเดิม:

- Folder name, file name, Document ID, Requirement ID, Decision ID และ Test Case ID
- HTTP method, API path, `operationId`, request/response field และ JSON key
- Database entity/column, Prisma model/enum, constraint และ source-code identifier
- Error code, role code, system state, protocol และ technology name

ให้ใส่ backticks รอบตัวระบุเมื่อกล่าวใน prose เช่น `ADMIN`, `round_id`, `POST /evaluations` และ `EVALUATION_NOT_FOUND`

### 5.3 บทบาทและสถานะ

- ใช้ “ผู้ดูแลระบบ” ในคำอธิบาย และใช้ `ADMIN` เมื่อหมายถึง role code
- ใช้ “ผู้ประเมิน” ในคำอธิบาย และใช้ `EVALUATOR` เมื่อหมายถึง role code
- “เจ้าหน้าที่งานทุน”, “หัวหน้างานทุน” และ “ผู้อนุมัติ” เป็นหน้าที่ทางธุรกิจ ไม่ใช่คำแทน `ADMIN` โดยอัตโนมัติ
- ค่าที่ระบบจัดเก็บหรือส่งผ่าน API ต้องใช้ canonical enum เช่น `DRAFT`, `OPEN`, `CLOSED`, `ARCHIVED`, `SUBMITTED`, `REOPENED`, `CANCELLED`, `NOT_STARTED`, `IN_PROGRESS`, `MINIMUM_COMPLETE`, `FULLY_COMPLETE`, `FINALIZED` และ `CLOSED_INCOMPLETE`
- Title Case เช่น “Draft” หรือ “Minimum Complete” ใช้ได้เมื่อเป็นข้อความแสดงผลบนหน้าจอเท่านั้น; requirement, API contract และ expected result ต้องใช้ canonical enum

### 5.4 หัวข้อ Metadata และไฟล์ Machine-readable

- หัวข้อเชิงอธิบายใช้ภาษาไทยเป็นหลัก โดยคงชื่อมาตรฐาน เช่น API, RBAC, SRS และ UAT
- ใช้ Metadata keys `Document ID`, `Version`, `Last Updated`, `Author` และ `Status` อย่างสม่ำเสมอเพื่อรองรับเครื่องมือตรวจเอกสาร
- ห้ามแปลหรือ reformat ไฟล์ machine-readable เช่น YAML, JSON, CSV, Prisma, source code และ executable artifact เพื่อวัตถุประสงค์ด้านภาษา
- Markdown ที่แปลงจาก PDF หรือ Workbook ต้องรักษาความสัมพันธ์กับต้นฉบับ และไม่แก้ข้อความเพียงเพื่อให้ตรงกับ style guide หากจะทำให้เนื้อหาไม่ตรงกัน

### 5.5 คำศัพท์มาตรฐาน

| แนวคิด | คำไทยที่ใช้ | คำเทคนิค/ค่าระบบ |
| :--- | :--- | :--- |
| System administrator | ผู้ดูแลระบบ | `ADMIN` / Admin |
| Scholarship officer | เจ้าหน้าที่งานทุน | Scholarship Officer |
| Evaluator | ผู้ประเมิน | `EVALUATOR` / Evaluator |
| Applicant | ผู้สมัคร | Applicant |
| Scholarship application | ใบสมัครทุน | Application |
| Scholarship round | รอบทุน | Scholarship Round |
| Evaluation | รายการประเมิน / ผลการประเมิน | Evaluation |
| Save draft | บันทึกแบบร่าง | Save Draft / `DRAFT` |
| Submit evaluation | ส่งผลการประเมิน | Submit / `SUBMITTED` |
| Reopen evaluation | เปิดผลการประเมินให้แก้ไข | Reopen Evaluation / `REOPENED` |
| Criteria set | ชุดเกณฑ์ | Criteria Set |
| Criteria version | เวอร์ชันเกณฑ์ | Criteria Version |
| Result summary | ผลสรุปคะแนน | Result Summary |
| Latest score | คะแนนล่าสุด | Latest Score |
| Final score | คะแนนสุดท้าย | Final Score |
| Data import | การนำเข้าข้อมูล | Data Import |
| Column mapping | การจับคู่คอลัมน์ | Column Mapping |
| Error report | รายงานข้อผิดพลาด | Error Report |
| Role-based access control | การควบคุมสิทธิ์ตามบทบาท | `RBAC` |
| Audit trail | ประวัติการตรวจสอบย้อนหลัง | Audit Trail |
| Controlled correction | การแก้ไขแบบควบคุม | Controlled Correction |
| Report snapshot | ภาพบันทึกรายงาน | Report Snapshot |
| Baseline candidate | เอกสารเสนอเป็น baseline | `Baseline Candidate` |
| Pending formal approval | รอการอนุมัติอย่างเป็นทางการ | `Pending Formal Approval` |

### 5.6 Checklist ด้านภาษา

- [ ] คำอธิบายสำหรับผู้มีส่วนเกี่ยวข้องใช้ภาษาไทยเป็นหลัก
- [ ] ตัวระบุทางเทคนิคและค่าระบบคงรูปเดิม
- [ ] บทบาททางธุรกิจไม่ถูกใช้แทน role code โดยไม่มี mapping
- [ ] ประโยคผสมภาษาอ่านได้ชัดเจนและไม่มี English verb ที่ไม่จำเป็น
- [ ] Approval status และข้อความ Revision History เดิมไม่ถูกเปลี่ยนความหมาย
- [ ] Machine-readable และ reference artifacts ไม่ถูกแก้เพียงเพื่อปรับภาษา

## 6. Checklist ก่อน Commit หรือ Pull Request

- [ ] เอกสารอยู่ในหมวดหมู่ที่ถูกต้อง
- [ ] Version, Last Updated และ Author เป็นปัจจุบัน
- [ ] Revision History ระบุการเปลี่ยนแปลงแล้ว
- [ ] README ของโฟลเดอร์ได้รับการอัปเดต
- [ ] Root `README.md` ได้รับการอัปเดตเมื่อจำเป็น
- [ ] `REPOSITORY_TREE.md` ตรงกับโครงสร้างจริงและมี Version Tag
- [ ] Markdown links ใช้งานได้
- [ ] Change Summary ระบุไฟล์และเวอร์ชันครบถ้วน
- [ ] ไม่มี Secret หรือข้อมูลส่วนบุคคลจริง

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.3 | 2026-07-24 | SEMS Documentation Team | เพิ่มนโยบาย Thai-first คำศัพท์มาตรฐาน กฎตัวระบุทางเทคนิค และชี้แจงการเริ่มเวอร์ชัน `v0.1` สำหรับเอกสาร pre-baseline |
| v1.2 | 2026-07-23 | SEMS Documentation Team | รองรับ `v0.x` สำหรับ Working Draft/Pre-baseline และสงวน `v1.0` สำหรับ First Approved/Official Release |
| v1.1 | 2026-07-23 | SEMS Documentation Team | เชื่อมโยงข้อกำหนด Commit, Branch และ Pull Request ไปยัง `CONTRIBUTING.md` |
| v1.0 | 2026-07-23 | SEMS Documentation Team | จัดทำนโยบายการกำกับดูแลเอกสารและการควบคุมเวอร์ชันฉบับแรก |
