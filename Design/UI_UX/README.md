# Design/UI_UX

| Metadata | Value |
| :--- | :--- |
| Current Version | **v1.13** |
| Last Updated | **2026-08-05** |
| Author | **SEMS Documentation Team** |
| Scope | Clickable prototype, stakeholder review and formative evaluation |

[START HERE](../../START_HERE.md) › [🎨 Design](../README.md) › Design/UI_UX

## Document Register

| File | Version | Status |
| :--- | :---: | :--- |
| [`SEMS_Wireframe_Specification.md`](./SEMS_Wireframe_Specification.md) | v0.11 | Draft — Phase 3.6 Authentication Invariant |
| [`Wireframe_UAT_Checklist.md`](./Wireframe_UAT_Checklist.md) | v0.9 | Draft — Phase 3.6 Regression Checklist |
| [`SEMS_Wireframe_Prototype.html`](./SEMS_Wireframe_Prototype.html) | v1.4 | Phase 3.6 — Authentication Hotfix; browser verification pending |
| [`SEMS_Wireframe_Overview.png`](./SEMS_Wireframe_Overview.png) | v1.1 | Draft — English Captions |
| [`screen_manifest.json`](./screen_manifest.json) | v1.4 | Phase 3.5 Screen-level Static Mapping |
| [`screens/`](./screens/) | v1.0 | 15 existing previews; WF-16 deferred to Phase 6 |

## Usage

1. เปิด `SEMS_Wireframe_Prototype.html`
2. ทำ Stakeholder Review, Prototype Evaluation หรือ Usability Walkthrough ด้วย `Wireframe_UAT_Checklist.md`
3. บันทึกข้อเสนอแนะก่อนเริ่มพัฒนา Frontend

> กิจกรรมนี้เป็น Formative Evaluation ไม่ใช่ Formal UAT และ Prototype ใช้ข้อมูลสังเคราะห์โดยไม่เชื่อม Production API, KKU OAuth/OIDC จริง หรือบริการภายนอก

`prototype_status` ใน Screen Manifest เป็นสถานะระดับหน้าจอหรือ interaction เท่านั้น ไม่ใช่ Formal Requirement Approval; ให้ยึด Coverage Matrix 27 รายการใน Wireframe Specification สำหรับสถานะ Feature โดย Item 3–6 มี Static Evidence หลัง Phase 3.5 แต่ยังเป็น `partial` จนผ่าน Browser walkthrough ส่วน Item 10–11 ยังคง Must-have Gap และ Export ถูก disable จน Phase 4 ฟิลด์ `coverage_scope`, `feature_coverage` และ `coverage_note` เป็น additive metadata; consumer เดิมที่อ่าน `id`/`image` ยังคงใช้โครงสร้าง JSON array เดิม

## ลำดับการอ่านที่แนะนำ

1. [Wireframe Specification](./SEMS_Wireframe_Specification.md)
2. เปิด [Interactive Prototype](./SEMS_Wireframe_Prototype.html) และเทียบกับ screen previews
3. บันทึกผลจริงใน [Wireframe UAT Checklist](./Wireframe_UAT_Checklist.md)
4. เมื่อมีหลักฐานครบ ให้อัปเดต [System Design Approval Record](../../Requirements/Approvals/System_Design_Approval_Record.md)

## Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v1.13 | 2026-08-05 | SEMS Documentation Team | Recorded the Phase 3.6 shared authentication invariant, direct-handler guards, eight-scenario catalogue and accessibility fix; Item 3–6 remain partial and Item 10–11 remain disabled. |
| v1.12 | 2026-08-05 | SEMS Documentation Team | Recorded Phase 3.5 import guard, Application-owned documents, Criteria edit buffer, isolated scenarios, disabled Item 11 export, readiness traceability and partial static coverage pending browser verification. |
| v1.11 | 2026-08-05 | SEMS Documentation Team | Recorded Phase 3 Item 3–6 ADMIN preparation workflows, integrated Demo State/scenarios, updated screen-level manifest evidence and retained Items 10–11 as gaps. |
| v1.10 | 2026-08-05 | SEMS Documentation Team | Recorded Phase 2.5 role/session stabilization, semantic form/button cleanup, disabled Phase 3 placeholders and additive screen-level manifest coverage metadata. |
| v1.9 | 2026-08-05 | SEMS Documentation Team | Updated the UI/UX package for the approved Phase 1–2 scope baseline, formative-evaluation terminology, 16-screen manifest and deferred Phase 6 screenshots. |
| v1.8 | 2026-07-24 | SEMS Documentation Team | เพิ่มและปรับ document navigation |
| v1.7 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v1.6 | 2026-07-24 | SEMS Documentation Team | Synchronized wireframe status/version and indexed explicit screen-manifest image paths. |
| v1.5 | 2026-07-24 | SEMS Documentation Team | Synchronized confirmed Release 1 UI behavior and UAT scenarios. |
| v1.4 | 2026-07-24 | SEMS Documentation Team | Added interactive Admin and Evaluator UAT flows, explicit prototype feedback, and automated interaction checks. |
| v1.3 | 2026-07-23 | SEMS Documentation Team | Aligned wireframe import file types and updated the UAT checklist for automated documentation checks. |
| v1.2 | 2026-07-23 | SEMS Documentation Team | Rebuilt the overview image with readable English captions for all 15 screens. |
| v1.1 | 2026-07-23 | SEMS Documentation Team | Embedded the overview and 15 screen previews in the wireframe specification. |
| v1.0 | 2026-07-23 | SEMS Documentation Team | Added the 15-screen wireframe prototype, specification, previews, and UAT checklist. |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — Data Dictionary และ Import Column Mapping](../Data_Templates/SEMS_Data_Dictionary_Import_Mapping_Guide.md)<br>
↑ หมวดเอกสาร: [🎨 Design](../README.md)<br>
⌂ หน้าหลัก: [START HERE](../../START_HERE.md)<br>
→ อ่านต่อ: [SEMS Wireframe Specification](./SEMS_Wireframe_Specification.md)

<!-- DOC_NAV_END -->
