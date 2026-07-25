# Scholarship Evaluation Management System (SEMS)

> **ระบบบริหารจัดการการประเมินทุนการศึกษา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยขอนแก่น**

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.20** |
| Last Updated | **2026-07-25** |
| Author | **SEMS Documentation Team** |
| Repository Type | Documentation |

[START HERE](./START_HERE.md) › Scholarship Evaluation Management System (SEMS)

คลังเอกสารสำหรับการวิเคราะห์ ออกแบบ ทดสอบ และนำระบบ SEMS ขึ้นใช้งาน โดยจัดเอกสารตามวงจรการพัฒนาระบบ

> **Release 1 baseline readiness:** confirmed stakeholder decisions are synchronized across Requirements, Design, API, Database, UI/UX and Testing. Formal approval remains pending because no approver/date/signature evidence is recorded.

## 🚦 เริ่มต้นอ่านเอกสาร

หากเพิ่งเข้ามาใน repository นี้ ให้เริ่มที่
👉 [`START_HERE.md`](./START_HERE.md)

หน้านี้มีลำดับการอ่านตามบทบาท พร้อมลิงก์ไปยังเอกสารทั้งหมด

Markdown ทุกไฟล์มี breadcrumb และ navigation footer มาตรฐานสำหรับกลับ Section Index, กลับ `START_HERE.md` และไปยังเอกสารหรือขั้นตอนถัดไป

เอกสารคำอธิบายใช้ภาษาไทยเป็นหลัก และคงตัวระบุทางเทคนิคเป็นภาษาอังกฤษตาม
[`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md)

เอกสารลำดับถัดไปสำหรับภาพรวมเชิงโครงการคือ [Project Proposal](./Requirements/Proposal/SEMS-project-proposal.md)

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
| 🚦 **Recommended Entry Point** | Reading order, baseline status and complete index | [`START_HERE.md`](./START_HERE.md) (v1.8 Current), [`DOCUMENTATION_REVIEW_REPORT.md`](./DOCUMENTATION_REVIEW_REPORT.md) v0.7 |
| 📖 **Repository Governance** | Versioning, contribution and automated checks | [`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md) (v1.4), [`CONTRIBUTING.md`](./CONTRIBUTING.md) (v1.2) |
| 📋 **[Requirements](./Requirements/README.md)** | PRD, SRS, decisions, stories, traceability and stakeholder records | [PRD](./Requirements/PRD/SEMS-PRD.md) v0.5 Baseline Candidate, [SRS](./Requirements/SRS/SEMS-SRS.md) v0.6 Baseline Candidate, [Stakeholder Questions](./Requirements/Meeting_Notes/SEMS_Stakeholder_Questions.md) v0.2, [Stakeholder Responses](./Requirements/Meeting_Notes/SEMS_Stakeholder_Responses.md) v0.5 Pending Formal Record |
| 🎨 **[Design](./Design/README.md)** | Architecture, API, database, scoring, import and UI/UX | [System Architecture](./Design/Architecture/SEMS_System_Architecture.md), [Error Catalog](./Design/API/SEMS_Error_Code_Catalog.md), OpenAPI, database and scoring drafts |
| 🧪 **[Testing](./Testing/README.md)** | Test plans, cases and synthetic reference data | P0 catalog with linked requirements/decisions and [scoring reference cases](./Testing/Test_Data/SEMS_Scoring_Reference_Cases.md) |
| 🚀 **[Deployment](./Deployment/README.md)** | Deployment index and architecture considerations | Setup/operations guides remain pending |

## 🛠️ Technology Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS
- **Backend:** NestJS, TypeScript
- **Database:** PostgreSQL, Prisma ORM
- **Authentication:** KKU SSO / OAuth 2.1 / OpenID Connect
- **Testing:** Jest, Playwright, Postman

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.20 | 2026-07-25 | SEMS Documentation Team | ซิงก์เวอร์ชัน START HERE หลังเพิ่ม MoSCoW Feature Prioritization ในดัชนีเอกสาร |
| v1.19 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v1.18 | 2026-07-24 | SEMS Documentation Team | เพิ่มมาตรฐาน Thai-first และเชื่อมโยงนโยบายภาษาและคำศัพท์ของ Repository |
| v1.17 | 2026-07-24 | SEMS Documentation Team | Corrected entry-point and requirement versions and linked the Project Proposal from the repository overview. |
| v1.16 | 2026-07-24 | SEMS Documentation Team | Synchronized the Release 1 baseline candidate and retained Pending Formal Approval status. |
| v1.15 | 2026-07-24 | SEMS Documentation Team | Reclassified the stakeholder responses as confirmed, pending a formal record, and synchronized repository indexes. |
| v1.14 | 2026-07-24 | SEMS Documentation Team | Added and indexed stakeholder questions and the advisor-answer simulation under Requirements meeting notes. |
| v1.13 | 2026-07-24 | SEMS Documentation Team | Clarified pre-baseline status and synchronized embedded-point, canonical error-code, traceability and validation-document updates. |
| v1.12 | 2026-07-23 | SEMS Documentation Team | Reconciled pre-baseline requirements/design/testing indexes and linked review, traceability, architecture and governance deliverables. |
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

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: เริ่มต้นชุดเอกสารนี้<br>
↑ หมวดเอกสาร: เอกสารนี้คือ Repository Index<br>
⌂ หน้าหลัก: [START HERE](./START_HERE.md)<br>
→ อ่านต่อ: [🚦 เริ่มต้นใช้งานเอกสาร SEMS (START HERE)](./START_HERE.md)

<!-- DOC_NAV_END -->
