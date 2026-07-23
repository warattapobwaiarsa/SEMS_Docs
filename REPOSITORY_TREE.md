# SEMS Repository Tree

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.11** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Scope | Versioned documentation and standard SEMS directories |

## Directory Tree

```text
SEMS_Docs/
├── 📋 Requirements/
│   ├── Meeting_Notes/
│   ├── Proposal/
│   │   ├── SEMS-project-proposal.md [v1.0]
│   │   └── SEMS-project-proposal.pdf [v1.0]
│   ├── SRS/
│   │   └── SEMS-SRS.md [v2.0 Draft]
│   ├── User_Stories/
│   │   ├── README.md [v1.0]
│   │   └── SEMS_User_Stories_and_Acceptance_Criteria.md [v0.1 Draft]
│   ├── README.md [v1.5]
│   ├── SEMS_Requirement_Decision_Analysis.md [v1.1 Draft]
│   └── SEMS_Requirement_Decision_Register.md [v1.0 Draft]
├── 🎨 Design/
│   ├── API/
│   │   ├── endpoint-matrix.csv [v1.0 Draft]
│   │   ├── kku-oauth-summary.md [v1.0]
│   │   ├── openapi.yaml [v1.0 Draft]
│   │   └── SEMS_API_Specification.md [v1.1 Draft]
│   ├── Architecture/
│   │   ├── SEMS_Permission_Matrix.md [v1.0 Draft]
│   │   ├── SEMS_Process_Flows.md [v1.0 Draft]
│   │   └── SEMS_State_Transition_Specification.md [v0.1 Draft]
│   ├── Criteria/
│   │   ├── Criteria.xlsx [v1.0]
│   │   ├── Criteria_Converted.md [v1.0 Draft]
│   │   ├── SEMS_Criteria_Config.json [v1.0 Draft]
│   │   └── SEMS_Scoring_Rule_Specification.md [v1.0 Draft]
│   ├── Database/
│   │   ├── SEMS_Data_Dictionary/
│   │   │   ├── 00_Workbook_Overview.md [v1.0]
│   │   │   ├── 01_Data_Dictionary.md [v1.0]
│   │   │   ├── 02_Import_Column_Mapping.md [v1.0]
│   │   │   ├── 03_Value_Sets.md [v1.0]
│   │   │   ├── 04_Design_Decisions.md [v1.0]
│   │   │   └── README.md [v1.0]
│   │   ├── SEMS_Data_Dictionary.xlsx [v1.0 Draft]
│   │   ├── SEMS_ER_Diagram.png [v1.0 Draft]
│   │   └── SEMS_ER_Prisma_Data_Dictionary.md [v1.1 Draft]
│   ├── Data_Templates/
│   │   ├── Data_import_to_web.xlsx [v1.0]
│   │   ├── Data_import_to_web_Specification.md [v1.0]
│   │   ├── SEMS_Applicant_Import_Mapping_Specification.md [v0.1 Draft]
│   │   ├── SEMS_Applicant_Import_Mapping_Specification.xlsx [v0.1 Draft]
│   │   ├── SEMS_Data_Dictionary_Import_Mapping/
│   │   │   ├── 00_README.md [v1.0]
│   │   │   ├── 01_ENTITY_MODEL.md [v1.0]
│   │   │   ├── 02_DATA_DICTIONARY.md [v1.0]
│   │   │   ├── 03_IMPORT_MAPPING.md [v1.0]
│   │   │   ├── 04_VALIDATION_RULES.md [v1.0]
│   │   │   ├── 05_REFERENCE_VALUES.md [v1.0]
│   │   │   ├── 06_OPEN_DECISIONS.md [v1.0]
│   │   │   └── README.md [v1.0]
│   │   ├── SEMS_Data_Dictionary_Import_Mapping.xlsx [v0.1 Draft]
│   │   └── SEMS_Data_Dictionary_Import_Mapping_Guide.md [v0.2 Draft]
│   ├── UI_UX/
│   │   ├── screens/
│   │   │   ├── 01-login.png [v1.0 Draft]
│   │   │   ├── 02-dashboard.png [v1.0 Draft]
│   │   │   ├── 03-rounds.png [v1.0 Draft]
│   │   │   ├── 04-upload.png [v1.0 Draft]
│   │   │   ├── 05-mapping.png [v1.0 Draft]
│   │   │   ├── 06-preview.png [v1.0 Draft]
│   │   │   ├── 07-errors.png [v1.0 Draft]
│   │   │   ├── 08-applicants.png [v1.0 Draft]
│   │   │   ├── 09-applicant-detail.png [v1.0 Draft]
│   │   │   ├── 10-criteria.png [v1.0 Draft]
│   │   │   ├── 11-select-applicant.png [v1.0 Draft]
│   │   │   ├── 12-evaluation.png [v1.0 Draft]
│   │   │   ├── 13-review.png [v1.0 Draft]
│   │   │   ├── 14-summary.png [v1.0 Draft]
│   │   │   └── 15-export.png [v1.0 Draft]
│   │   ├── README.md [v1.2]
│   │   ├── screen_manifest.json [v1.0 Draft]
│   │   ├── SEMS_Wireframe_Overview.png [v1.1 Draft]
│   │   ├── SEMS_Wireframe_Prototype.html [v1.0 Draft]
│   │   ├── SEMS_Wireframe_Specification.md [v1.1 Draft]
│   │   └── Wireframe_UAT_Checklist.md [v1.0 Draft]
│   └── README.md [v1.6]
├── 🧪 Testing/
│   ├── Test_Cases/
│   │   ├── SEMS_Functional_Test_Case_Catalog.md [v0.1 Draft]
│   │   ├── SEMS_High_Risk_Test_Cases.md [v0.1 Draft]
│   │   ├── SEMS_Import_Test_Cases.md [v0.1 Draft]
│   │   ├── SEMS_Regression_Checklist.md [v0.1 Draft]
│   │   ├── SEMS_Scoring_State_Report_Test_Cases.md [v0.1 Draft]
│   │   └── SEMS_Security_RBAC_SSO_Test_Cases.md [v0.1 Draft]
│   ├── Test_Plans/
│   │   ├── SEMS_Master_Test_Plan.md [v0.1 Draft]
│   │   ├── SEMS_Risk_and_Coverage_Matrix.md [v0.1 Draft]
│   │   └── SEMS_Test_Data_and_Environment_Plan.md [v0.1 Draft]
│   ├── UAT/
│   └── README.md [v1.2]
├── 🚀 Deployment/
│   ├── Guides/
│   ├── User_Manuals/
│   └── README.md [v1.1]
├── .gitignore
├── CONTRIBUTING.md [v1.0]
├── DOCUMENTATION_POLICY.md [v1.1]
├── README.md [v1.11]
├── REPOSITORY_TREE.md [v1.11]
└── START_HERE.md [v1.0 Current]
```

Ignored local workspace metadata (`.git/`, `.obsidian/`, and `.tmp-sheet-inspect/`), internal agent state (`.agents/`), and unversioned conversion artifacts (`tmp/`) are intentionally excluded.

## Versioned File Index

| Category | Index / Key Document | Version | Last Updated |
| :--- | :--- | :---: | :---: |
| Repository | [`README.md`](./README.md) | v1.11 | 2026-07-23 |
| Repository | [`START_HERE.md`](./START_HERE.md) | v1.0 (Current) | 2026-07-23 |
| Repository | [`REPOSITORY_TREE.md`](./REPOSITORY_TREE.md) | v1.11 | 2026-07-23 |
| Repository | [`CONTRIBUTING.md`](./CONTRIBUTING.md) | v1.0 | 2026-07-23 |
| Repository | [`DOCUMENTATION_POLICY.md`](./DOCUMENTATION_POLICY.md) | v1.1 | 2026-07-23 |
| Requirements | [`Requirements/README.md`](./Requirements/README.md) | v1.6 | 2026-07-23 |
| Requirements | [`Requirements/Proposal/SEMS-project-proposal.md`](./Requirements/Proposal/SEMS-project-proposal.md) | v1.0 | 2026-07-23 |
| Requirements | [`Requirements/SRS/SEMS-SRS.md`](./Requirements/SRS/SEMS-SRS.md) | v2.0 (Draft) | 2026-07-23 |
| Requirements | [`Requirements/User_Stories/README.md`](./Requirements/User_Stories/README.md) | v1.0 | 2026-07-23 |
| Design | [`Design/README.md`](./Design/README.md) | v1.6 | 2026-07-23 |
| Design | [`Design/API/openapi.yaml`](./Design/API/openapi.yaml) | v1.0 (Draft) | 2026-07-23 |
| Design | [`Design/Database/SEMS_Data_Dictionary/README.md`](./Design/Database/SEMS_Data_Dictionary/README.md) | v1.0 | 2026-07-23 |
| Design | [`Design/Database/SEMS_ER_Prisma_Data_Dictionary.md`](./Design/Database/SEMS_ER_Prisma_Data_Dictionary.md) | v1.1 (Draft) | 2026-07-23 |
| Design | [`Design/Data_Templates/Data_import_to_web_Specification.md`](./Design/Data_Templates/Data_import_to_web_Specification.md) | v1.0 | 2026-07-23 |
| Design | [`Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md`](./Design/Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md) | v1.0 | 2026-07-23 |
| Design | [`Design/UI_UX/README.md`](./Design/UI_UX/README.md) | v1.2 | 2026-07-23 |
| Testing | [`Testing/README.md`](./Testing/README.md) | v1.2 | 2026-07-23 |
| Deployment | [`Deployment/README.md`](./Deployment/README.md) | v1.1 | 2026-07-23 |

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.11 | 2026-07-23 | SEMS Documentation Team | Added `START_HERE.md`, synchronized changed index versions, and recorded the main GitHub/Obsidian entry point. |
| v1.10 | 2026-07-23 | SEMS Documentation Team | Rebuilt the wireframe overview with readable English captions and synchronized index versions. |
| v1.9 | 2026-07-23 | SEMS Documentation Team | Added GitHub-readable PDF and spreadsheet conversions and synchronized image/reference links and indexes. |
| v1.8 | 2026-07-23 | SEMS Documentation Team | Reorganized Requirements, Design, UI/UX, and Testing deliverables; removed two duplicate Testing package copies; synchronized all current paths and version tags. |
| v1.7 | 2026-07-23 | SEMS Documentation Team | Added `Design/Database/SEMS_Data_Dictionary.xlsx` v1.0 (Draft). |
| v1.6 | 2026-07-23 | SEMS Documentation Team | Added the Data Dictionary/Import Mapping workbook and guide v0.1 (Draft). |
| v1.5 | 2026-07-23 | SEMS Documentation Team | Added the Requirement Decision Analysis v1.1 (Draft). |
| v1.4 | 2026-07-23 | SEMS Documentation Team | Added the Requirement Decision Register v1.0 (Draft). |
| v1.3 | 2026-07-23 | SEMS Documentation Team | Added `CONTRIBUTING.md` and updated documentation governance. |
| v1.2 | 2026-07-23 | SEMS Documentation Team | Added `DOCUMENTATION_POLICY.md`. |
| v1.1 | 2026-07-23 | SEMS Documentation Team | Added file version tags and synchronized repository paths. |
| v1.0 | 2026-07-22 | SEMS Documentation Team | Established the official Requirements, Design, Testing, and Deployment hierarchy. |
