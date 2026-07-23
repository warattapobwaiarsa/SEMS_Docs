# Scholarship Evaluation Management System (SEMS)

> **ระบบบริหารจัดการการประเมินทุนการศึกษา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยขอนแก่น**

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.3** |
| Last Updated | **2026-07-23** |
| Repository Type | Documentation |

คลังเอกสารสำหรับการวิเคราะห์ ออกแบบ ทดสอบ และนำระบบ SEMS ขึ้นใช้งาน โดยจัดเอกสารตามวงจรการพัฒนาระบบ

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

| Category | Scope | Key Documents |
| :--- | :--- | :--- |
| 📖 **Repository Governance** | Documentation versioning, Commit, Branch, Pull Request, and safety rules | [`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md) (v1.1), [`CONTRIBUTING.md`](./CONTRIBUTING.md) (v1.0) |
| 📋 **[Requirements](./Requirements/README.md)** | PRD, SRS, proposals, user stories, meeting notes | `SEMS-project-proposal.pdf` (v1.0) |
| 🎨 **[Design](./Design/README.md)** | Architecture, APIs, database, scoring criteria, import templates, UI/UX | `kku-oauth-summary.md` (v1.0), `Criteria.xlsx` (v1.0), `Data_import_to_web.xlsx` (v1.0) |
| 🧪 **[Testing](./Testing/README.md)** | Test plans, test cases, UAT | No documents indexed yet |
| 🚀 **[Deployment](./Deployment/README.md)** | Setup guides, system administration, user manuals | No documents indexed yet |

## 🛠️ Technology Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS
- **Backend:** NestJS, TypeScript
- **Database:** PostgreSQL, Prisma ORM
- **Authentication:** KKU SSO / OAuth 2.1 / OpenID Connect
- **Testing:** Jest, Playwright, Postman

## Revision History

| Version | Date | Change |
| :--- | :--- | :--- |
| v1.3 | 2026-07-23 | Added `CONTRIBUTING.md` v1.0 and updated the documentation policy to v1.1. |
| v1.2 | 2026-07-23 | Added `DOCUMENTATION_POLICY.md` v1.0 and indexed the repository governance rules. |
| v1.1 | 2026-07-23 | Re-indexed all categories, added document version metadata, and moved the KKU OAuth summary into `Design/API/`. |
| v1.0 | 2026-07-22 | Established the four-category SEMS documentation structure and indexed the proposal, scoring criteria, and data-import template. |
