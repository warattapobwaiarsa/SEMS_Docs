# SEMS Error Code Catalog

| Metadata | Value |
|---|---|
| Document ID | `SEMS-ERR-001` |
| Version | **v0.4** |
| Last Updated | **2026-07-24** |
| Status | **Draft — System-wide Source of Truth** |

ทุก SRS, User Story, API, OpenAPI, UI และ Test Case ต้องอ้าง code จากไฟล์นี้ ห้ามสร้าง alias ใหม่โดยไม่แก้ catalog และ revision history

## Error Contract

```json
{
  "code": "ERROR_CODE",
  "message": "ข้อความที่ผู้ใช้เข้าใจได้",
  "details": [
    {
      "field": "fieldName",
      "reason": "รายละเอียดข้อผิดพลาด"
    }
  ],
  "traceId": "trace-id",
  "timestamp": "2026-07-23T12:00:00Z"
}
```

- ไม่มี object `error` ครอบอีกชั้น
- `details` เป็น array; ว่างได้แต่ห้ามเปลี่ยนเป็น object
- ใช้ `traceId` เท่านั้นใน error response
- ห้ามเปิดเผย stack trace, SQL, token, secret, session, credential หรือ storage/internal path

## Canonical Codes

| Code | HTTP | Meaning |
|---|---:|---|
| `AUTH_REQUIRED` | 401 | ไม่มี session หรือ session หมดอายุ |
| `TOKEN_VALIDATION_FAILED` | 401 | OIDC token ไม่ผ่าน validation |
| `STATE_MISMATCH` | 400 | OAuth state ไม่ตรง |
| `NONCE_MISMATCH` | 400 | OIDC nonce ไม่ตรง |
| `USER_NOT_PROVISIONED` | 403 | ไม่มีบัญชี SEMS |
| `USER_INACTIVE` | 403 | บัญชี SEMS ไม่ active |
| `ACCESS_DENIED` | 403 | ไม่มีสิทธิ์ตามบทบาท/ขอบเขต |
| `CSRF_INVALID` | 403 | CSRF token หายหรือไม่ถูกต้อง |
| `ROUND_NOT_FOUND` | 404 | ไม่พบรอบทุน |
| `ROUND_NOT_OPEN` | 409 | กิจกรรมนี้ต้องใช้รอบ OPEN |
| `INVALID_ROUND_STATUS_TRANSITION` | 409 | Transition ไม่อยู่ใน state machine |
| `ACTIVE_CRITERIA_REQUIRED` | 409 | ไม่มี Active Criteria Set |
| `NO_APPLICANTS` | 422 | ไม่มีผู้สมัครก่อนเปิดรอบ; confirmed Blocking Error per RD-023/Q-021 |
| `DUPLICATE_EVALUATION` | 409 | ผู้ประเมินมี active evaluation เดิม |
| `EVALUATOR_LIMIT_REACHED` | 409 | มี active evaluator ครบ 3 |
| `EVALUATION_NOT_OWNER` | 403 | ไม่ใช่เจ้าของ evaluation |
| `EVALUATION_ALREADY_SUBMITTED` | 409 | รายการถูก submit แล้ว |
| `EVALUATION_INCOMPLETE` | 422 | ข้อมูลก่อน submit ไม่ครบ |
| `REQUIRED_FIELD_MISSING` | 422 | ฟิลด์บังคับหาย |
| `INVALID_STUDENT_ID` | 422 | รหัสนักศึกษาไม่ถูกต้อง |
| `INVALID_GPA` | 422 | GPA ไม่ถูกต้อง |
| `INVALID_DATE` | 422 | วันที่ไม่ถูกต้อง |
| `INVALID_PHONE` | 422 | เบอร์โทรไม่ถูกต้อง |
| `INVALID_EMAIL` | 422 | อีเมลไม่ถูกต้อง |
| `INVALID_COORDINATE` | 422 | พิกัดไม่ถูกต้อง |
| `DUPLICATE_STUDENT_IN_FILE` | 422 | Business key ซ้ำในไฟล์ |
| `DUPLICATE_STUDENT_IN_ROUND` | 409 | Business key ซ้ำในรอบ |
| `ORPHAN_CONTINUATION_ROW` | 422 | แถวต่อเนื่องไม่มีแถวหลัก |
| `SCORE_OUT_OF_RANGE` | 422 | คะแนนอยู่นอกช่วง criteria version |
| `CRITERION_VERSION_MISMATCH` | 409 | Criterion ไม่ตรง version ที่ evaluation ผูกไว้ |
| `CONCURRENCY_CONFLICT` | 409 | ข้อมูล/version เปลี่ยนพร้อมกัน |
| `UNSUPPORTED_FILE_TYPE` | 415 | Import Release 1 รับเฉพาะ `.xlsx` และ `.csv` |
| `DOCUMENT_TYPE_UNSUPPORTED` | 415 | ชนิด Applicant Document ไม่รองรับ |
| `IMPORT_FILE_TOO_LARGE` | 413 | ไฟล์ Import เกิน configuration |
| `DOCUMENT_TOO_LARGE` | 413 | Applicant Document เกิน configuration |
| `REPORT_FORMAT_UNSUPPORTED` | 415 | รูปแบบ Report Export ไม่รองรับ |
| `IMPORT_HAS_BLOCKING_ERRORS` | 409 | Import ยังมี blocking errors |

## Retired Aliases

| Retired | Canonical |
|---|---|
| `EVALUATION_DUPLICATE` | `DUPLICATE_EVALUATION` |
| `MAX_EVALUATORS_REACHED` | `EVALUATOR_LIMIT_REACHED` |
| `EVALUATION_NOT_OWNED` | `EVALUATION_NOT_OWNER` |

Retired aliases ห้ามปรากฏใน contract ใหม่ และใช้ได้เฉพาะ revision history ที่อธิบายการย้ายชื่อ

## Confirmed-response reuse rules

- Reopen request/decision reuses `EVALUATION_NOT_FOUND`, `EVALUATION_NOT_OWNER`, `EVALUATION_NOT_SUBMITTED`, `REOPEN_NOT_ALLOWED`, `FORBIDDEN` and `CONCURRENCY_CONFLICT`.
- Controlled Correction reuses `APPLICANT_NOT_FOUND`, `VALIDATION_ERROR`, `FORBIDDEN` and `CONCURRENCY_CONFLICT`.
- Round reopen reuses `ROUND_NOT_FOUND`, `ROUND_ARCHIVED`, `INVALID_ROUND_STATUS_TRANSITION`, `FORBIDDEN` and `CONCURRENCY_CONFLICT`.
- Report snapshots reuse `REPORT_EXPORT_NOT_FOUND`, `REPORT_NOT_READY`, `REPORT_EXPIRED`, `FORBIDDEN` and `CONCURRENCY_CONFLICT`.
- Code-list validation reuses `VALIDATION_ERROR`, `FORBIDDEN` and `CONCURRENCY_CONFLICT`.
- Scan status reuses `DOCUMENT_NOT_FOUND`, `DOCUMENT_ACCESS_DENIED` and `FILE_STORAGE_ERROR`.

No aliases were created; all responses retain `{ code, message, details, traceId, timestamp }`.

## Allowed Code Inventory

ชื่อที่อนุญาตใน OpenAPI `x-error-codes` มีเฉพาะรายการนี้; ความหมายของ core codes อยู่ในตารางด้านบน และ module-specific codes ต้องไม่เปลี่ยนความหมายโดยไม่มี revision:

`ACCESS_DENIED`, `ACTIVE_CRITERIA_REQUIRED`, `APPLICANT_ACCESS_DENIED`, `APPLICANT_NOT_FOUND`, `AUDIT_LOG_NOT_FOUND`, `AUTH_CALLBACK_INVALID`, `AUTH_REQUIRED`, `CONCURRENCY_CONFLICT`, `CRITERIA_INVALID`, `CRITERIA_LOCKED`, `CRITERIA_MINIMUM_REQUIRED`, `CRITERIA_SET_NOT_FOUND`, `CRITERIA_STATE_INVALID`, `CRITERION_NOT_FOUND`, `CRITERION_VERSION_MISMATCH`, `CSRF_INVALID`, `DOCUMENT_ACCESS_DENIED`, `DOCUMENT_IN_USE`, `DOCUMENT_NOT_FOUND`, `DOCUMENT_TOO_LARGE`, `DOCUMENT_TYPE_UNSUPPORTED`, `DUPLICATE_ACTIVE_CRITERIA_SET`, `DUPLICATE_CRITERION_CODE`, `DUPLICATE_EMAIL`, `DUPLICATE_EVALUATION`, `DUPLICATE_KKU_SUB`, `DUPLICATE_ROUND_CODE`, `DUPLICATE_STUDENT_IN_FILE`, `DUPLICATE_STUDENT_IN_ROUND`, `DUPLICATE_TARGET_FIELD`, `EVALUATION_ACCESS_DENIED`, `EVALUATION_ALREADY_SUBMITTED`, `EVALUATION_INCOMPLETE`, `EVALUATION_NOT_EDITABLE`, `EVALUATION_NOT_FOUND`, `EVALUATION_NOT_OWNER`, `EVALUATION_NOT_SUBMITTED`, `EVALUATOR_LIMIT_REACHED`, `EXPORT_IN_PROGRESS`, `FILE_STORAGE_ERROR`, `FORBIDDEN`, `IMPORT_ALREADY_CONFIRMED`, `IMPORT_FILE_EMPTY`, `IMPORT_FILE_TOO_LARGE`, `IMPORT_HAS_BLOCKING_ERRORS`, `IMPORT_MAPPING_INCOMPLETE`, `IMPORT_NOT_FOUND`, `IMPORT_NOT_MAPPED`, `IMPORT_NOT_VALIDATED`, `IMPORT_STATE_INVALID`, `INVALID_COORDINATE`, `INVALID_DATE`, `INVALID_DATE_RANGE`, `INVALID_EMAIL`, `INVALID_GPA`, `INVALID_PHONE`, `INVALID_RETURN_URL`, `INVALID_ROUND_STATUS_TRANSITION`, `INVALID_SCORE_RANGE`, `INVALID_STUDENT_ID`, `INVALID_WEIGHT`, `LAST_ACTIVE_ADMIN`, `NONCE_MISMATCH`, `NO_APPLICANTS`, `ORPHAN_CONTINUATION_ROW`, `REOPEN_NOT_ALLOWED`, `REPORT_DATA_INCONSISTENT`, `REPORT_EXPIRED`, `REPORT_EXPORT_NOT_FOUND`, `REPORT_FORMAT_UNSUPPORTED`, `REPORT_NOT_READY`, `REQUIRED_FIELD_MISSING`, `ROUND_ARCHIVED`, `ROUND_HAS_EVALUATIONS`, `ROUND_NOT_FOUND`, `ROUND_NOT_OPEN`, `SCORE_OUT_OF_RANGE`, `SCORING_RULE_INVALID`, `SSO_LOGOUT_FAILED`, `SSO_UNAVAILABLE`, `STATE_MISMATCH`, `SUMMARY_NOT_AVAILABLE`, `TOKEN_VALIDATION_FAILED`, `UNKNOWN_TARGET_FIELD`, `UNSUPPORTED_FILE_TYPE`, `USER_INACTIVE`, `USER_NOT_FOUND`, `USER_NOT_PROVISIONED`, `VALIDATION_ERROR`, `VERSION_ALREADY_EXISTS`

## Related Documents

- Governing contract: [SEMS API Specification](./SEMS_API_Specification.md)
- Machine-readable contract: [OpenAPI](./openapi.yaml)

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.4 | 2026-07-24 | SEMS Documentation Team | ปรับภาษาไทยเป็นหลักและทำให้คำศัพท์ทางเทคนิคสอดคล้องกับนโยบายเอกสาร |
| v0.3 | 2026-07-24 | SEMS Design Team | Added backlinks to the governing Markdown and OpenAPI specifications. |
| v0.2 | 2026-07-24 | SEMS Design Team | Removed unused generic/round-state error codes and documented module-specific import, document and report codes already present in the allowed inventory. |
| v0.1 | 2026-07-23 | SEMS Design Team | Established canonical error envelope, code names and retired aliases. |
