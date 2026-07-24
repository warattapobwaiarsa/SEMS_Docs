# แนวทางการ Commit และมีส่วนร่วมในโครงการ SEMS

| รายการ | รายละเอียด |
| :--- | :--- |
| Version | **v1.1** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Development Team** |
| สถานะ | ฉบับใช้งาน |

เอกสารนี้กำหนดมาตรฐานการสร้าง Branch, Commit และ Pull Request สำหรับ Repository ของโครงการ **Scholarship Evaluation Management System (SEMS)**

การจัดการและควบคุมเวอร์ชันเอกสารต้องเป็นไปตาม [`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md)
คำอธิบายในเอกสารใช้ภาษาไทยเป็นหลัก โดยคงตัวระบุทางเทคนิคเป็นภาษาอังกฤษตามนโยบายเดียวกัน

## 1. หลักการ Commit

- Commit หนึ่งรายการควรมีวัตถุประสงค์เดียวและสามารถตรวจสอบได้ง่าย
- ห้ามรวมการแก้ไขที่ไม่เกี่ยวข้องกันไว้ใน Commit เดียว
- Commit เฉพาะไฟล์ที่เกี่ยวข้องกับงาน และตรวจสอบรายการไฟล์ก่อน Commit
- ห้าม Commit รหัสผ่าน, Token, API Key, Secret, Credential หรือข้อมูลส่วนบุคคลจริง
- ห้ามใช้ข้อความกำกวม เช่น `update`, `fix`, `changes` หรือ `final`
- ห้าม Commit ไฟล์ชั่วคราว ไฟล์ Build หรือไฟล์ตั้งค่าส่วนตัวที่ไม่จำเป็น

## 2. รูปแบบ Commit Message

ใช้รูปแบบ:

```text
<type>(<scope>): <summary>
```

`scope` สามารถละได้หากการเปลี่ยนแปลงครอบคลุมทั้ง Repository:

```text
<type>: <summary>
```

### Commit Types

| Type | ใช้เมื่อ |
| :--- | :--- |
| `feat` | เพิ่มความสามารถใหม่ของระบบ |
| `fix` | แก้ไขข้อผิดพลาด |
| `docs` | เพิ่มหรือแก้ไขเอกสาร |
| `test` | เพิ่มหรือแก้ไขการทดสอบ |
| `refactor` | ปรับโครงสร้างโค้ดโดยไม่เปลี่ยนพฤติกรรม |
| `chore` | งานบำรุงรักษา การตั้งค่า หรือจัดระเบียบ Repository |

### Scopes ที่แนะนำ

| Scope | ขอบเขต |
| :--- | :--- |
| `requirements` | Requirements, SRS, proposals และ user stories |
| `design` | Architecture, API, database, criteria และ UI/UX |
| `testing` | Test plans, test cases และ UAT |
| `deployment` | Setup guides, deployment และ user manuals |
| `repo` | โครงสร้าง Repository, policy และ root indexes |

### ตัวอย่าง

```text
docs(requirements): update scholarship proposal to v1.1
docs(design): add OAuth integration guide
test(testing): add evaluator UAT cases
chore(repo): reorganize documentation indexes
fix(deployment): correct database setup command
```

### กฎการเขียน Summary

- ใช้ภาษาอังกฤษสำหรับ Commit summary และ Pull Request title
- เขียนให้กระชับและอธิบายสิ่งที่เปลี่ยน
- ไม่ต้องใส่จุดท้ายข้อความ
- หากมี Breaking Change ให้ระบุ `!` หลัง type หรือ scope และอธิบายใน Pull Request

```text
docs(requirements)!: revise scholarship scoring process
```

## 3. นโยบาย Branch

ห้าม Commit โดยตรงเข้า Branch หลัก เว้นแต่ผู้ดูแล Repository อนุมัติ

ใช้รูปแบบชื่อ Branch:

```text
<type>/<short-description>
```

ตัวอย่าง:

```text
docs/update-documentation-policy
feat/add-evaluation-round
fix/correct-score-calculation
test/add-uat-cases
```

ชื่อ Branch ต้องใช้ตัวพิมพ์เล็ก คั่นคำด้วย `-` และไม่มีข้อมูลส่วนบุคคล

## 4. ขั้นตอนการทำงาน

1. สร้าง Branch จาก Branch หลักเวอร์ชันล่าสุด
2. เพิ่มหรือแก้ไขเฉพาะไฟล์ที่อยู่ในขอบเขตงาน
3. อัปเดต Version, Last Updated, Revision History และ Index ที่เกี่ยวข้อง
4. ตรวจสอบ Diff และรายการไฟล์ก่อน Commit
5. สร้าง Commit ตามรูปแบบที่กำหนด
6. Push Branch และสร้าง Pull Request
7. แก้ไขข้อเสนอแนะและรับการอนุมัติก่อน Merge

## 5. นโยบาย Pull Request

Pull Request ต้องมีข้อมูลต่อไปนี้:

| หัวข้อ | รายละเอียด |
| :--- | :--- |
| Summary | สรุปวัตถุประสงค์และสิ่งที่เปลี่ยน |
| Changed Files | รายการไฟล์ที่เพิ่ม แก้ไข ย้าย หรือลบ |
| Versions | เวอร์ชันเดิมและเวอร์ชันใหม่ |
| Validation | วิธีตรวจสอบ เช่น link check, test หรือการเปิดตรวจเอกสาร |
| Breaking Changes | ผลกระทบและขั้นตอนที่ผู้ใช้งานต้องดำเนินการ |

ควรมีผู้ตรวจอย่างน้อยหนึ่งคนก่อน Merge และห้าม Merge หากการตรวจสอบที่จำเป็นไม่ผ่าน

## 6. Checklist ก่อน Commit

- [ ] การเปลี่ยนแปลงอยู่ในขอบเขตงานเดียว
- [ ] ไม่มีไฟล์ที่ไม่เกี่ยวข้องหรือไฟล์ชั่วคราว
- [ ] ไม่มี Secret, Credential หรือข้อมูลส่วนบุคคลจริง
- [ ] Version และ Revision History เป็นปัจจุบัน
- [ ] README และ `REPOSITORY_TREE.md` ได้รับการอัปเดตเมื่อจำเป็น
- [ ] Markdown links และการตรวจสอบที่เกี่ยวข้องผ่าน
- [ ] Commit message ตรงตามรูปแบบ `<type>(<scope>): <summary>`
- [ ] คำอธิบายเอกสารเป็น Thai-first และ technical identifiers คงรูปเดิม

## 7. Checklist ก่อน Merge

- [ ] Pull Request มี Summary และ Changed Files ครบถ้วน
- [ ] ระบุเลขเวอร์ชันและ Breaking Changes แล้ว
- [ ] ไม่มีข้อคิดเห็นสำคัญที่ยังไม่ได้แก้ไข
- [ ] การตรวจสอบหรือ Test ที่จำเป็นผ่าน
- [ ] ได้รับการอนุมัติจากผู้ตรวจอย่างน้อยหนึ่งคน

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.1 | 2026-07-24 | SEMS Development Team | เพิ่มกฎ Thai-first สำหรับเอกสารและกำหนด Commit summary กับ Pull Request title เป็นภาษาอังกฤษ |
| v1.0 | 2026-07-23 | SEMS Development Team | กำหนดมาตรฐาน Commit Message, Branch, Pull Request และ Checklist ฉบับแรก |
