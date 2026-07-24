# 🚦 START HERE — SEMS Documentation

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Documentation Team** |
| Status | **Current** |
| Scope | Main entry point and complete repository document index |

ไฟล์นี้คือจุดเริ่มต้นหลักของคลังเอกสาร Scholarship Evaluation Management System (SEMS) ซึ่งเป็นระบบสำหรับจัดการข้อมูลผู้สมัครทุน ตรวจเอกสาร ประเมินและให้คะแนน คำนวณผล และส่งออกรายงานของคณะวิศวกรรมศาสตร์ มหาวิทยาลัยขอนแก่น

ใช้หน้านี้เพื่อเลือกลำดับการอ่านตามบทบาท และเข้าถึงเอกสารที่เกี่ยวข้องทั้งหมดได้ทั้งบน GitHub และ Obsidian

## ลำดับการอ่านที่แนะนำ

1. [README.md](./README.md) — ภาพรวมโครงการ วัตถุประสงค์ ทีม และ technology stack
2. [Project Proposal](./Requirements/Proposal/SEMS-project-proposal.md) — ที่มา ขอบเขต และแนวคิดของโครงการ
3. [Documentation Review Report](./DOCUMENTATION_REVIEW_REPORT.md) — Critical/Open Decisions และ readiness
4. [PRD](./Requirements/PRD/SEMS-PRD.md) และ [Requirement Decision Register](./Requirements/SEMS_Requirement_Decision_Register.md)
5. [SRS](./Requirements/SRS/SEMS-SRS.md) และ [Traceability Matrix](./Requirements/SEMS_Traceability_Matrix.md)
6. [System Architecture](./Design/Architecture/SEMS_System_Architecture.md) และ [Design Overview](./Design/README.md)
7. [Testing Overview](./Testing/README.md) — test plans, test cases และ reference data
8. [Deployment Overview](./Deployment/README.md)
9. ก่อนแก้ไขเอกสาร อ่าน [Documentation Policy](./DOCUMENTATION_POLICY.md) และ [Contributing Guide](./CONTRIBUTING.md)

> `Requirements/Meeting_Notes/` มีรายการคำถามและคำตอบจากผู้มีส่วนเกี่ยวข้องที่ยืนยันแล้วแต่ยังรอบันทึกทางการ; คำตอบดังกล่าวยังไม่ใช่ Approved Requirement Baseline ส่วน `Testing/UAT/`, `Deployment/Guides/` และ `Deployment/User_Manuals/` ยังไม่มี deliverable ที่อนุมัติ

## เส้นทางการอ่านตามบทบาท

### Product Owner / Business Analyst

1. [Project Proposal](./Requirements/Proposal/SEMS-project-proposal.md)
2. [Requirements Overview](./Requirements/README.md)
3. [Requirement Decision Analysis](./Requirements/SEMS_Requirement_Decision_Analysis.md)
4. [Requirement Decision Register](./Requirements/SEMS_Requirement_Decision_Register.md)
5. [SRS](./Requirements/SRS/SEMS-SRS.md)
6. [User Stories and Acceptance Criteria](./Requirements/User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
7. [Wireframe Specification](./Design/UI_UX/SEMS_Wireframe_Specification.md)
8. [Requirement Baseline Approval Record Template](./Requirements/Approvals/Requirement_Baseline_Approval_Record.md)

### Developer / System Designer

1. [SRS](./Requirements/SRS/SEMS-SRS.md)
2. [Design Overview](./Design/README.md)
3. [System Architecture](./Design/Architecture/SEMS_System_Architecture.md), [Process Flows](./Design/Architecture/SEMS_Process_Flows.md), [Permission Matrix](./Design/Architecture/SEMS_Permission_Matrix.md) และ [State Transition Specification](./Design/Architecture/SEMS_State_Transition_Specification.md)
4. [API Specification](./Design/API/SEMS_API_Specification.md), [Error Code Catalog](./Design/API/SEMS_Error_Code_Catalog.md), [OpenAPI](./Design/API/openapi.yaml) และ [KKU OAuth Summary](./Design/API/kku-oauth-summary.md)
5. [ER / Prisma Data Dictionary](./Design/Database/SEMS_ER_Prisma_Data_Dictionary.md) และ [Data Dictionary Index](./Design/Database/SEMS_Data_Dictionary/README.md)
6. [Scoring Rule Specification](./Design/Criteria/SEMS_Scoring_Rule_Specification.md)
7. [Import Mapping Guide](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md)

### Tester / QA

1. [SRS](./Requirements/SRS/SEMS-SRS.md)
2. [User Stories and Acceptance Criteria](./Requirements/User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
3. [Testing Overview](./Testing/README.md)
4. [Master Test Plan](./Testing/Test_Plans/SEMS_Master_Test_Plan.md)
5. [Risk and Coverage Matrix](./Testing/Test_Plans/SEMS_Risk_and_Coverage_Matrix.md)
6. [Functional Test Case Catalog](./Testing/Test_Cases/SEMS_Functional_Test_Case_Catalog.md)
7. [High-Risk Test Cases](./Testing/Test_Cases/SEMS_High_Risk_Test_Cases.md) และ test cases เฉพาะด้านในดัชนีด้านล่าง
8. [Wireframe UAT Checklist](./Design/UI_UX/Wireframe_UAT_Checklist.md)

### Deployment / Operations / User Support

1. [Project Overview](./README.md)
2. [Deployment Overview](./Deployment/README.md)
3. [Process Flows](./Design/Architecture/SEMS_Process_Flows.md)
4. [Permission Matrix](./Design/Architecture/SEMS_Permission_Matrix.md)
5. [KKU OAuth Summary](./Design/API/kku-oauth-summary.md)
6. [Test Data and Environment Plan](./Testing/Test_Plans/SEMS_Test_Data_and_Environment_Plan.md)

> หมวด Deployment ยังไม่มี setup guide, operations guide หรือ user manual ที่จัดทำดัชนี

## Complete File Index

### Repository

- [README.md](./README.md)
- [START_HERE.md](./START_HERE.md)
- [REPOSITORY_TREE.md](./REPOSITORY_TREE.md)
- [DOCUMENTATION_POLICY.md](./DOCUMENTATION_POLICY.md)
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [.gitignore](./.gitignore)

### Requirements

- [Requirements/README.md](./Requirements/README.md)
- [PRD](./Requirements/PRD/SEMS-PRD.md)
- [Project Proposal — Markdown](./Requirements/Proposal/SEMS-project-proposal.md)
- [Project Proposal — PDF](./Requirements/Proposal/SEMS-project-proposal.pdf)
- [SRS](./Requirements/SRS/SEMS-SRS.md)
- [User Stories Index](./Requirements/User_Stories/README.md)
- [User Stories and Acceptance Criteria](./Requirements/User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
- [Requirement Decision Analysis](./Requirements/SEMS_Requirement_Decision_Analysis.md)
- [Requirement Decision Register](./Requirements/SEMS_Requirement_Decision_Register.md)
- [Traceability Matrix](./Requirements/SEMS_Traceability_Matrix.md)
- [Requirement Baseline Approval Record Template](./Requirements/Approvals/Requirement_Baseline_Approval_Record.md)
- [System Design Approval Record Template](./Requirements/Approvals/System_Design_Approval_Record.md)
- [Meeting Notes Index](./Requirements/Meeting_Notes/README.md)
- [Meeting Note Template](./Requirements/Meeting_Notes/MEETING_NOTE_TEMPLATE.md)
- [Stakeholder Questions](./Requirements/Meeting_Notes/SEMS_Stakeholder_Questions.md)
- [Stakeholder Responses — Pending Formal Record](./Requirements/Meeting_Notes/SEMS_Stakeholder_Responses.md)

### Design — API and Architecture

- [Design Overview](./Design/README.md)
- [API Specification](./Design/API/SEMS_API_Specification.md)
- [Error Code Catalog](./Design/API/SEMS_Error_Code_Catalog.md)
- [OpenAPI Definition](./Design/API/openapi.yaml)
- [Endpoint Matrix](./Design/API/endpoint-matrix.csv)
- [KKU OAuth Summary](./Design/API/kku-oauth-summary.md)
- [Permission Matrix](./Design/Architecture/SEMS_Permission_Matrix.md)
- [System Architecture](./Design/Architecture/SEMS_System_Architecture.md)
- [Process Flows](./Design/Architecture/SEMS_Process_Flows.md)
- [State Transition Specification](./Design/Architecture/SEMS_State_Transition_Specification.md)

### Design — Criteria

- [Criteria Workbook](./Design/Criteria/Criteria.xlsx)
- [Converted Criteria](./Design/Criteria/Criteria_Converted.md)
- [Criteria Configuration](./Design/Criteria/SEMS_Criteria_Config.json)
- [Scoring Rule Specification](./Design/Criteria/SEMS_Scoring_Rule_Specification.md)

### Design — Database

- [Data Dictionary Workbook](./Design/Database/SEMS_Data_Dictionary.xlsx)
- [Data Dictionary Index](./Design/Database/SEMS_Data_Dictionary/README.md)
- [Workbook Overview](./Design/Database/SEMS_Data_Dictionary/00_Workbook_Overview.md)
- [Data Dictionary](./Design/Database/SEMS_Data_Dictionary/01_Data_Dictionary.md)
- [Import Column Mapping](./Design/Database/SEMS_Data_Dictionary/02_Import_Column_Mapping.md)
- [Value Sets](./Design/Database/SEMS_Data_Dictionary/03_Value_Sets.md)
- [Design Decisions](./Design/Database/SEMS_Data_Dictionary/04_Design_Decisions.md)
- [ER Diagram](./Design/Database/SEMS_ER_Diagram.png)
- [ER / Prisma Data Dictionary](./Design/Database/SEMS_ER_Prisma_Data_Dictionary.md)

### Design — Data Templates

- [Data Import Workbook](./Design/Data_Templates/Data_import_to_web.xlsx)
- [Data Import Specification](./Design/Data_Templates/Data_import_to_web_Specification.md)
- [Applicant Import Mapping Specification](./Design/Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md)
- [Applicant Import Mapping Workbook](./Design/Data_Templates/SEMS_Applicant_Import_Mapping_Specification.xlsx)
- [Data Dictionary Import Mapping Workbook](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping.xlsx)
- [Data Dictionary Import Mapping Guide](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md)
- [Import Mapping Index](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md)
- [Import Mapping Overview](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/00_README.md)
- [Entity Model](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/01_ENTITY_MODEL.md)
- [Import Data Dictionary](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/02_DATA_DICTIONARY.md)
- [Import Mapping](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/03_IMPORT_MAPPING.md)
- [Validation Rules](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/04_VALIDATION_RULES.md)
- [Reference Values](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/05_REFERENCE_VALUES.md)
- [Open Decisions](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/06_OPEN_DECISIONS.md)

### Design — UI/UX

- [UI/UX Index](./Design/UI_UX/README.md)
- [Wireframe Specification](./Design/UI_UX/SEMS_Wireframe_Specification.md)
- [Wireframe Prototype](./Design/UI_UX/SEMS_Wireframe_Prototype.html)
- [Wireframe Overview](./Design/UI_UX/SEMS_Wireframe_Overview.png)
- [Wireframe UAT Checklist](./Design/UI_UX/Wireframe_UAT_Checklist.md)
- [Screen Manifest](./Design/UI_UX/screen_manifest.json)
- [01 Login](./Design/UI_UX/screens/01-login.png)
- [02 Dashboard](./Design/UI_UX/screens/02-dashboard.png)
- [03 Rounds](./Design/UI_UX/screens/03-rounds.png)
- [04 Upload](./Design/UI_UX/screens/04-upload.png)
- [05 Mapping](./Design/UI_UX/screens/05-mapping.png)
- [06 Preview](./Design/UI_UX/screens/06-preview.png)
- [07 Errors](./Design/UI_UX/screens/07-errors.png)
- [08 Applicants](./Design/UI_UX/screens/08-applicants.png)
- [09 Applicant Detail](./Design/UI_UX/screens/09-applicant-detail.png)
- [10 Criteria](./Design/UI_UX/screens/10-criteria.png)
- [11 Select Applicant](./Design/UI_UX/screens/11-select-applicant.png)
- [12 Evaluation](./Design/UI_UX/screens/12-evaluation.png)
- [13 Review](./Design/UI_UX/screens/13-review.png)
- [14 Summary](./Design/UI_UX/screens/14-summary.png)
- [15 Export](./Design/UI_UX/screens/15-export.png)

### Testing

- [Testing Overview](./Testing/README.md)
- [Master Test Plan](./Testing/Test_Plans/SEMS_Master_Test_Plan.md)
- [Risk and Coverage Matrix](./Testing/Test_Plans/SEMS_Risk_and_Coverage_Matrix.md)
- [Test Data and Environment Plan](./Testing/Test_Plans/SEMS_Test_Data_and_Environment_Plan.md)
- [Functional Test Case Catalog](./Testing/Test_Cases/SEMS_Functional_Test_Case_Catalog.md)
- [High-Risk Test Cases](./Testing/Test_Cases/SEMS_High_Risk_Test_Cases.md)
- [Import Test Cases](./Testing/Test_Cases/SEMS_Import_Test_Cases.md)
- [Regression Checklist](./Testing/Test_Cases/SEMS_Regression_Checklist.md)
- [Scoring, State, and Report Test Cases](./Testing/Test_Cases/SEMS_Scoring_State_Report_Test_Cases.md)
- [Security, RBAC, and SSO Test Cases](./Testing/Test_Cases/SEMS_Security_RBAC_SSO_Test_Cases.md)
- [Scoring Reference Cases](./Testing/Test_Data/SEMS_Scoring_Reference_Cases.md)

`Testing/UAT/` ยังไม่มีเอกสาร

### Deployment

- [Deployment Overview](./Deployment/README.md)

`Deployment/Guides/` และ `Deployment/User_Manuals/` ยังไม่มีเอกสาร

## เปิด Repository เป็น Obsidian Vault

1. Clone หรือดาวน์โหลด repository ลงเครื่อง
2. เปิด Obsidian แล้วเลือก **Open folder as vault**
3. เลือกโฟลเดอร์ราก `SEMS_Docs/`
4. เปิด `START_HERE.md` แล้วใช้ **Pin tab** หรือเพิ่ม **Bookmark** เพื่อกำหนดเป็นหน้าหลักของ vault

ลิงก์ทั้งหมดเป็น relative Markdown links จึงใช้ได้โดยไม่ต้องแปลงเป็น Obsidian wikilinks ส่วน `.obsidian/` ถูก ignore ไว้ใน [.gitignore](./.gitignore) เพื่อไม่ commit การตั้งค่าส่วนบุคคล

## เมื่อเพิ่มเอกสารใหม่

1. วางไฟล์ในหมวดที่ตรงกับเนื้อหา และใช้ชื่อไฟล์กับ capitalization ให้คงที่
2. เพิ่ม metadata และ revision history ตาม [Documentation Policy](./DOCUMENTATION_POLICY.md)
3. เพิ่ม relative Markdown link ใน `README.md` ของหมวดนั้น
4. เพิ่มไฟล์ใน Complete File Index ของ `START_HERE.md`
5. อัปเดต directory tree และ versioned file index ใน [REPOSITORY_TREE.md](./REPOSITORY_TREE.md)
6. เพิ่ม revision history และเพิ่ม version เฉพาะไฟล์ดัชนีที่แก้ไข
7. ตรวจว่าลิงก์ทุกเส้นทางตรงกับชื่อไฟล์จริงและเปิดได้ทั้ง GitHub และ Obsidian
8. อย่า commit `.obsidian/`, `.trash/` หรือ personal workspace settings

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.3 | 2026-07-24 | SEMS Documentation Team | Reclassified the stakeholder responses as confirmed, pending a formal record, and updated the reading index. |
| v1.2 | 2026-07-24 | SEMS Documentation Team | Added stakeholder questions and the clearly labeled advisor-answer simulation to the reading index. |
| v1.1 | 2026-07-23 | SEMS Documentation Team | Added review report, PRD, traceability, architecture, error catalog, approval/meeting templates and scoring reference data. |
| v1.0 | 2026-07-23 | SEMS Documentation Team | Created the main onboarding guide, role-based reading paths, complete file index, and Obsidian instructions. |
