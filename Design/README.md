# 🎨 Design

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.6** |
| Last Updated | **2026-07-23** |
| Author | **SEMS Documentation Team** |
| Scope | Architecture, APIs, database, scoring criteria, data templates, and UI/UX |

เอกสารการออกแบบเชิงเทคนิค เกณฑ์การประเมิน และรูปแบบข้อมูลของระบบ SEMS

## Directory Index

- **API/** — API and authentication specifications
- **Architecture/** — System architecture and diagrams
- **Criteria/** — Evaluation and scoring criteria
- **Data_Templates/** — Data import/export templates
- **Database/** — Database schemas and ER diagrams
- **UI_UX/** — Wireframes, mockups, and interface designs

## Document Register

| Document | Version | Last Updated | Status |
| :--- | :---: | :---: | :--- |
| [`API/kku-oauth-summary.md`](./API/kku-oauth-summary.md) | v1.0 | 2026-07-23 | Current |
| [`API/SEMS_API_Specification.md`](./API/SEMS_API_Specification.md) | v1.1 | 2026-07-23 | Draft |
| [`API/openapi.yaml`](./API/openapi.yaml) | v1.0 | 2026-07-23 | Draft |
| [`API/endpoint-matrix.csv`](./API/endpoint-matrix.csv) | v1.0 | 2026-07-23 | Draft |
| [`Architecture/SEMS_Permission_Matrix.md`](./Architecture/SEMS_Permission_Matrix.md) | v1.0 | 2026-07-23 | Draft |
| [`Architecture/SEMS_Process_Flows.md`](./Architecture/SEMS_Process_Flows.md) | v1.0 | 2026-07-23 | Draft |
| [`Architecture/SEMS_State_Transition_Specification.md`](./Architecture/SEMS_State_Transition_Specification.md) | v0.1 | 2026-07-23 | Draft |
| [`Criteria/Criteria.xlsx`](./Criteria/Criteria.xlsx) | v1.0 | 2026-07-20 | Current |
| [`Criteria/Criteria_Converted.md`](./Criteria/Criteria_Converted.md) | v1.0 | 2026-07-23 | Draft |
| [`Criteria/SEMS_Criteria_Config.json`](./Criteria/SEMS_Criteria_Config.json) | v1.0 | 2026-07-23 | Draft |
| [`Criteria/SEMS_Scoring_Rule_Specification.md`](./Criteria/SEMS_Scoring_Rule_Specification.md) | v1.0 | 2026-07-23 | Draft |
| [`Data_Templates/Data_import_to_web.xlsx`](./Data_Templates/Data_import_to_web.xlsx) | v1.0 | 2026-07-22 | Current |
| [`Data_Templates/Data_import_to_web_Specification.md`](./Data_Templates/Data_import_to_web_Specification.md) | v1.0 | 2026-07-23 | Reference — Converted from Workbook |
| [`Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md`](./Data_Templates/SEMS_Applicant_Import_Mapping_Specification.md) | v0.1 | 2026-07-23 | Draft |
| [`Data_Templates/SEMS_Applicant_Import_Mapping_Specification.xlsx`](./Data_Templates/SEMS_Applicant_Import_Mapping_Specification.xlsx) | v0.1 | 2026-07-23 | Draft |
| [`Data_Templates/SEMS_Data_Dictionary_Import_Mapping.xlsx`](./Data_Templates/SEMS_Data_Dictionary_Import_Mapping.xlsx) | v0.1 | 2026-07-23 | Draft — Pre-Baseline |
| [`Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md`](./Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md) | v0.2 | 2026-07-23 | Draft — Pre-Baseline |
| [`Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md`](./Data_Templates/SEMS_Data_Dictionary_Import_Mapping/README.md) | v1.0 | 2026-07-23 | Reference — Converted from Workbook |
| [`Database/SEMS_Data_Dictionary.xlsx`](./Database/SEMS_Data_Dictionary.xlsx) | v1.0 | 2026-07-23 | Draft — Pending Validation |
| [`Database/SEMS_Data_Dictionary/README.md`](./Database/SEMS_Data_Dictionary/README.md) | v1.0 | 2026-07-23 | Reference — Converted from Workbook |
| [`Database/SEMS_ER_Diagram.png`](./Database/SEMS_ER_Diagram.png) | v1.0 | 2026-07-23 | Draft |
| [`Database/SEMS_ER_Prisma_Data_Dictionary.md`](./Database/SEMS_ER_Prisma_Data_Dictionary.md) | v1.1 | 2026-07-23 | Draft |
| [`UI_UX/README.md`](./UI_UX/README.md) | v1.2 | 2026-07-23 | Current Index |

## Revision History

| Version | Date | Author | Document / Change |
| :--- | :---: | :--- | :--- |
| v1.6 | 2026-07-23 | SEMS Documentation Team | Rebuilt the wireframe overview with readable English captions. |
| v1.5 | 2026-07-23 | SEMS Documentation Team | Added GitHub-readable spreadsheet conversions and embedded ER/wireframe images and API reference links. |
| v1.4 | 2026-07-23 | SEMS Documentation Team | Added API, architecture, scoring, database, import-mapping, and UI/UX design packages. |
| v1.3 | 2026-07-23 | SEMS Documentation Team | Added `Database/SEMS_Data_Dictionary.xlsx` (document v1.0, Draft). |
| v1.2 | 2026-07-23 | SEMS Documentation Team | Added the Data Dictionary/Import Mapping workbook and guide (v0.1 Draft). |
| v1.1 | 2026-07-23 | SEMS Documentation Team | Moved and indexed `API/kku-oauth-summary.md` (document v1.0); added version metadata for all Design documents. |
| v1.0 | 2026-07-22 | SEMS Documentation Team | Added `Criteria/Criteria.xlsx` and `Data_Templates/Data_import_to_web.xlsx` (document v1.0). |
