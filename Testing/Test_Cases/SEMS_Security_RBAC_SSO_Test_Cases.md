# SEMS Security, RBAC and SSO Test Cases

| Metadata | Value |
| :--- | :--- |
| Version | **v0.2** |
| Last Updated | **2026-07-24** |
| Author | **SEMS QA Team** |
| Status | **Draft** |

## 1. Authentication/OIDC

### SEC-AUTH-001 Authorization Code + PKCE S256 Success

**Expected:** redirect ใช้ `response_type=code`, `scope` มี `openid`, ส่ง `code_challenge_method=S256`; callback ตรวจ state/nonce; ID token signature/issuer/audience/expiry ผ่านก่อนสร้าง session

### SEC-AUTH-002 State Missing or Mismatch

**Expected:** login ถูกปฏิเสธ; authorization code ไม่ถูกใช้; audit failure; ไม่มี open redirect

### SEC-AUTH-003 Nonce Missing or Mismatch

**Expected:** ID token ถูกปฏิเสธและไม่สร้าง local session

### SEC-AUTH-004 Reused Authorization Code

**Expected:** แลก token ครั้งที่สองไม่สำเร็จ; SEMS ไม่สร้าง session ซ้ำผิดปกติ

### SEC-AUTH-005 Invalid/Expired ID Token

**Expected:** 401/403 ตาม flow; ไม่เชื่อ claims ที่ไม่ verify

### SEC-AUTH-006 `/userinfo` Subject Mismatch

**Expected:** ปฏิเสธเมื่อ `sub` ไม่ตรงกับ ID token; audit security failure

### SEC-AUTH-007 SEMS Account Inactive

**Expected:** แม้ KKU auth สำเร็จ ต้องปฏิเสธ `USER_INACTIVE`

### SEC-AUTH-008 Logout

**Expected:** local session ถูกยกเลิก; protected API ตอบ 401; logout redirect อยู่ allowlist; full SSO logout ใช้เฉพาะนโยบายที่อนุมัติ

### SEC-AUTH-009 Token Revocation/Session Invalidation

**Expected:** เมื่อ session/token ถูก revoke หรือ account deactivate การเรียก protected API ถูกปฏิเสธภายในเวลาที่กำหนด

### SEC-AUTH-010 CSRF on State-changing Endpoint

**Expected:** cookie/session configuration และ CSRF protection ป้องกัน request จาก origin ที่ไม่อนุญาต

## 2. Role-based Access Control

| ID | Actor | Action | Expected |
|---|---|---|---|
| RBAC-D-001 | Evaluator | เปิด Admin Dashboard | 403/route denied |
| RBAC-D-002 | Evaluator | Create/Update/Delete Round | 403 |
| RBAC-D-003 | Evaluator | Import applicant | 403 |
| RBAC-D-004 | Evaluator | Manage Criteria | 403 |
| RBAC-D-005 | Evaluator | Export report | 403 |
| RBAC-D-006 | Evaluator | View audit log | 403 |
| RBAC-D-007 | Admin | Submit evaluation แทน evaluator | ปฏิเสธ เว้นแต่นโยบายระบุชัด |
| RBAC-D-008 | Inactive user | Protected API ใด ๆ | 403 `USER_INACTIVE` |

ทุกกรณีต้องทดสอบทั้ง UI route และ direct API request

## 3. Ownership and Data Scope

### SEC-OWN-001 Evaluator Edits Own Draft

**Expected:** allowed เมื่อ round Open และ record Draft/Reopened

### SEC-OWN-002 Evaluator Reads Another Evaluator's Evaluation Detail

**Expected:** ปฏิเสธหรือจำกัดข้อมูลตาม Permission Matrix; ห้ามคืนคะแนน/comment ที่ไม่ควรเห็น

### SEC-OWN-003 Evaluator Updates Another Evaluator's Draft

**Expected:** 403 `ACCESS_DENIED`; DB unchanged; audit denied

### SEC-OWN-004 Evaluator Submits Another Evaluator's Draft

**Expected:** 403; no state change; no summary recalculation

### SEC-OWN-005 Applicant Search Before Selection

**Expected:** แสดงเฉพาะข้อมูลขั้นต่ำสำหรับค้นหาใน Open round; ไม่เปิดรายละเอียดอ่อนไหว/เอกสาร

### SEC-OWN-006 Applicant Detail After Selection

**Expected:** evaluator เข้าถึง applicant ที่ตนมี active evaluation เท่านั้น ตาม field-level scope

### SEC-OWN-007 Direct Document IDOR

**Steps:** เปลี่ยน document ID เป็นของ applicant ที่ไม่ได้เลือก

**Expected:** 403/404; no metadata/path/signed URL; audit denied

### SEC-OWN-008 Cross-round IDOR

**Expected:** evaluator ที่มี evaluation ใน round A ไม่ได้สิทธิ์ applicant/document round B โดยอัตโนมัติ

### SEC-OWN-009 Cancelled Evaluation Loses Access

**Expected:** หลัง cancel สิทธิ์รายละเอียด/เอกสารถูกถอนตาม policy; search-level minimal data อาจยังเห็นเมื่อ round Open

### SEC-OWN-010 Submitted Evaluation Access

**Expected:** read-only own submitted result; edit endpoint deniedจนกว่าจะ Reopen

## 4. File Security

### SEC-FILE-001 MIME Mismatch

**Expected:** ตรวจ magic bytes/MIME ไม่เชื่อ extension อย่างเดียว

### SEC-FILE-002 Path Traversal Filename

**Input:** `../../secret.pdf`, encoded variants

**Expected:** sanitize generated storage key; ไม่ overwrite/อ่านไฟล์นอก namespace

### SEC-FILE-003 Direct Storage Access

**Expected:** bucket/directory private; signed URL อายุสั้นและออกหลัง authorization หรือ stream ผ่าน backend

### SEC-FILE-004 Stored XSS via Filename/Metadata

**Expected:** filename/comment ถูก output encode; script ไม่ execute ใน UI/export

### SEC-FILE-005 Malicious PDF/Image

**Expected:** preview/download ไม่ทำให้ server execute content; optional antivirus policy; Content-Disposition/CSP เหมาะสม

## 5. Session and API Security

### SEC-API-001 Force Browsing Hidden Endpoint

**Expected:** backend RBAC denies แม้ UI ไม่แสดงเมนู

### SEC-API-002 Mass Assignment

**Input:** evaluator ส่ง `role=Admin`, `owner_id` อื่น, `status=Submitted` ใน payload ที่ไม่ควรแก้

**Expected:** ignored/rejected; DTO whitelist; no privilege escalation

### SEC-API-003 SQL/Filter Injection

**Expected:** input parameterized; no DB error leakage; search behaves safely

### SEC-API-004 Excessive Data Exposure

**Expected:** list/search response ไม่คืนรายได้ครอบครัว เอกสาร path token หรือ fields ที่ไม่จำเป็น

### SEC-API-005 Rate/Abuse on Selection

**Expected:** repeated request ไม่ทำ data violation; rate limit/logging ตาม policy

### SEC-API-006 Error Message Leakage

**Expected:** ไม่มี stack trace, SQL, storage path, client secret หรือ internal host ใน production response

## 6. Audit and Privacy

### SEC-AUD-001 Audit Required Events

ต้องมีอย่างน้อย Login success/failure, access denied, user/role change, round state change, import confirm, selection success/reject, submit/reopen/cancel, document access denied และ export

### SEC-AUD-002 No Secrets in Logs

**Search:** password, `client_secret`, authorization code, access/refresh/id token, cookie, signed URL

**Expected:** absent หรือ redacted

### SEC-AUD-003 Minimal PII

**Expected:** audit ใช้ IDs และข้อมูลจำเป็น; ไม่คัดลอก document body หรือข้อมูลครอบครัวทั้งหมด

### SEC-AUD-004 Audit Integrity/Authorization

**Expected:** evaluator แก้/ลบ audit ไม่ได้; Admin access ตามหน้าที่; timestamps และ actor traceable

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2026-07-24 | SEMS QA Team | Replaced the inactive-account alias with canonical `USER_INACTIVE`. |
| v0.1 | 2026-07-23 | SEMS QA Team | Initial security, RBAC and SSO test cases. |
