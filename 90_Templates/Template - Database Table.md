---
type: DB-Table
project: [[_MOC]]
tags: [design, database]
created: {{date}}
---

# Database Table: `[ชื่อตาราง]`

## 1. คำอธิบาย (Description)
- **หน้าที่:** [ใช้เก็บข้อมูลอะไร]
- **ความสัมพันธ์ (Relationships):** 
  - เชื่อมโยงกับ `[[Database Table - Other]]` แบบ One-to-Many

## 2. โครงสร้างฟิลด์ (Data Dictionary)

| Field Name | Data Type | Key / Constraint | Nullable | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | UUID | PK / Default uuid_generate_v4() | No | รหัสหลักของข้อมูล |
| `created_at` | Timestamp | Default now() | No | วันเวลาที่สร้าง |
| `updated_at` | Timestamp | Default now() | No | วันเวลาที่แก้ไขล่าสุด |

## 3. ลิงก์ที่เกี่ยวข้อง
- API ที่ใช้งานตารางนี้: 
- User Stories ที่เกี่ยวข้อง: 
