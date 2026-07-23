# Scholarship Evaluation Management System (SEMS)

> **ระบบบริหารจัดการการประเมินทุนการศึกษา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยขอนแก่น**

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.11** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Repository Type | Documentation |

คลังเอกสารสำหรับการวิเคราะห์ ออกแบบ ทดสอบ และนำระบบ SEMS ขึ้นใช้งาน โดยจัดเอกสารตามวงจรการพัฒนาระบบ

## 🚦 เริ่มต้นอ่านเอกสาร

หากเพิ่งเข้ามาใน repository นี้ ให้เริ่มที่  
👉 [`START_HERE.md`](./START_HERE.md)

หน้านี้มีลำดับการอ่านตามบทบาท พร้อมลิงก์ไปยังเอกสารทั้งหมด

## 👥 คณะผู้จัดทำ

1. **นายลัญจปรัชญ์ ทัศนียพงค์** (รหัสนักศึกษา: 663040664-8)
2. **นายวรัทภพ ไวอาสา** (รหัสนักศึกษา: 663040665-6)

## 🎯 วัตถุประสงค์

- รวบรวมข้อมูลผู้สมัคร เอกสารประกอบ และประวัติทุนไว้ในระบบเดียว
- รองรับการตรวจเอกสารและให้คะแนนผ่านเว็บ
- คำนวณผลและส่งออกรายงาน Excel หรือ CSV
- ลดความซ้ำซ้อนและข้อผิดพลาดจากการจัดการไฟล์ด้วยตนเอง

## 📂 โครงสร้างคลังเอกสาร

ดูเส้นทางทั้งหมดและเวอร์ชันรายไฟล์ได้ที่ [REPOSITORY_TREE.md](./REPOSITORY_TREE.md)

| Category                                        | Scope                                                                    | Key Documents                                                                                                                                                                                                                                             |
| :---------------------------------------------- | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🚦 **Recommended Entry Point**                  | Reading order, role-based paths, complete file index, and Obsidian setup | [`START_HERE.md`](./START_HERE.md) (v1.0 Current)                                                                                                                                                                                                         |
| 📖 **Repository Governance**                    | Documentation versioning, Commit, Branch, Pull Request, and safety rules | [`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md) (v1.1), [`CONTRIBUTING.md`](./CONTRIBUTING.md) (v1.0)                                                                                                                                              |
| 📋 **[Requirements](./Requirements/README.md)** | PRD, SRS, proposals, user stories, meeting notes                         | SRS (v2.0 Draft), User Stories (v0.1 Draft), Decision Register/Analysis, [Proposal Markdown](./Requirements/Proposal/SEMS-project-proposal.md)                                                                                                            |
| 🎨 **[Design](./Design/README.md)**             | Architecture, APIs, database, scoring criteria, import templates, UI/UX  | API/OpenAPI, Process Flows, Permission Matrix, State Transitions, Scoring Rules, [Data Dictionary](./Design/Database/SEMS_Data_Dictionary/README.md), [Import Mapping](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md), Wireframes |
| 🧪 **[Testing](./Testing/README.md)**           | Test plans, test cases, UAT                                              | 3 Test Plans and 6 Test Case documents (v0.1 Draft)                                                                                                                                                                                                       |
| 🚀 **[Deployment](./Deployment/README.md)**     | Setup guides, system administration, user manuals                        | No documents indexed yet                                                                                                                                                                                                                                  |

## 🛠️ Technology Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS
- **Backend:** NestJS, TypeScript
- **Database:** PostgreSQL, Prisma ORM
- **Authentication:** KKU SSO / OAuth 2.1 / OpenID Connect
- **Testing:** Jest, Playwright, Postman

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.11 | 2026-07-23 | SEMS Documentation Team | Added `START_HERE.md` as the recommended entry point for GitHub and Obsidian readers. |
| v1.10 | 2026-07-23 | SEMS Documentation Team | Updated the wireframe overview with readable English captions. |
| v1.9 | 2026-07-23 | SEMS Documentation Team | Added GitHub-readable PDF and spreadsheet conversions and linked embedded design images and reference artifacts. |
| v1.8 | 2026-07-23 | SEMS Documentation Team | Reorganized and indexed the SRS, User Stories, full Design package, UI/UX wireframes, and deduplicated Testing package. |
| v1.7 | 2026-07-23 | SEMS Documentation Team | Added and indexed `Design/Database/SEMS_Data_Dictionary.xlsx` v1.0 (Draft). |
| v1.6 | 2026-07-23 | SEMS Documentation Team | Added and indexed the Data Dictionary/Import Mapping workbook and guide v0.1 (Draft). |
| v1.5 | 2026-07-23 | SEMS Documentation Team | Added and indexed `Requirements/SEMS_Requirement_Decision_Analysis.md` v1.1 (Draft). |
| v1.4 | 2026-07-23 | SEMS Documentation Team | Added and indexed `Requirements/SEMS_Requirement_Decision_Register.md` v1.0 (Draft). |
| v1.3 | 2026-07-23 | SEMS Documentation Team | Added `CONTRIBUTING.md` v1.0 and updated the documentation policy to v1.1. |
| v1.2 | 2026-07-23 | SEMS Documentation Team | Added `DOCUMENTATION_POLICY.md` v1.0 and indexed the repository governance rules. |
| v1.1 | 2026-07-23 | SEMS Documentation Team | Re-indexed all categories, added document version metadata, and moved the KKU OAuth summary into `Design/API/`. |
| v1.0 | 2026-07-22 | SEMS Documentation Team | Established the four-category SEMS documentation structure and indexed the proposal, scoring criteria, and data-import template. |
