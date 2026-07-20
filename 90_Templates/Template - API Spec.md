---
type: API-Spec
project: [[_MOC]]
status: Planned # Planned, Implemented, Deprecated
method: GET # GET, POST, PUT, DELETE, PATCH
path: /api/v1/...
tags: [design, api]
created: {{date}}
---

# API: `{{value:method}}` `{{value:path}}`

## 1. คำอธิบาย (Description)
- **รายละเอียด:** [API นี้ทำหน้าที่อะไร]
- **การเข้าถึงสิทธิ์ (Authorization):** [Public / Bearer Token / Role-based]

## 2. ข้อมูลการส่งคำขอ (Request)
- **Headers:**
  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Query Parameters / Request Body:**
  ```json
  {
    "example_key": "example_value"
  }
  ```

## 3. ข้อมูลการตอบกลับ (Response)
- **Success (200 OK):**
  ```json
  {
    "status": "success",
    "data": {}
  }
  ```
- **Error (400 Bad Request / 401 Unauthorized / 500 Server Error):**

## 4. ตารางฐานข้อมูลที่เกี่ยวข้อง (Database Tables)
- [[Database Table - Example]]
