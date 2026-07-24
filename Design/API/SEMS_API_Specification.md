# SEMS API Specification

| Metadata | Value |
| :--- | :--- |
| Version | **v1.3** |
| Last Updated | **2026-07-24** |
| Author | **SEMS Design Team** |
| Status | **Draft — System Design Review** |
| Base URL | `/api/v1` |
| Format | REST + JSON, UUID, RFC 3339, Session Cookie, CSRF |

## 1. หลักการออกแบบ

- Authentication ใช้ KKU OAuth 2.1 / OpenID Connect แบบ Authorization Code + PKCE (S256); SEMS ไม่รับหรือจัดเก็บรหัสผ่าน KKU
- Authorization ใช้ RBAC (`ADMIN`, `EVALUATOR`) ร่วมกับ Object-level authorization โดย Evaluator เข้าถึงรายละเอียดผู้สมัคร เอกสาร และ Evaluation ได้เฉพาะรายการที่ตนเลือกและเป็นเจ้าของ
- ผู้สมัครหนึ่งรายต่อรอบมี Evaluation ที่ใช้งานอยู่ได้สูงสุด 3 รายการ และผู้ประเมินคนเดิมมีได้ไม่เกินหนึ่งรายการ
- คะแนนรวมรายผู้ประเมินเป็นผลรวม Embedded Point ของเกณฑ์ที่มีผลต่อคะแนนทั้ง 10 ข้อ; `weight_percent` เป็น metadata และห้ามคูณซ้ำ
- Result Summary เป็นค่าเฉลี่ยเลขคณิตของคะแนนรวมจาก Evaluation สถานะ `SUBMITTED` ของผู้ประเมินไม่ซ้ำกัน 2–3 คน; เมื่อคนที่ 3 Submit ต้องคำนวณใหม่อัตโนมัติ
- Response error ใช้ `{ code, message, details, traceId, timestamp }` และทุก operation ระบุ Error Code กับ Audit Event

## 2. Endpoint Specification

### Auth

#### `GET /auth/login` — เริ่มเข้าสู่ระบบด้วย KKU SSO

- **Role:** Public
- **Request:** Query: returnUrl (optional)
- **Response:** 302 Redirect
- **Validation:** returnUrl ต้องเป็น path ภายในระบบเท่านั้น
- **Error Code:** SSO_UNAVAILABLE, INVALID_RETURN_URL
- **Audit Event:** AUTH_LOGIN_STARTED

#### `GET /auth/callback` — รับ Callback จาก KKU SSO

- **Role:** Public
- **Request:** Query: code + state จาก KKU
- **Response:** 302 Redirect พร้อม Session cookie
- **Validation:** ตรวจ state และ nonce; แลก authorization code ด้วย PKCE verifier; ตรวจลายเซ็น/issuer/audience/expiry ของ id_token; ใช้ KKU sub เป็นตัวระบุถาวร
- **Error Code:** AUTH_CALLBACK_INVALID, STATE_MISMATCH, NONCE_MISMATCH, TOKEN_VALIDATION_FAILED, USER_NOT_PROVISIONED, USER_INACTIVE, SSO_UNAVAILABLE
- **Audit Event:** AUTH_LOGIN_SUCCESS, AUTH_LOGIN_FAILURE

#### `GET /auth/me` — อ่านข้อมูลผู้ใช้ปัจจุบัน

- **Role:** ADMIN, EVALUATOR
- **Request:** Session cookie
- **Response:** User
- **Validation:** Session ต้องยังไม่หมดอายุและบัญชี SEMS ต้อง ACTIVE
- **Error Code:** AUTH_REQUIRED, USER_INACTIVE
- **Audit Event:** -

#### `POST /auth/logout` — ออกจากระบบ SEMS

- **Role:** ADMIN, EVALUATOR
- **Request:** Session + X-CSRF-Token
- **Response:** 204 No Content
- **Validation:** ยกเลิก Session ฝั่ง SEMS เสมอ; การออกจาก KKU SSO ทั้งหมดขึ้นกับ logout mode ที่กำหนด
- **Error Code:** AUTH_REQUIRED, CSRF_INVALID, SSO_LOGOUT_FAILED
- **Audit Event:** AUTH_LOGOUT

### Users

#### `GET /users` — ค้นหาและแสดงผู้ใช้งาน SEMS

- **Role:** ADMIN
- **Request:** Query filter + pagination
- **Response:** Paged<User>
- **Validation:** pageSize ไม่เกิน 100
- **Error Code:** AUTH_REQUIRED, FORBIDDEN
- **Audit Event:** -

#### `POST /users` — เชื่อมโยง KKU Account และสร้างบัญชี SEMS

- **Role:** ADMIN
- **Request:** CreateUserRequest
- **Response:** 201 User
- **Validation:** kkuSub และ email ต้องไม่ซ้ำ; ระบบไม่รับหรือจัดเก็บรหัสผ่าน KKU
- **Error Code:** VALIDATION_ERROR, DUPLICATE_KKU_SUB, DUPLICATE_EMAIL, CSRF_INVALID
- **Audit Event:** USER_CREATED

#### `GET /users/{userId}` — อ่านรายละเอียดผู้ใช้งาน

- **Role:** ADMIN
- **Request:** Path: userId
- **Response:** User
- **Validation:** -
- **Error Code:** USER_NOT_FOUND
- **Audit Event:** -

#### `PATCH /users/{userId}` — แก้ไขชื่อหรือบทบาทผู้ใช้งาน

- **Role:** ADMIN
- **Request:** UpdateUserRequest
- **Response:** User
- **Validation:** ห้ามลดสิทธิ์ผู้ดูแลระบบคนสุดท้าย; If-Match ต้องตรงเมื่อส่งมา
- **Error Code:** USER_NOT_FOUND, VALIDATION_ERROR, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** USER_UPDATED

#### `POST /users/{userId}/activate` — เปิดสิทธิ์ใช้งาน SEMS

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** User
- **Validation:** ห้ามปิดสิทธิ์ผู้ดูแลระบบ ACTIVE คนสุดท้าย
- **Error Code:** USER_NOT_FOUND, LAST_ACTIVE_ADMIN, CSRF_INVALID
- **Audit Event:** USER_ACTIVATED

#### `POST /users/{userId}/deactivate` — ปิดสิทธิ์ใช้งาน SEMS

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** User
- **Validation:** ห้ามปิดสิทธิ์ผู้ดูแลระบบ ACTIVE คนสุดท้าย
- **Error Code:** USER_NOT_FOUND, LAST_ACTIVE_ADMIN, CSRF_INVALID
- **Audit Event:** USER_DEACTIVATED

### Scholarship Rounds

#### `GET /scholarship-rounds` — แสดงรอบทุน

- **Role:** ADMIN, EVALUATOR
- **Request:** Query status + pagination
- **Response:** Paged<ScholarshipRound>
- **Validation:** Evaluator เห็นเฉพาะรอบที่เกี่ยวข้อง โดยค่าเริ่มต้นคือ OPEN
- **Error Code:** AUTH_REQUIRED
- **Audit Event:** -

#### `POST /scholarship-rounds` — สร้างรอบทุน

- **Role:** ADMIN
- **Request:** CreateRoundRequest
- **Response:** 201 ScholarshipRound
- **Validation:** startDate ต้องไม่เกิน endDate; code ต้องไม่ซ้ำ
- **Error Code:** VALIDATION_ERROR, DUPLICATE_ROUND_CODE, INVALID_DATE_RANGE, CSRF_INVALID
- **Audit Event:** ROUND_CREATED

#### `GET /scholarship-rounds/{roundId}` — อ่านรายละเอียดรอบทุน

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: roundId
- **Response:** ScholarshipRound
- **Validation:** -
- **Error Code:** ROUND_NOT_FOUND, ACCESS_DENIED
- **Audit Event:** -

#### `PATCH /scholarship-rounds/{roundId}` — แก้ไขรอบทุนสถานะ DRAFT

- **Role:** ADMIN
- **Request:** UpdateRoundRequest
- **Response:** ScholarshipRound
- **Validation:** แก้ไขข้อมูลหลักได้เมื่อ DRAFT; หากมี Evaluation แล้วห้ามเปลี่ยนข้อมูลที่กระทบผล
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, ROUND_HAS_EVALUATIONS, INVALID_DATE_RANGE, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** ROUND_UPDATED

#### `POST /scholarship-rounds/{roundId}/open` — เปิดรอบทุน

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** ScholarshipRound
- **Validation:** สถานะเดิมต้อง DRAFT; ต้องมี Criteria Set ACTIVE, ผ่าน Pre-open Validation และมี Application อย่างน้อย 1 ราย; ไม่มี Application เป็น Blocking Error `NO_APPLICANTS`
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, ACTIVE_CRITERIA_REQUIRED, NO_APPLICANTS, CSRF_INVALID
- **Audit Event:** ROUND_OPENED

#### `POST /scholarship-rounds/{roundId}/close` — ปิดรอบทุน

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** ScholarshipRound
- **Validation:** สถานะเดิมต้อง OPEN; ปิดการสร้าง/Submit Evaluation ใหม่; ผู้สมัคร Submitted >=2 เป็น FINALIZED; น้อยกว่า 2 เป็น CLOSED_INCOMPLETE
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, CSRF_INVALID
- **Audit Event:** ROUND_CLOSED

#### `POST /scholarship-rounds/{roundId}/archive` — จัดเก็บรอบทุน

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** ScholarshipRound
- **Validation:** สถานะเดิมต้อง CLOSED; ข้อมูลยังอ่านได้แต่แก้ไขไม่ได้
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, CSRF_INVALID
- **Audit Event:** ROUND_ARCHIVED

### Imports

#### `GET /imports` — แสดงประวัติการนำเข้า

- **Role:** ADMIN
- **Request:** Query filters
- **Response:** Paged<ImportBatch>
- **Validation:** -
- **Error Code:** FORBIDDEN
- **Audit Event:** -

#### `POST /imports` — อัปโหลดไฟล์ผู้สมัคร

- **Role:** ADMIN
- **Request:** multipart: roundId + file
- **Response:** 201 ImportBatch
- **Validation:** Release 1 รองรับ CSV/XLSX เท่านั้น; XLS เป็น Optional / Out of Scope; รอบทุนต้อง DRAFT หรือ OPEN ตามนโยบาย; ขนาดไฟล์ใช้ configuration
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, UNSUPPORTED_FILE_TYPE, IMPORT_FILE_EMPTY, IMPORT_FILE_TOO_LARGE, CSRF_INVALID
- **Audit Event:** IMPORT_UPLOADED

#### `GET /imports/{importId}` — อ่านสถานะ Import Batch

- **Role:** ADMIN
- **Request:** Path: importId
- **Response:** ImportBatch
- **Validation:** -
- **Error Code:** IMPORT_NOT_FOUND
- **Audit Event:** -

#### `PUT /imports/{importId}/mapping` — บันทึก Column Mapping

- **Role:** ADMIN
- **Request:** ImportMappingRequest
- **Response:** ImportBatch
- **Validation:** ทุกฟิลด์บังคับต้องมี Mapping; หนึ่ง targetField รับได้ไม่เกินหนึ่ง sourceColumn เว้นแต่ระบุ multi-row transform
- **Error Code:** IMPORT_NOT_FOUND, IMPORT_STATE_INVALID, IMPORT_MAPPING_INCOMPLETE, DUPLICATE_TARGET_FIELD, UNKNOWN_TARGET_FIELD, CSRF_INVALID
- **Audit Event:** IMPORT_MAPPING_SAVED

#### `POST /imports/{importId}/validate` — ตรวจสอบและแปลงข้อมูลนำเข้า

- **Role:** ADMIN
- **Request:** ImportValidationRequest (optional)
- **Response:** Batch + topErrors
- **Validation:** รหัสนักศึกษาใช้รูปแบบ ^\d{9}-\d$ (check digit เป็นกฎแยก); GPA 0.00-4.00; วันที่ไทยต้องแปลง พ.ศ. เป็น ค.ศ.; พิกัด latitude/longitude อยู่ในช่วงมาตรฐาน; รองรับข้อมูล กยศ./ทุนหลายแถวและตรวจ orphan continuation row
- **Error Code:** IMPORT_NOT_FOUND, IMPORT_STATE_INVALID, IMPORT_MAPPING_INCOMPLETE, REQUIRED_FIELD_MISSING, INVALID_STUDENT_ID, INVALID_GPA, INVALID_DATE, INVALID_PHONE, INVALID_EMAIL, INVALID_COORDINATE, DUPLICATE_STUDENT_IN_FILE, ORPHAN_CONTINUATION_ROW, CSRF_INVALID
- **Audit Event:** IMPORT_VALIDATED, IMPORT_VALIDATION_FAILED

#### `GET /imports/{importId}/preview` — ดูตัวอย่างข้อมูลหลังแปลง

- **Role:** ADMIN
- **Request:** Pagination + onlyIssues
- **Response:** Paged<ImportPreviewRow>
- **Validation:** -
- **Error Code:** IMPORT_NOT_FOUND, IMPORT_NOT_MAPPED
- **Audit Event:** -

#### `GET /imports/{importId}/errors` — ดาวน์โหลด/อ่านรายการข้อผิดพลาด

- **Role:** ADMIN
- **Request:** Pagination + severity
- **Response:** Paged<ImportError>
- **Validation:** -
- **Error Code:** IMPORT_NOT_FOUND
- **Audit Event:** -

#### `POST /imports/{importId}/confirm` — ยืนยันนำเข้าข้อมูลเข้าสู่รอบทุน

- **Role:** ADMIN
- **Request:** allowWarnings (optional)
- **Response:** ImportBatch CONFIRMED
- **Validation:** ต้องผ่าน Validation และไม่มี ERROR; ใช้ Database Transaction; Applicant ต่อรอบต้องไม่ซ้ำตาม studentId
- **Error Code:** IMPORT_NOT_FOUND, IMPORT_NOT_VALIDATED, IMPORT_HAS_BLOCKING_ERRORS, IMPORT_ALREADY_CONFIRMED, INVALID_ROUND_STATUS_TRANSITION, DUPLICATE_STUDENT_IN_ROUND, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** IMPORT_CONFIRMED

#### `POST /imports/{importId}/cancel` — ยกเลิก Import Batch ที่ยังไม่ Confirm

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** ImportBatch CANCELLED
- **Validation:** ยกเลิกได้ก่อน CONFIRMED เท่านั้น
- **Error Code:** IMPORT_NOT_FOUND, IMPORT_ALREADY_CONFIRMED, CSRF_INVALID
- **Audit Event:** IMPORT_CANCELLED

### Applicants

#### `GET /applicants` — ค้นหาและแสดงผู้สมัคร

- **Role:** ADMIN, EVALUATOR
- **Request:** roundId + search/filter
- **Response:** Paged<ApplicantSummary>
- **Validation:** Evaluator ค้นหาได้เฉพาะรอบ OPEN; Evaluator ได้เฉพาะข้อมูลขั้นต่ำสำหรับค้นหา/เลือกผู้สมัคร
- **Error Code:** ROUND_NOT_FOUND, ACCESS_DENIED
- **Audit Event:** APPLICANT_LIST_VIEWED

#### `GET /applicants/{applicantRoundId}` — อ่านรายละเอียดผู้สมัคร

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: applicantRoundId
- **Response:** ApplicantDetail (field-filtered)
- **Validation:** Evaluator ต้องมี Evaluation ที่ใช้งานอยู่ของตนสำหรับผู้สมัครนี้; ปกปิด field ที่ไม่จำเป็นตามบทบาท
- **Error Code:** APPLICANT_NOT_FOUND, APPLICANT_ACCESS_DENIED, ROUND_NOT_OPEN
- **Audit Event:** APPLICANT_DETAIL_VIEWED

#### `PATCH /applicants/{applicantRoundId}` — แก้ไขข้อมูลผู้สมัคร

- **Role:** ADMIN
- **Request:** UpdateApplicantRequest
- **Response:** ApplicantDetail
- **Validation:** ข้อมูลต้องผ่าน validation เดียวกับ Import; การแก้ไขหลัง Finalized ต้องเป็นไปตามนโยบายและมีเหตุผล
- **Error Code:** APPLICANT_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, VALIDATION_ERROR, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** APPLICANT_UPDATED

### Documents

#### `GET /applicants/{applicantRoundId}/documents` — แสดงเอกสารของผู้สมัคร

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: applicantRoundId
- **Response:** Document[]
- **Validation:** Evaluator ต้องเป็นเจ้าของ Evaluation ของผู้สมัคร
- **Error Code:** APPLICANT_NOT_FOUND, DOCUMENT_ACCESS_DENIED
- **Audit Event:** DOCUMENT_LIST_VIEWED

#### `POST /applicants/{applicantRoundId}/documents` — อัปโหลดเอกสารประกอบ

- **Role:** ADMIN
- **Request:** multipart file + metadata
- **Response:** 201 Document
- **Validation:** รองรับ PDF/JPG/PNG; ตรวจ MIME จริง ไม่เชื่อเฉพาะนามสกุล; ชื่อไฟล์ต้อง sanitize; ขนาดสูงสุดมาจาก configuration
- **Error Code:** APPLICANT_NOT_FOUND, DOCUMENT_TYPE_UNSUPPORTED, DOCUMENT_TOO_LARGE, FILE_STORAGE_ERROR, CSRF_INVALID
- **Audit Event:** DOCUMENT_UPLOADED

#### `GET /documents/{documentId}` — อ่าน metadata เอกสาร

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: documentId
- **Response:** Document
- **Validation:** -
- **Error Code:** DOCUMENT_NOT_FOUND, DOCUMENT_ACCESS_DENIED
- **Audit Event:** DOCUMENT_METADATA_VIEWED

#### `GET /documents/{documentId}/content` — เปิดดูหรือดาวน์โหลดเอกสาร

- **Role:** ADMIN, EVALUATOR
- **Request:** Path + disposition
- **Response:** Binary stream
- **Validation:** ตรวจสิทธิ์ทุกครั้งผ่าน Backend; ห้ามเปิดเผย storage path โดยตรง
- **Error Code:** DOCUMENT_NOT_FOUND, DOCUMENT_ACCESS_DENIED, FILE_STORAGE_ERROR
- **Audit Event:** DOCUMENT_OPENED, DOCUMENT_DOWNLOADED

#### `DELETE /documents/{documentId}` — ลบเอกสารประกอบ

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** 204 No Content
- **Validation:** ต้องลบ metadata และไฟล์ตาม transaction/outbox policy; อาจใช้ soft delete เพื่อ auditability
- **Error Code:** DOCUMENT_NOT_FOUND, DOCUMENT_IN_USE, FILE_STORAGE_ERROR, CSRF_INVALID
- **Audit Event:** DOCUMENT_DELETED

### Criteria Sets

#### `GET /criteria-sets` — แสดงชุดเกณฑ์

- **Role:** ADMIN
- **Request:** Query filters
- **Response:** Paged<CriteriaSet>
- **Validation:** -
- **Error Code:** FORBIDDEN
- **Audit Event:** -

#### `POST /criteria-sets` — สร้างชุดเกณฑ์และรายการเกณฑ์

- **Role:** ADMIN
- **Request:** CreateCriteriaSetRequest
- **Response:** 201 CriteriaSet
- **Validation:** minScore <= maxScore; code และ displayOrder ไม่ซ้ำในชุด; น้ำหนัก/คะแนนเต็มต้องเป็นไปตาม Scoring Rule ที่อนุมัติ
- **Error Code:** ROUND_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, DUPLICATE_CRITERION_CODE, INVALID_SCORE_RANGE, INVALID_WEIGHT, VALIDATION_ERROR, CSRF_INVALID
- **Audit Event:** CRITERIA_SET_CREATED

#### `GET /criteria-sets/{criteriaSetId}` — อ่านรายละเอียดชุดเกณฑ์

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: criteriaSetId
- **Response:** CriteriaSet
- **Validation:** Evaluator อ่านได้เฉพาะชุด ACTIVE ของรอบที่ตนกำลังประเมิน
- **Error Code:** CRITERIA_SET_NOT_FOUND, ACCESS_DENIED
- **Audit Event:** -

#### `PATCH /criteria-sets/{criteriaSetId}` — แก้ไขข้อมูลชุดเกณฑ์ DRAFT

- **Role:** ADMIN
- **Request:** UpdateCriteriaSetRequest
- **Response:** CriteriaSet
- **Validation:** แก้ไขได้เมื่อยังไม่มี Evaluation อ้างอิง; การเปลี่ยนกฎคะแนนที่กระทบผลต้องสร้าง version ใหม่
- **Error Code:** CRITERIA_SET_NOT_FOUND, CRITERIA_LOCKED, CONCURRENCY_CONFLICT, VALIDATION_ERROR, CSRF_INVALID
- **Audit Event:** CRITERIA_SET_UPDATED

#### `POST /criteria-sets/{criteriaSetId}/criteria` — เพิ่มเกณฑ์ในชุด DRAFT

- **Role:** ADMIN
- **Request:** CriterionInput
- **Response:** 201 Criterion
- **Validation:** ชุดต้อง DRAFT; code/displayOrder ไม่ซ้ำ; minScore <= maxScore
- **Error Code:** CRITERIA_SET_NOT_FOUND, CRITERIA_LOCKED, DUPLICATE_CRITERION_CODE, INVALID_SCORE_RANGE, INVALID_WEIGHT, CSRF_INVALID
- **Audit Event:** CRITERION_ADDED

#### `PATCH /criteria-sets/{criteriaSetId}/criteria/{criterionId}` — แก้ไขเกณฑ์ในชุด DRAFT

- **Role:** ADMIN
- **Request:** CriterionInput
- **Response:** Criterion
- **Validation:** ชุดต้อง DRAFT และยังไม่ถูกใช้งาน
- **Error Code:** CRITERIA_SET_NOT_FOUND, CRITERION_NOT_FOUND, CRITERIA_LOCKED, DUPLICATE_CRITERION_CODE, INVALID_SCORE_RANGE, INVALID_WEIGHT, CSRF_INVALID
- **Audit Event:** CRITERION_UPDATED

#### `DELETE /criteria-sets/{criteriaSetId}/criteria/{criterionId}` — ลบเกณฑ์จากชุด DRAFT

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** 204 No Content
- **Validation:** ต้องเหลือเกณฑ์อย่างน้อย 1 รายการ
- **Error Code:** CRITERIA_SET_NOT_FOUND, CRITERION_NOT_FOUND, CRITERIA_LOCKED, CRITERIA_MINIMUM_REQUIRED, CSRF_INVALID
- **Audit Event:** CRITERION_DELETED

#### `POST /criteria-sets/{criteriaSetId}/activate` — ตรวจสอบและเปิดใช้ชุดเกณฑ์

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** CriteriaSet ACTIVE
- **Validation:** เกณฑ์ครบถ้วน; คะแนน/น้ำหนักรวมตรงกฎที่อนุมัติ; หนึ่งรอบมีชุด ACTIVE ได้หนึ่งชุด
- **Error Code:** CRITERIA_SET_NOT_FOUND, CRITERIA_STATE_INVALID, CRITERIA_INVALID, DUPLICATE_ACTIVE_CRITERIA_SET, CSRF_INVALID
- **Audit Event:** CRITERIA_SET_ACTIVATED

#### `POST /criteria-sets/{criteriaSetId}/versions` — สร้างเวอร์ชันใหม่จากชุดเกณฑ์เดิม

- **Role:** ADMIN
- **Request:** reason + copyCriteria
- **Response:** 201 CriteriaSet new version
- **Validation:** reason บังคับ; Evaluation เดิมต้องยังอ้างอิง version เดิมเสมอ
- **Error Code:** CRITERIA_SET_NOT_FOUND, INVALID_ROUND_STATUS_TRANSITION, VERSION_ALREADY_EXISTS, CSRF_INVALID
- **Audit Event:** CRITERIA_VERSION_CREATED

### Evaluations

#### `GET /evaluations` — แสดงรายการประเมิน

- **Role:** ADMIN, EVALUATOR
- **Request:** Query filters
- **Response:** Paged<Evaluation>
- **Validation:** Evaluator ถูกบังคับ mine=true และเห็นเฉพาะของตน
- **Error Code:** ACCESS_DENIED
- **Audit Event:** -

#### `POST /evaluations` — เลือกผู้สมัครและสร้าง Evaluation Draft

- **Role:** EVALUATOR
- **Request:** CreateEvaluationRequest
- **Response:** 201 Evaluation DRAFT
- **Validation:** บัญชี ACTIVE; รอบ OPEN; ผู้ประเมินคนเดิมไม่มี Evaluation ที่ยังไม่ถูกยกเลิก; ผู้สมัครมี active Evaluation < 3; ใช้ transaction/row lock ป้องกันเลือกพร้อมกันเกิน 3 คน
- **Error Code:** APPLICANT_NOT_FOUND, USER_INACTIVE, ROUND_NOT_OPEN, ACTIVE_CRITERIA_REQUIRED, DUPLICATE_EVALUATION, EVALUATOR_LIMIT_REACHED, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** EVALUATION_CREATED, EVALUATION_CREATE_REJECTED

#### `GET /evaluations/{evaluationId}` — อ่านรายการประเมิน

- **Role:** ADMIN, EVALUATOR
- **Request:** Path: evaluationId
- **Response:** Evaluation
- **Validation:** Evaluator อ่านได้เฉพาะของตน; Admin อ่านได้เพื่อการตรวจสอบตามหน้าที่
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_ACCESS_DENIED
- **Audit Event:** EVALUATION_VIEWED

#### `PATCH /evaluations/{evaluationId}` — บันทึกหรือแก้ไข Draft

- **Role:** EVALUATOR
- **Request:** scores + comment + version
- **Response:** Evaluation
- **Validation:** เจ้าของ Evaluation เท่านั้น; สถานะ DRAFT หรือ REOPENED; คะแนนทุกค่าต้องอยู่ใน min/max ของ criterion version ที่ผูกไว้; version ต้องตรง
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_NOT_OWNER, EVALUATION_NOT_EDITABLE, ROUND_NOT_OPEN, SCORE_OUT_OF_RANGE, CRITERION_VERSION_MISMATCH, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** EVALUATION_DRAFT_SAVED

#### `POST /evaluations/{evaluationId}/review` — ตรวจความครบถ้วนก่อน Submit

- **Role:** EVALUATOR
- **Request:** Path + CSRF
- **Response:** EvaluationReview
- **Validation:** เกณฑ์ required ต้องมีคะแนนครบ; ความคิดเห็นบังคับตาม Scoring Rule; ไม่เปลี่ยนสถานะ Evaluation
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_NOT_OWNER, EVALUATION_NOT_EDITABLE, ROUND_NOT_OPEN, EVALUATION_INCOMPLETE, SCORE_OUT_OF_RANGE, CSRF_INVALID
- **Audit Event:** EVALUATION_REVIEWED

#### `POST /evaluations/{evaluationId}/submit` — ยืนยันส่งผลประเมิน

- **Role:** EVALUATOR
- **Request:** confirmation=true + version
- **Response:** Evaluation + optional ResultSummary
- **Validation:** confirmation ต้อง true; ใช้เฉพาะคะแนนครบถ้วน; total เป็นผลรวม Embedded Point ของ 10 เกณฑ์โดยไม่คูณ `weight_percent` ซ้ำ; เปลี่ยนเป็น SUBMITTED แบบ atomic; หาก Submitted คนที่ 2 หรือ 3 ให้คำนวณค่าเฉลี่ยเลขคณิตจาก evaluator total ใหม่อัตโนมัติ
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_NOT_OWNER, EVALUATION_ALREADY_SUBMITTED, EVALUATION_INCOMPLETE, ROUND_NOT_OPEN, SCORE_OUT_OF_RANGE, CONCURRENCY_CONFLICT, CSRF_INVALID
- **Audit Event:** EVALUATION_SUBMITTED, RESULT_SUMMARY_RECALCULATED

#### `DELETE /evaluations/{evaluationId}` — ยกเลิกการเลือกผู้สมัครก่อน Submit

- **Role:** EVALUATOR
- **Request:** Path + CSRF
- **Response:** 204 No Content
- **Validation:** ยกเลิกได้เฉพาะ DRAFT/REOPENED ก่อน Submit; ใช้ soft-cancel และไม่นับใน activeEvaluationCount
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_NOT_OWNER, EVALUATION_ALREADY_SUBMITTED, ROUND_NOT_OPEN, CSRF_INVALID
- **Audit Event:** EVALUATION_CANCELLED

#### `POST /evaluations/{evaluationId}/reopen` — เปิดผล Submitted ให้แก้ไขตามนโยบาย

- **Role:** ADMIN
- **Request:** reason
- **Response:** Evaluation REOPENED
- **Validation:** ต้องมีเหตุผล; ต้องเป็นไปตาม Reopen Policy; ผลสรุปเดิมต้องถูกทำเครื่องหมาย stale และคำนวณใหม่เมื่อ Submit ซ้ำ
- **Error Code:** EVALUATION_NOT_FOUND, EVALUATION_NOT_SUBMITTED, REOPEN_NOT_ALLOWED, INVALID_ROUND_STATUS_TRANSITION, CSRF_INVALID
- **Audit Event:** EVALUATION_REOPENED

### Result Summaries

#### `GET /result-summaries` — ค้นหาและแสดงผลสรุป

- **Role:** ADMIN
- **Request:** roundId + filters
- **Response:** Paged<ResultSummary>
- **Validation:** คะแนนและกราฟใช้เฉพาะ Evaluation SUBMITTED
- **Error Code:** ROUND_NOT_FOUND, FORBIDDEN
- **Audit Event:** RESULT_SUMMARY_LIST_VIEWED

#### `GET /result-summaries/{applicantRoundId}` — อ่านผลสรุปของผู้สมัคร

- **Role:** ADMIN
- **Request:** Path: applicantRoundId
- **Response:** ResultSummary
- **Validation:** Draft/Cancelled ไม่ถูกนำมาคำนวณ; Submitted <2 อาจคืน summaryScore=null พร้อมสถานะปัจจุบัน
- **Error Code:** APPLICANT_NOT_FOUND, SUMMARY_NOT_AVAILABLE
- **Audit Event:** RESULT_SUMMARY_VIEWED

#### `POST /result-summaries/{applicantRoundId}/recalculate` — คำนวณผลสรุปใหม่ด้วยตนเอง

- **Role:** ADMIN
- **Request:** Path + CSRF
- **Response:** ResultSummary
- **Validation:** ใช้เฉพาะ Submitted จาก evaluator ไม่ซ้ำกัน 2–3 คน; evaluator total เป็นผลรวม Embedded Point โดยไม่คูณ `weight_percent` ซ้ำ; summary เป็นค่าเฉลี่ยเลขคณิต; มี Result Summary ได้หนึ่งรายการต่อ applicantRoundId; ใช้เพื่อ recovery/verification ไม่ใช่ flow ปกติ
- **Error Code:** APPLICANT_NOT_FOUND, SUMMARY_NOT_AVAILABLE, ROUND_ARCHIVED, SCORING_RULE_INVALID, CSRF_INVALID
- **Audit Event:** RESULT_SUMMARY_MANUALLY_RECALCULATED

#### `GET /result-summaries/dashboard` — อ่านข้อมูล Simple Dashboard

- **Role:** ADMIN
- **Request:** Query: roundId
- **Response:** DashboardSummary
- **Validation:** กราฟคะแนนใช้เฉพาะผล Submitted; count status ต้องสอดคล้องกับ Round status และ submittedCount
- **Error Code:** ROUND_NOT_FOUND
- **Audit Event:** DASHBOARD_VIEWED

### Reports

#### `POST /reports/exports` — สร้างงานส่งออกรายงาน

- **Role:** ADMIN
- **Request:** CreateReportExportRequest
- **Response:** 202 ReportExport
- **Validation:** รองรับ XLSX/CSV; ข้อมูลต้องมาจาก Result Summary และ Evaluation SUBMITTED เท่านั้น; Closed Incomplete ต้องไม่มี final summaryScore
- **Error Code:** ROUND_NOT_FOUND, REPORT_FORMAT_UNSUPPORTED, REPORT_DATA_INCONSISTENT, EXPORT_IN_PROGRESS, CSRF_INVALID
- **Audit Event:** REPORT_EXPORT_REQUESTED

#### `GET /reports/exports/{exportId}` — อ่านสถานะงานส่งออก

- **Role:** ADMIN
- **Request:** Path: exportId
- **Response:** ReportExport
- **Validation:** -
- **Error Code:** REPORT_EXPORT_NOT_FOUND
- **Audit Event:** -

#### `GET /reports/exports/{exportId}/download` — ดาวน์โหลดไฟล์รายงาน

- **Role:** ADMIN
- **Request:** Path: exportId
- **Response:** Binary file
- **Validation:** สถานะต้อง READY และยังไม่หมดอายุ; ตรวจสิทธิ์ผู้ใช้งานก่อนดาวน์โหลด
- **Error Code:** REPORT_EXPORT_NOT_FOUND, REPORT_NOT_READY, REPORT_EXPIRED, FILE_STORAGE_ERROR
- **Audit Event:** REPORT_EXPORTED

### Audit Logs

#### `GET /audit-logs` — ค้นหา Audit Log

- **Role:** ADMIN
- **Request:** Filters + pagination
- **Response:** Paged<AuditLog>
- **Validation:** ช่วงเวลาต้องไม่เกินค่าที่กำหนดเพื่อควบคุมประสิทธิภาพ; ผลลัพธ์ต้องปกปิดข้อมูลลับและข้อมูลส่วนบุคคลที่ไม่จำเป็น
- **Error Code:** FORBIDDEN, INVALID_DATE_RANGE
- **Audit Event:** AUDIT_LOG_SEARCHED

#### `GET /audit-logs/{auditLogId}` — อ่าน Audit Log รายการเดียว

- **Role:** ADMIN
- **Request:** Path: auditLogId
- **Response:** AuditLog
- **Validation:** ปกปิด secret/token เสมอ
- **Error Code:** AUDIT_LOG_NOT_FOUND
- **Audit Event:** AUDIT_LOG_VIEWED

## 3. Error Response มาตรฐาน

```json
{
  "code": "EVALUATOR_LIMIT_REACHED",
  "message": "ผู้สมัครมีรายการประเมินที่ใช้งานอยู่ครบ 3 รายการแล้ว",
  "details": [{ "field": "applicantRoundId", "reason": "active evaluation limit" }],
  "traceId": "01J2Y7QY8M8F6QK1J8N9P0ABCD",
  "timestamp": "2026-07-23T14:30:00Z"
}
```

## 4. รายการ Error Code สำคัญ

Source of Truth: [`SEMS_Error_Code_Catalog.md`](./SEMS_Error_Code_Catalog.md)

Endpoint ต้องใช้ชื่อ canonical ใน catalog โดยเฉพาะ `DUPLICATE_EVALUATION`, `EVALUATOR_LIMIT_REACHED`, `EVALUATION_NOT_OWNER`, `INVALID_ROUND_STATUS_TRANSITION`, `UNSUPPORTED_FILE_TYPE` และ `traceId`.

## 5. Confirmed-response API additions

Every mutation below requires the SEMS session, CSRF token, object-level authorization, optimistic concurrency/idempotency where shown, canonical error envelope `{code, message, details, traceId, timestamp}`, and the listed audit event.

| Method / URL | Role and object authorization | Request / validation / concurrency | Response | Canonical errors | Audit event |
|---|---|---|---|---|---|
| `POST /evaluations/{id}/reopen-requests` | owner Evaluator; Admin only on behalf of owner | reason, reference, optional `onBehalfOf`; Submitted; normally Open round; idempotency key | request `PENDING` | `EVALUATION_NOT_FOUND`, `EVALUATION_NOT_OWNER`, `EVALUATION_NOT_SUBMITTED`, `REOPEN_NOT_ALLOWED`, `CONCURRENCY_CONFLICT` | `EVALUATION_REOPEN_REQUESTED` |
| `POST /evaluation-reopen-requests/{id}/decision` | Head/delegate; technical Admin cannot decide own request | approve/reject, reason, expected version; preserve revision; return editable state to Draft | request + Evaluation | `FORBIDDEN`, `REOPEN_NOT_ALLOWED`, `CONCURRENCY_CONFLICT` | `EVALUATION_REOPEN_DECIDED` |
| `POST /evaluations/{id}/resubmit` | Evaluation owner only | complete scores, confirmation, expected version; Embedded Point; after commit recalculate Submitted mean | Evaluation + Result Summary | existing submit errors | `EVALUATION_RESUBMITTED`, `RESULT_SUMMARY_RECALCULATED` |
| `DELETE /evaluations/{id}` | Draft owner only | reason, expected version; soft-cancel atomically releases slot | `204` | existing cancel errors | `EVALUATION_CANCELLED` |
| `POST /applications/{id}/controlled-corrections` | Admin with application access; independent approval when required | reason, before/after fields, expected version; identity triplet immutable | correction record | `APPLICANT_NOT_FOUND`, `FORBIDDEN`, `VALIDATION_ERROR`, `CONCURRENCY_CONFLICT` | `CONTROLLED_CORRECTION_CREATED` |
| `POST /scholarship-rounds/{id}/reopen-requests` | Head/System Owner | reason, reference; Closed only; Archived rejected; idempotency key | request `PENDING` | `ROUND_NOT_FOUND`, `ROUND_ARCHIVED`, `INVALID_ROUND_STATUS_TRANSITION` | `ROUND_REOPEN_REQUESTED` |
| `POST /round-reopen-requests/{id}/decision` | designated faculty approver | approve/reject, reason, expected version; supersede old Final snapshot atomically | request + Round | `FORBIDDEN`, `ROUND_ARCHIVED`, `CONCURRENCY_CONFLICT` | `ROUND_REOPEN_DECIDED`, `REPORT_SNAPSHOT_SUPERSEDED` |
| `GET /scholarship-rounds/{id}/report-snapshots` | Admin with round access | filter status; immutable records | snapshots | `ROUND_NOT_FOUND`, `FORBIDDEN` | `REPORT_SNAPSHOT_LISTED` |
| `POST /reports/exports` | Admin with round access | format XLSX/CSV, profile `INTERNAL_FULL`/`SUMMARY_MASKED`; idempotency key | export job | existing report errors | `REPORT_EXPORT_REQUESTED` |
| `GET/POST /code-lists` | read: authorized users; mutate: Admin | version/concurrency; used values become Inactive, never deleted | code-list data | `FORBIDDEN`, `VALIDATION_ERROR`, `CONCURRENCY_CONFLICT` | `CODE_LIST_CHANGED` |
| `GET /documents/{id}/scan-status` | user authorized for the application/document | no file bytes; state only | Quarantined/Scanning/Clean/Rejected/Unavailable | `DOCUMENT_NOT_FOUND`, `DOCUMENT_ACCESS_DENIED` | `DOCUMENT_SCAN_STATUS_VIEWED` |

Confirmed limits: PDF 20 MB, JPG/PNG 10 MB, 10 applicant files, XLSX/CSV import 20 MB. Production download/view is denied until scan status is Clean. Evaluator responses expose only own Evaluation plus slot/Submitted/minimum-completion counts.

## 6. Remaining external API records

Formal approval evidence, KKU production client/claims/URIs, actual domains, rate limits based on measured traffic and infrastructure assignments remain pending. Scoring, reopen, report, retention, session and file-security business rules are no longer Open.

## 7. ไฟล์ Machine-readable

ดูรายละเอียด schema, request/response และ custom extensions (`x-roles`, `x-validation`, `x-error-codes`, `x-audit-events`) ใน [`openapi.yaml`](./openapi.yaml) และดูสรุป endpoint แบบตารางใน [`endpoint-matrix.csv`](./endpoint-matrix.csv)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.4 | 2026-07-24 | SEMS Design Team | Added confirmed reopen/correction/round/report/code-list/scan contracts and object-authorization/concurrency/audit rules. |
| v1.3 | 2026-07-24 | SEMS Design Team | Made the embedded-point total and arithmetic-mean summary formula explicit across submit and recalculation operations. |
| v1.2 | 2026-07-23 | SEMS Design Team | Standardized error catalog/aliases, Release 1 import types and provisional round-opening validation. |
| v1.1 | 2026-07-23 | SEMS Design Team | Initial API draft indexed for System Design Review. |
