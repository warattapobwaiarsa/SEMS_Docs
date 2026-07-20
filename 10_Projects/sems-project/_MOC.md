---
type: Project-MOC
project: SEMS Project
status: Active
tags: [project, moc]
created: 2026-07-20
---

# 🗺️ SEMS Project Map of Content (MOC)

ยินดีต้อนรับสู่แดชบอร์ดหลักของโครงการ **SEMS (Smart Enterprise Management System)** เอกสารนี้ทำหน้าที่เป็นศูนย์กลางเชื่อมโยงข้อมูลทั้งหมดของโครงการเพื่อให้คุณสืบค้นและดูความเชื่อมโยงใน Obsidian ได้อย่างรวดเร็ว

---

## 🚀 ข้อมูลทั่วไปของโครงการ (General Info)
*   **เป้าหมายโครงการ:** พัฒนาระบบบริหารจัดการองค์กรอัจฉริยะ (SEMS) เพื่อยกระดับการทำงาน
*   **Repository:** [Git Repo Link] (ระบุลิงก์ของคุณที่นี่)
*   **Figma UI/UX:** [Figma Link] (ระบุลิงก์งานดีไซน์ที่นี่)
*   **สถานะโครงการ:** 🟢 กำลังพัฒนา (Active)

---

## 📂 สารบัญเอกสารแยกตามเฟส (Document Navigation)

### 📋 1. ข้อกำหนดและความต้องการ (Planning & Requirements)
*   **เอกสารหลัก:** [[Requirements/README|ดูคำอธิบายภาพรวมโฟลเดอร์ Requirements]]
*   **SRS:** [[Requirements/SRS - System Requirements]] (ข้อกำหนดระบบหลัก)
*   **รายการ User Stories:**
    *   *ตารางแสดงความต้องการผู้ใช้ด้านล่างนี้จะอัปเดตอัตโนมัติหากเปิดใช้ปลั๊กอิน Dataview*

```dataview
TABLE status, priority, created
FROM "10_Projects/sems-project/Requirements"
WHERE type = "User-Story"
SORT priority DESC
```

---

### 🎨 2. การออกแบบเชิงเทคนิค (Design & Architecture)
*   **เอกสารหลัก:** [[Design/README|ดูคำอธิบายภาพรวมโฟลเดอร์ Design]]
*   **สถาปัตยกรรมระบบ:** [[Design/System Architecture]] (SAD)
*   **การออกแบบฐานข้อมูล:**
    *   [[Design/Database - ERD]] (โครงสร้างรวม)
    *   *ตารางข้อมูลในระบบ (อัปเดตอัตโนมัติ):*

```dataview
TABLE tags, created
FROM "10_Projects/sems-project/Design"
WHERE type = "DB-Table"
```

*   **รายการ API Specifications:**
    *   *รายชื่อ API ที่บันทึกไว้ในระบบ (อัปเดตอัตโนมัติ):*

```dataview
TABLE method, path, status
FROM "10_Projects/sems-project/Design"
WHERE type = "API-Spec"
SORT method ASC
```

---

### 🧪 3. การประกันคุณภาพและการทดสอบ (Testing & QA)
*   **เอกสารหลัก:** [[Testing/README|ดูคำอธิบายภาพรวมโฟลเดอร์ Testing]]
*   **แผนและกรณีทดสอบ:** [[Testing/Test Plan & Test Cases]]
*   **เอกสารการรับมอบระบบ (UAT):** [[Testing/UAT Scenarios]]

---

### 🚀 4. การติดตั้งและส่งมอบ (Deployment & Handover)
*   **เอกสารหลัก:** [[Deployment/README|ดูคำอธิบายภาพรวมโฟลเดอร์ Deployment]]
*   **คู่มือการขึ้นระบบ:** [[Deployment/Deployment Guide]]
*   **คู่มือผู้ใช้:** [[Deployment/User Manual]]

---

> [!TIP]
> **การเชื่อมโยงความรู้ไปยังคลังสมองส่วนตัว (Everyday Connections):**
> หากคุณพบเทคนิคดีๆ ระหว่างเขียนโค้ด ให้เขียนลิงก์ไปยังคลังความรู้ส่วนตัวของคุณในโฟลเดอร์ `20_Areas/` เสมอ เช่น:
> - พัฒนาระบบ Auth ด้วย `[[20_Areas/Backend/JWT Authentication Best Practices]]`
> - จัดการ CSS ด้วย `[[20_Areas/Frontend/Tailwind Responsive Layout Grid]]`
