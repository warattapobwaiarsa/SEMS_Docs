# การจัดลำดับความสำคัญ Feature ด้วยวิธี MoSCoW — SEMS

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-MOSCOW-001` |
| Version | **v0.3** |
| Last Updated | **2026-07-25** |
| Status | **Draft — Pending Review** |
| Author | **SEMS Requirements Team** |

[START HERE](../START_HERE.md) › [📋 Requirements](./README.md) › การจัดลำดับความสำคัญ Feature ด้วยวิธี MoSCoW — SEMS

## 1. วัตถุประสงค์

เอกสารนี้จัดกลุ่ม Functional Features ของ Scholarship Evaluation Management System (SEMS) ตาม MoSCoW เพื่อให้เห็นชัดว่า Feature ใดจำเป็นต่อ Core Flow, Feature ใดเลื่อนได้ และ Feature ใดอยู่นอกขอบเขต พร้อมแยก Supporting/Non-functional Requirements และ Traceability ออกจากตารางหลักเพื่อให้อ่านง่ายตาม Comment ที่ได้รับ

## 2. ขอบเขต

- ตารางหลักครอบคลุม Functional Features จาก User Stories, Confirmed-response stories, PRD, SRS และ Proposal โดยรวมรายการซ้ำเป็นความสามารถเดียว
- Supporting/Non-functional Requirements เช่น Security, Audit integrity, Retention, Backup, Performance และ Capacity อยู่ในตารางแยกและไม่นับเป็น Functional Feature
- Design Constraints และ Prohibited Behaviours แยกจาก Won't-have Features เพื่อไม่ให้ทางเลือกทางเทคนิคหรือข้อห้ามถูกตีความเป็น Feature
- Acceptance Criteria ใช้เป็นหลักฐานประกอบ แต่ไม่แยกเป็น Feature ใหม่
- เอกสารนี้เป็น Draft สำหรับตรวจทาน ไม่ใช่หลักฐานอนุมัติ Requirement Baseline

## 3. นิยาม MoSCoW ตาม Comment

| กลุ่ม | นิยามที่ใช้ |
| :--- | :--- |
| **Must have** | หากไม่มีแล้วผู้ใช้ไม่สามารถทำ Core Flow ตั้งแต่ Login, Import, ประเมิน, Submit, คำนวณผล ถึง Export ได้ หรือผลลัพธ์หลักผิดกฎ/ระบบมีช่องโหว่ร้ายแรงจนใช้งานจริงไม่ได้อย่างยอมรับได้ |
| **Should have** | สำคัญต่อการใช้งานจริง การแก้กรณียกเว้น Lifecycle, Audit หรือ Administration แต่ Core Flow ปกติยังทำงานครบและเลื่อนไป Release ถัดไปได้ |
| **Could have** | เพิ่มความสะดวกหรือ UX และมีวิธีพื้นฐาน/Manual รองรับอยู่แล้วโดยไม่กระทบ Business Rule หรือผลคะแนน |
| **Won't have** | เป็น Functional Capability ที่เอกสารระบุว่าไม่ทำในโครงการหรือ Release 1 หรือต้องมีโครงการ/การอนุมัติแยก |

## 4. วิธีพิจารณา Feature

1. ถามก่อนว่าเมื่อไม่มี Feature แล้ว Core Flow ส่วนใดหยุดหรือผลลัพธ์ใดผิด หากไม่มีผลดังกล่าวจะไม่จัด Must เพียงเพราะอยู่ใน PRD หรือ Release 1
2. ใช้ Priority ใน User Stories เป็นค่าเริ่มต้น แล้วตรวจซ้ำกับ PRD, SRS, Decision Register และลักษณะ Dependency/Security/Data Integrity
3. รวม Technical Controls ที่เป็นส่วนประกอบของ Feature เดียวกัน ไม่แยกย่อยจนจำนวน Must สูงจากรายละเอียดทางเทคนิค
4. แยกกรณีผิดพลาด/กรณียกเว้นที่เลื่อนได้เป็น Should แม้ SRS บางรายการระบุ Must และบันทึกข้อขัดแย้งไว้ให้ยืนยัน
5. ใช้ Could เฉพาะรายการ Optional/Nice to have/ทำเมื่อมีเวลา หรือมี Manual/Core alternative ที่มีหลักฐาน
6. ใช้ Won't เฉพาะ Functional Capability ที่ไม่ทำจริง ส่วนข้อห้ามและ Design Choice อยู่ในหัวข้อแยก
7. เก็บ Story ID, Requirement ID, Decision ID และ Trace ID ในตาราง Traceability เท่านั้น

## 5. ตาราง Functional Features ตาม MoSCoW

ตารางแบ่งตามกลุ่ม MoSCoW เพื่อให้ตรวจสอบแต่ละกลุ่มได้ง่าย ภายในแต่ละกลุ่มเรียงตาม Core Flow ของระบบ ส่วน Won't have เรียงตามประเภทของ Out-of-Scope Capability การเปลี่ยนลำดับนี้ไม่ได้หมายถึงการเปลี่ยน Priority หรือ Scope

### 5.1 Must have

| Feature | กลุ่ม | เหตุผลที่จัดไว้กลุ่มนี้ |
| :--- | :---: | :--- |
| เข้าสู่ระบบด้วย KKU Account ผ่าน OAuth/OIDC | Must have | หากไม่มี ผู้ใช้ทุกบทบาทเริ่มใช้งาน SEMS ไม่ได้ จึงไม่สามารถเข้าสู่ขั้น Import, ประเมิน หรือ Export |
| Authorization และ RBAC ตามบทบาท รอบทุน และ Ownership | Must have | หากไม่มี ผู้ประเมินอาจอ่านหรือแก้ผลของผู้อื่นและ Admin-only flow ถูกเรียกได้โดยผู้ไม่มีสิทธิ์ ทำให้ระบบไม่ปลอดภัยพอสำหรับข้อมูลผู้สมัคร |
| ออกจากระบบ SEMS และยกเลิก Session | Must have | หาก Session เดิมยังใช้ได้หลัง Logout ผู้ใช้อื่นบนอุปกรณ์ร่วมอาจเข้าถึงข้อมูลและผลประเมินต่อได้ ซึ่งเป็นช่องโหว่ร้ายแรง |
| ค้นหาและดูบัญชี SEMS | Must have | Admin ต้องค้นหาบัญชีเพื่อเชื่อมตัวตน กำหนดบทบาท และแก้สถานะ มิฉะนั้นผู้ประเมินที่ต้องใช้ Core Flow จะไม่ได้รับสิทธิ์อย่างควบคุม |
| Pre-provision บัญชี เชื่อม KKU Identity และกำหนดบทบาท | Must have | Login เพียงอย่างเดียวไม่ให้สิทธิ์ใช้งาน ผู้ใช้ต้องถูกเชื่อมกับบัญชีและบทบาทก่อนจึงจะเข้าถึง Core Flow ได้ |
| เปิดหรือปิดสิทธิ์บัญชี SEMS | Must have | หากบัญชีที่ถูกถอนสิทธิ์ยังเรียก API ได้ ระบบจะเปิดให้ผู้ไม่มีอำนาจเข้าถึง PII และคะแนน จึงใช้งานจริงไม่ได้อย่างยอมรับได้ |
| สร้างรอบทุน | Must have | Applicant, Criteria, Evaluation และ Report ต้องผูกกับรอบทุน หากไม่มีจะเริ่มและแยกกระบวนการประเมินแต่ละรอบไม่ได้ |
| แก้ไข ตรวจความพร้อม และเปิดรอบทุน | Must have | ผู้ประเมินสร้าง Draft ได้เฉพาะรอบ Open ที่มี Applicant และ Active Criteria หากไม่มีขั้นเปิดรอบ Core evaluation จะเริ่มไม่ได้ |
| อัปโหลด `.xlsx`/`.csv` และจับคู่คอลัมน์ | Must have | เป็นช่องทางนำ Applicant เข้าระบบ หากไม่มีจะไม่มีข้อมูลสำหรับเปิดรอบ เลือกผู้สมัคร หรือประเมิน |
| Preview, Normalize และ Validation ก่อน Import | Must have | หากข้ามขั้นนี้ identifier, วันที่ หรือข้อมูลบังคับอาจผิดและถูกใช้ต่อในการประเมิน ทำให้ข้อมูลและผลลัพธ์หลักไม่น่าเชื่อถือ |
| ยืนยัน Import แบบ Transaction และเก็บประวัติ Batch | Must have | หาก Confirm ไม่เป็นชุดเดียวอาจเกิด Applicant ครึ่งชุดหรือข้อมูลซ้ำ ทำให้ Core Flow ใช้ข้อมูลไม่สอดคล้อง |
| รองรับผู้สมัครหนึ่งคนสมัครหลายประเภททุนในรอบเดียว | Must have | Business key ที่ยืนยันแยกใบสมัครตามประเภททุน หากไม่มีข้อมูล เอกสาร Evaluation และคะแนนของแต่ละทุนอาจถูกทับหรือรวมผิด |
| ดูและจัดการข้อมูลผู้สมัครกับประวัติทุน/กยศ. แบบ Snapshot ต่อรอบ | Must have | ผู้ประเมินต้องใช้ข้อมูลประกอบที่ถูกผูกกับรอบเพื่อให้คะแนน หากไม่มีหน้าข้อมูลนี้การประเมินจะขาดหลักฐานหลัก |
| ตรวจ Required-before-evaluation ก่อนสร้าง Draft | Must have | หากสร้าง Draft จากข้อมูลสำคัญที่ขาด ผู้ประเมินอาจให้คะแนนจากข้อมูลไม่ครบและ Result Summary ผิดวัตถุประสงค์ |
| อัปโหลดเอกสารผู้สมัคร | Must have | เอกสารเป็นข้อมูลประกอบที่ผู้ประเมินต้องใช้ตามขอบเขตโครงการ หากไม่มีการอัปโหลด Core evaluation จะขาดหลักฐานที่กำหนด |
| Preview หรือ Download เอกสารตามสิทธิ์ | Must have | หากผู้ประเมินเปิดเอกสารที่ได้รับสิทธิ์ไม่ได้ จะประเมินข้อมูลประกอบไม่ครบ; หากเปิดโดยไม่ตรวจสิทธิ์ระบบจะเปิดเผย PII ร้ายแรง |
| สร้างชุดเกณฑ์ คะแนน และ Outcome Fields สำหรับรอบทุน | Must have | หากไม่มีเกณฑ์ ผู้ประเมินกรอกคะแนนไม่ได้และระบบสร้างผลรวมตามสูตรไม่ได้ |
| Validate และ Activate Criteria Version | Must have | Draft/Submit ต้องอ้าง Active Criteria ที่ครบและคะแนนเต็มถูกต้อง หาก Activate เกณฑ์ผิด ผลคะแนนหลักจะผิดตามไปด้วย |
| ล็อกเกณฑ์ที่ใช้งานและสร้าง Version ใหม่ | Must have | หากแก้เกณฑ์ย้อนหลังหลังมี Draft คะแนนเก่าและใหม่จะใช้กฎคนละชุดโดยตรวจไม่ได้ ทำให้ Result Summary ไม่ถูกต้อง |
| ค้นหาผู้สมัครในรอบที่เปิด | Must have | เป็นจุดเริ่มของผู้ประเมินในการเลือกผู้สมัคร หากไม่มีจะสร้าง Evaluation Draft สำหรับรายการที่กำลังสัมภาษณ์ไม่ได้ |
| เลือกผู้สมัครและสร้าง Evaluation Draft ไม่ซ้ำ สูงสุด 3 คน | Must have | หากไม่ตรวจผู้ประเมินซ้ำและเพดาน 3 คน จำนวน input ของสูตรจะผิด และ Draft/Submit ขั้นถัดไปเริ่มไม่ได้อย่างถูกต้อง |
| แสดงข้อมูล Applicant, Documents, History และ Criteria ในหน้าประเมิน | Must have | หากไม่มี ผู้ประเมินไม่เห็นข้อมูลที่ใช้ตัดสินคะแนนและต้องกลับไปใช้ระบบ/ไฟล์ภายนอก ทำให้ Core evaluation ไม่ครบ |
| กรอกคะแนน ความคิดเห็น และคำแนะนำภายใต้ Validation | Must have | คะแนนรายเกณฑ์เป็น input โดยตรงของผลสรุป หากกรอกไม่ได้หรือไม่ตรวจช่วง ระบบจะไม่มีผลหรือได้ผลผิดกฎ |
| Manual Save และกลับมาแก้ Draft | Must have | การประเมินอาจใช้หลายช่วง หากบันทึกไม่ได้ข้อมูลจะสูญก่อน Submit และผู้ประเมินทำ Core Flow ต่อเนื่องไม่ได้ |
| Review คะแนน ความคิดเห็น Outcome และยอดรวมก่อนส่ง | Must have | หากไม่มีด่าน Review ผู้ประเมินไม่เห็นข้อมูลที่จะล็อกและเข้าสูตรคำนวณ ทำให้ Submit ผิดโดยไม่มีโอกาสตรวจขั้นสุดท้าย |
| ยืนยัน Submit และล็อกผลประเมิน | Must have | Result Summary ใช้เฉพาะ Submitted หากไม่มีการ Submit ระบบจะคำนวณผล ปิดรอบ และ Export ผลสำเร็จไม่ได้ |
| คำนวณคะแนนรวมรายผู้ประเมินจาก Embedded Points | Must have | หากไม่มีหรือใช้สูตรผิด ระบบจะสร้าง evaluator total ที่ใช้เป็น input ของ Result Summary ไม่ได้อย่างถูกต้อง |
| สร้างคะแนนสรุปเมื่อมี Submitted ครบ 2 คน | Must have | เป็นผลลัพธ์หลักของ SEMS หากไม่มีจะกำหนด Minimum Complete, Final Score หรือรายงานผลไม่ได้ |
| คำนวณใหม่เมื่อผู้ประเมินคนที่ 3 Submit | Must have | ระบบรองรับ 2–3 คน หากไม่คำนวณใหม่ผลสรุป Dashboard และ Export จะยังใช้เพียง 2 คนและผิดกฎที่ยืนยัน |
| ตรวจความครบถ้วนและปิดรอบ | Must have | หากไม่มีการ Close ระบบไม่สามารถตรึงผลและกำหนดผลสุดท้าย/ไม่ครบเพื่อส่งออกรายงานรอบนั้นได้ |
| กำหนด Finalized หรือ Closed Incomplete หลังปิดรอบ | Must have | หากผู้สมัครที่มี Submitted ต่ำกว่า 2 ได้ Final Score หรือสถานะไม่ตรง Count รายงานหลักจะผิดและใช้ตัดสินใจไม่ได้ |
| Dashboard ภาพรวม Submitted count และสถานะผู้สมัคร | Must have | Admin ใช้ตรวจความพร้อมก่อน Close; หากไม่มีมุมมองรวมจะไม่สามารถติดตามว่ารอบพร้อมปิดตาม Core workflow ที่กำหนดหรือไม่ |
| ส่งออก Excel/CSV ที่ตรง Result Summary | Must have | Export เป็นปลายทาง Core Flow และผลส่งมอบของโครงการ หากไม่มีผลประเมินไม่สามารถนำออกไปใช้ได้ |
| ส่งออกข้อมูลตามสิทธิ์โดยไม่รวม Restricted PII | Must have | หาก Export เปิดเผยข้อมูลเกินสิทธิ์ ระบบจะสร้างรายงานได้แต่ไม่ปลอดภัยพอใช้งานจริงกับข้อมูลส่วนบุคคล |

### 5.2 Should have

| Feature | กลุ่ม | เหตุผลที่จัดไว้กลุ่มนี้ |
| :--- | :---: | :--- |
| Archive รอบทุนเป็น Read-only | Should have | Core Flow จบที่ปิดรอบและ Export ได้โดยยังไม่ Archive; Feature นี้ช่วยแยกรอบย้อนหลังและป้องกันการแก้ภายหลัง จึงเลื่อนได้ |
| Exceptional Round Reopen และ Final Snapshot แบบ Superseded | Should have | เป็นกระบวนการแก้กรณีพิเศษหลังปิดรอบ รอบปกติยัง Close และ Export ได้ครบโดยไม่ Reopen จึงเลื่อนได้แต่ต้องควบคุมเมื่อเพิ่มภายหลัง |
| Controlled Correction พร้อมเหตุผล Before/After และ Audit | Should have | รองรับการแก้ข้อมูลที่ผิดหลังเริ่มประเมิน แต่กรณีปกติสามารถ Import ข้อมูลที่ตรวจแล้วและทำ Core Flow จนครบได้โดยไม่ใช้ Correction |
| จัดการ Code List แบบมี Version และ Audit | Should have | Core Flow ใช้ค่ามาตรฐานที่ตั้งไว้ล่วงหน้าได้ก่อน ระบบจัดการแบบ Dynamic ช่วยงาน Admin และรักษาประวัติเมื่อค่ามีการเปลี่ยน จึงเลื่อนได้ |
| ยกเลิก Draft แบบ Soft Cancel และคืน evaluator slot | Should have | ช่วยแก้กรณีเลือกผิดและคืน slot แต่ Core Flow ปกติยังเลือก บันทึก และ Submit Draft ที่ถูกต้องได้โดยไม่ใช้ Cancel |
| ขอ อนุมัติ และ Reopen Submitted Evaluation พร้อม Revision | Should have | เป็นทางแก้ข้อผิดพลาดหลัง Submit; กรณีปกติที่ Review แล้วส่งถูกต้องยังคำนวณและ Export ได้ครบ จึงเลื่อนได้ |
| กรองและเจาะดูรายการจาก Dashboard | Should have | Dashboard รวมและรายการ Applicant ยังแสดงสถานะได้ การ drill-down ลดเวลาหาเคสค้างแต่ไม่บล็อก Submit, Close หรือ Export |
| Report profiles, Interim Export และ Immutable Final Snapshot | Should have | Fixed safe Excel/CSV ยังส่งมอบผลหลักได้ Feature นี้เพิ่มหลายโปรไฟล์ อายุไฟล์ และ lifecycle หลัง Reopen จึงเลื่อนได้ |
| ดู Audit Trail และค้นหาเหตุการณ์พื้นฐาน | Should have | Core Flow ปกติยัง Login ถึง Export ได้โดยไม่มีหน้าดู Audit แต่หน้าดังกล่าวสำคัญต่อการตรวจเหตุผิดปกติและงานกำกับดูแล |

### 5.3 Could have

| Feature | กลุ่ม | เหตุผลที่จัดไว้กลุ่มนี้ |
| :--- | :---: | :--- |
| Full KKU Logout | Could have | SEMS ยกเลิก Session ภายในได้ครบอยู่แล้ว การออกจากทุกบริการ KKU เป็นความสะดวกเพิ่มเติมและทำได้เมื่อ KKU รองรับกับผู้ใช้ยืนยัน |
| คัดลอกเกณฑ์จากรอบเดิมเป็น Draft | Could have | Admin ยังสร้างชุดเกณฑ์ใหม่ได้ด้วย Feature หลัก การคัดลอกเพียงลดเวลาตั้งค่าและ SRS ระบุ Nice to have |
| Autosave ระหว่างกรอกคะแนน | Could have | Manual Save รองรับ Draft ครบแล้ว Autosave ลดโอกาสลืมบันทึกแต่ไม่เปลี่ยน Business Rule หรือผลคะแนน |
| หมายเหตุภายในสำหรับ Admin | Could have | Admin ยังจัดการ Applicant และติดตามเหตุการณ์จากข้อมูลหลัก/Audit ได้ ช่องหมายเหตุเป็นความสะดวกเพิ่มเติม |
| Advanced Search | Could have | Search/filter พื้นฐานรองรับการหา Applicant แล้ว Advanced Search เป็น UX enhancement ที่ไม่มีผลต่อคะแนนหรือสถานะ |
| รวมไฟล์ CSV เป็น ZIP | Could have | CSV สองไฟล์ส่งมอบข้อมูลครบอยู่แล้ว ZIP เป็นเพียง packaging ที่ Decision ระบุว่า optional |
| PDF Export, Custom Template และรูปแบบรายงานเสริม | Could have | Excel/CSV เป็นรูปแบบหลักที่ส่งมอบได้ครบ Proposal/SRS ระบุรูปแบบเหล่านี้เป็น Optional |
| Detailed Audit Viewer และ Advanced Audit Search | Could have | หน้าค้นหาพื้นฐานรองรับเหตุการณ์หลักแล้ว มุมมองละเอียดเป็นความสะดวกในการสืบค้นและ Proposal ระบุเป็นฟังก์ชันเสริม |
| Notification ภายในระบบ | Could have | ผู้ใช้ติดตามงานจาก Dashboard/สถานะได้ Notification ช่วยเตือนแต่ไม่มี Feature หลักพึ่งพา |

### 5.4 Won't have

| Feature | กลุ่ม | เหตุผลที่จัดไว้กลุ่มนี้ |
| :--- | :---: | :--- |
| ระบบสมัครทุนออนไลน์สำหรับนักศึกษา | Won't have | SEMS เริ่มจากไฟล์ที่งานทุนนำเข้า ไม่ครอบคลุมการรับใบสมัครจากนักศึกษา |
| ให้ผู้สมัครเข้าสู่ SEMS โดยตรง | Won't have | บทบาทที่ยืนยันมี Admin และ Evaluator การเพิ่ม applicant login/consent เป็น workflow และ security scope ใหม่ |
| การอนุมัติทุนขั้นสุดท้ายระดับนโยบาย/คณะกรรมการ | Won't have | SEMS จัดทำคะแนนและรายงานประกอบการตัดสินใจ แต่ไม่แทนอำนาจอนุมัติของคณะกรรมการ |
| ประกาศผลทุนแก่ผู้สมัครโดยตรง | Won't have | ผู้สมัครไม่ใช่ผู้ใช้ SEMS ใน Release 1 และหน่วยงานนำรายงานไปดำเนินการประกาศต่อ |
| โอนเงินทุนหรือจัดการทางการเงิน | Won't have | วัตถุประสงค์ของ SEMS สิ้นสุดที่การประเมินและ Export ธุรกรรมการเงินต้องเป็นระบบ/โครงการแยก |
| เชื่อมตรงหรือแทนฐานข้อมูลทะเบียน/ระบบทุนกลาง | Won't have | Release 1 ใช้ File Import และไม่แทน Source System กลาง การเชื่อมตรงต้องมี interface agreement และ scope แยก |
| จัดการหรือจัดเก็บรหัสผ่าน KKU ใน SEMS | Won't have | KKU SSO เป็นผู้จัดการรหัสผ่าน การสร้าง password management ใน SEMS ซ้ำระบบกลางและอยู่นอกขอบเขต |
| Native Mobile Application | Won't have | SEMS ส่งมอบเป็น Web Application; Native app ต้องมี codebase, deployment และ security review แยก |
| มอบหมายผู้สมัครให้อาจารย์ล่วงหน้า | Won't have | Workflow ที่ยืนยันให้อาจารย์ค้นหาและเลือกผู้สมัครเอง การทำ pre-assignment เป็นกระบวนการคนละแบบและอยู่นอกขอบเขต |
| จัดคิว/ห้องสัมภาษณ์ Zoom หรือควบคุมประชุมออนไลน์ | Won't have | SEMS รองรับการประเมินผู้สมัครที่กำลังสัมภาษณ์ แต่ไม่จัดการกระบวนการประชุมออนไลน์ |
| รองรับ National ID ใน Release 1 | Won't have | PRD และ Decisions ระบุว่าต้องมี lawful-need/security approval แยกก่อน จึงไม่ทำ capability นี้ใน Release 1 |
| Import ไฟล์ Legacy `.xls` | Won't have | Release 1 รับ `.xlsx`/`.csv` ซึ่งรองรับ Core Import แล้ว และเอกสารระบุ `.xls` เป็น Optional/Out of Scope |

## 6. Supporting / Non-functional Requirements

รายการต่อไปนี้เป็นเงื่อนไขคุณภาพและการควบคุมระบบ ไม่ใช่ Functional Features ในตารางที่อาจารย์ขอ

| Supporting Requirement | ระดับความจำเป็น | เหตุผล |
| :--------------------- | :-------------: | :----- |
| Transport, OIDC และ Session Security | Must have | หากไม่มี HTTPS, token validation, CSRF/replay protection หรือ Session revocation ผู้โจมตีอาจยึดตัวตนและเข้าถึง PII/คะแนน ทำให้ระบบใช้งานจริงไม่ได้อย่างยอมรับได้ |
| File Validation, Private Storage, Malware Scan และ Quarantine | Must have | ไฟล์เป็น trust boundary หากไฟล์ปลอม/มัลแวร์ถูกเปิดหรือ storage เปิดสาธารณะ ผู้ใช้และข้อมูลจะเสี่ยงร้ายแรง |
| Input, Error และ Secret Safety | Must have | หากรับ input โดยไม่จำกัดหรือเปิดเผย stack/token/secret อาจเกิด injection หรือ credential leak ที่กระทบทุก Core Flow |
| Data Minimization และ PII Protection | Must have | ระบบประมวลผลข้อมูลผู้สมัครที่ละเอียดอ่อน หากเก็บ/แสดงเกินจำเป็นหรือไม่ Mask จะไม่ปลอดภัยพอใช้งานจริง |
| Transaction, Concurrency และ Database Integrity | Must have | Import, Selection, Submit และ Recalculation ต้องไม่เกิดข้อมูลครึ่งชุด/ผู้ประเมินเกินเพดาน มิฉะนั้นผลคะแนนหลักผิด |
| Audit Event Integrity, Redaction และ Trace ID | Must have | แม้หน้าดู Audit เลื่อนได้ แต่เหตุการณ์สำคัญต้องถูกบันทึกตั้งแต่แรกแบบ append-only มิฉะนั้นหลักฐานย้อนหลังไม่สามารถสร้างคืนได้ |
| Retention, Legal Hold และ Secure Deletion | Should have | Core Flow ทำงานได้ก่อนมี automation เต็มรูปแบบ แต่ต้องกำหนดและดำเนินการก่อนข้อมูลหมดอายุเพื่อไม่เก็บ PII เกินนโยบายหรือทำลายหลักฐาน |
| Backup, Restore Test และ RPO/RTO | Should have | การทำงานปกติยังดำเนินได้ แต่หากเกิดเหตุข้อมูลจะกู้คืนไม่ได้ จึงควรพร้อมก่อน production และตรวจ restore ตามรอบ |
| Performance, Capacity และ Load Test | Should have | Core logic ทำงานได้โดยไม่มีผลวัด แต่ต้องทดสอบเป้าหมายก่อนอ้างว่ารองรับปริมาณจริงและก่อนใช้งาน production |
| Availability, Observability และ Time Handling | Should have | ไม่เปลี่ยน Business Rule แต่ช่วยตรวจ incident, เชื่อม trace และแสดงเวลาได้สอดคล้องในการปฏิบัติงานจริง |
| Usability, Accessibility และ Browser Compatibility | Should have | Core API/logic ยังทำงานได้ แต่ผู้ใช้บางกลุ่มอาจทำงานยากหรือเข้าไม่ถึง จึงควรครบก่อนส่งมอบใช้งานวงกว้าง |
| Maintainability, Migration และ Delivery Artifacts | Should have | ไม่ใช่ Feature ที่ผู้ใช้เรียก แต่ช่วยให้แก้กฎคะแนน ย้าย schema ติดตั้ง และดูแลระบบต่อได้โดยไม่สร้างความผิดพลาดซ้ำ |

## 7. Design Constraints และ Prohibited Behaviours

รายการเหล่านี้ไม่ใช่ Won't-have Features แต่เป็นทางเลือกการออกแบบหรือพฤติกรรมที่ระบบต้องไม่อนุญาต

| ประเภท | รายการ | เหตุผล |
| :--- | :--- | :--- |
| Design Constraint | เก็บ Binary Document ใน PostgreSQL | แบบที่ยืนยันใช้ Private File/Object Storage และเก็บ metadata ใน PostgreSQL จึงเป็น storage design choice ไม่ใช่ Feature ที่ผู้ใช้ร้องขอแล้วทีมตัดออก |
| Prohibited Behaviour | แก้คะแนน/ข้อมูลที่กระทบผลหลัง Submit โดยไม่มี Approval, Revision หรือ Audit | ระบบต้องปฏิเสธพฤติกรรมนี้เพื่อรักษา Data Integrity; ความสามารถที่รองรับจริงคือ Controlled Correction/Reopen |

## 8. Traceability

| Feature | Story / Requirement / Decision Reference |
| :------ | :--------------------------------------- |
| เข้าสู่ระบบด้วย KKU Account ผ่าน OAuth/OIDC | `US-AUTH-001`; `FR-AUT-001`–`FR-AUT-005`; `TRC-001` |
| Authorization และ RBAC ตามบทบาท รอบทุน และ Ownership | `US-AUTH-002`; `FR-AUT-006`; `SEC-005`; `TRC-001` |
| ออกจากระบบ SEMS และยกเลิก Session | `US-AUTH-003`; `FR-AUT-005`; `SEC-007`; `TRC-001` |
| Full KKU Logout | `US-AUTH-003` Optional Note |
| ค้นหาและดูบัญชี SEMS | `US-USR-001`; `FR-AUT-007`–`FR-AUT-010`; `TRC-002` |
| Pre-provision บัญชี เชื่อม KKU Identity และกำหนดบทบาท | `US-USR-002`, `US-SEC-004`; `FR-AUT-011`; `RD-036`; `TRC-002`, `TRC-018` |
| เปิดหรือปิดสิทธิ์บัญชี SEMS | `US-USR-003`; `FR-AUT-009`, `FR-AUT-010`, `FR-AUT-011`; `RD-035`; `TRC-002`, `TRC-018` |
| สร้างรอบทุน | `US-RND-001`; `FR-RND-001`–`FR-RND-003`; `TRC-003` |
| แก้ไข ตรวจความพร้อม และเปิดรอบทุน | `US-RND-002`; `FR-RND-004`, `FR-RND-005`; `RD-023`; `TRC-003` |
| Archive รอบทุนเป็น Read-only | `US-RND-003`; `FR-RND-009`; `RD-048`; `TRC-003` |
| Exceptional Round Reopen และ Final Snapshot แบบ Superseded | `US-RND-004`; `FR-RND-011`; `RD-048`, `RD-049`; `TRC-003`, `TRC-016` |
| อัปโหลด `.xlsx`/`.csv` และจับคู่คอลัมน์ | `US-IMP-001`; `FR-IMP-001`–`FR-IMP-004`; `TRC-004` |
| Preview, Normalize และ Validation ก่อน Import | `US-IMP-002`; `FR-IMP-005`–`FR-IMP-011`, `FR-IMP-016`, `FR-IMP-017`; `RD-015`, `RD-017`, `RD-019`, `RD-020`; `TRC-004` |
| ยืนยัน Import แบบ Transaction และเก็บประวัติ Batch | `US-IMP-003`; `FR-IMP-012`–`FR-IMP-015`; `RD-018`, `RD-019`; `TRC-004` |
| Import ไฟล์ Legacy `.xls` | `US-IMP-001` Optional/Out-of-Scope Note |
| รองรับผู้สมัครหนึ่งคนสมัครหลายประเภททุนในรอบเดียว | `US-APP-004`; `FR-APP-008`; `RD-015`, `RD-024`, `RD-025`; `TRC-005` |
| ดูและจัดการข้อมูลผู้สมัครกับประวัติทุน/กยศ. แบบ Snapshot ต่อรอบ | `FR-APP-001`–`FR-APP-007`; `RD-026`, `RD-028`; `TRC-005`; Proposal §5.2.4, §5.2.6 |
| Controlled Correction พร้อมเหตุผล Before/After และ Audit | `US-COR-001`; `FR-APP-009`; `RD-027`; `TRC-005` |
| ตรวจ Required-before-evaluation ก่อนสร้าง Draft | `US-DAT-005`; `FR-IMP-017`; `RD-019`, `RD-028` |
| อัปโหลดเอกสารผู้สมัคร | `US-DOC-001`; `FR-DOC-001`, `FR-DOC-002`; `TRC-006` |
| Preview หรือ Download เอกสารตามสิทธิ์ | `US-DOC-002`; `FR-DOC-003`–`FR-DOC-005`; `TRC-006` |
| สร้างชุดเกณฑ์ คะแนน และ Outcome Fields สำหรับรอบทุน | `US-CRI-001`; `FR-CRI-001`–`FR-CRI-004`, `FR-CRI-010`, `FR-CRI-011`; `RD-012`, `RD-013`, `RD-014`, `RD-047`; `TRC-007` |
| Validate และ Activate Criteria Version | `US-CRI-002`; `FR-CRI-005`, `FR-CRI-006`; `TRC-007` |
| ล็อกเกณฑ์ที่ใช้งานและสร้าง Version ใหม่ | `US-CRI-003`; `FR-CRI-007`–`FR-CRI-009`, `FR-CRI-013`; `RD-012`, `RD-014`; `TRC-007` |
| จัดการ Code List แบบมี Version และ Audit | `FR-COD-001`; `RD-046` |
| คัดลอกเกณฑ์จากรอบเดิมเป็น Draft | `FR-CRI-012`; Proposal §5.4.2 |
| ค้นหาผู้สมัครในรอบที่เปิด | `US-SEL-001`; `FR-EVA-001`; `TRC-008` |
| เลือกผู้สมัครและสร้าง Evaluation Draft ไม่ซ้ำ สูงสุด 3 คน | `US-SEL-002`; `FR-EVA-001`–`FR-EVA-006`; `RD-001`–`RD-005`; `TRC-008` |
| ยกเลิก Draft แบบ Soft Cancel และคืน evaluator slot | `US-SEL-003`, `US-EVA-010`; `FR-EVA-014`; SRS §12 `FR-EVA-018`; `RD-009`; `TRC-009` |
| มอบหมายผู้สมัครให้อาจารย์ล่วงหน้า | Proposal §5.3 ข้อ 11 |
| แสดงข้อมูล Applicant, Documents, History และ Criteria ในหน้าประเมิน | `US-DRF-001`; `FR-EVA-007`; `TRC-009` |
| กรอกคะแนน ความคิดเห็น และคำแนะนำภายใต้ Validation | `US-DRF-002`; `FR-EVA-008`, `FR-SCO-015`; `RD-013`, `RD-047`; `TRC-009` |
| Manual Save และกลับมาแก้ Draft | `US-DRF-003`; `FR-EVA-009`; `TRC-009` |
| Autosave ระหว่างกรอกคะแนน | `US-DRF-003` Optional Note; Proposal §5.4.2 |
| หมายเหตุภายในสำหรับ Admin | Proposal §5.4.2 |
| Review คะแนน ความคิดเห็น Outcome และยอดรวมก่อนส่ง | `US-SUB-001`; `FR-EVA-010`; `TRC-010` |
| ยืนยัน Submit และล็อกผลประเมิน | `US-SUB-002`; `FR-EVA-011`–`FR-EVA-013`; `TRC-011` |
| ขอ อนุมัติ และ Reopen Submitted Evaluation พร้อม Revision | `US-SUB-003`, `US-EVA-010`; `FR-EVA-015`; SRS §12 `FR-EVA-017`; `RD-008` |
| คำนวณคะแนนรวมรายผู้ประเมินจาก Embedded Points | `US-SCR-001`; `FR-SCO-001`–`FR-SCO-004`; `RD-010`, `RD-011`; `TRC-012` |
| สร้างคะแนนสรุปเมื่อมี Submitted ครบ 2 คน | `US-SCR-002`; `FR-SCO-005`, `FR-SCO-006`, `FR-SCO-008`–`FR-SCO-010`; `RD-004`, `RD-006`, `RD-010`, `RD-011`; `TRC-012` |
| คำนวณใหม่เมื่อผู้ประเมินคนที่ 3 Submit | `US-SCR-003`; `FR-SCO-007`, `FR-SCO-011`, `FR-SCO-012`; `RD-005`, `RD-010`, `RD-011`; `TRC-013` |
| ตรวจความครบถ้วนและปิดรอบ | `US-CLS-001`, `US-RND-004`; `FR-RND-006`–`FR-RND-008`, `FR-RND-010`; `RD-007`; `TRC-003`, `TRC-014` |
| กำหนด Finalized หรือ Closed Incomplete หลังปิดรอบ | `US-CLS-002`; `FR-SCO-009`–`FR-SCO-012`; `RD-006`–`RD-008`; `TRC-014` |
| Dashboard ภาพรวม Submitted count และสถานะผู้สมัคร | `US-DSH-001`; `FR-DSH-001`–`FR-DSH-003`; `TRC-015` |
| กรองและเจาะดูรายการจาก Dashboard | `US-DSH-002`; `FR-RPT-001`, `FR-RPT-002`; `TRC-015` |
| Advanced Search | Proposal §5.4.2 |
| ส่งออก Excel/CSV ที่ตรง Result Summary | `US-RPT-001`; `FR-RPT-003`–`FR-RPT-006`; `RD-021`; `TRC-016` |
| ส่งออกข้อมูลตามสิทธิ์โดยไม่รวม Restricted PII | `US-RPT-002`; `FR-RPT-007`, `FR-RPT-008`; `RD-022`; `TRC-016`, `TRC-017` |
| Report profiles, Interim Export และ Immutable Final Snapshot | `US-RPT-003`; `FR-RPT-010`; `RD-021`, `RD-022`, `RD-031`, `RD-032`, `RD-049`; `TRC-016` |
| รวมไฟล์ CSV เป็น ZIP | `US-RPT-003`; `FR-RPT-006`; `RD-021` |
| PDF Export, Custom Template และรูปแบบรายงานเสริม | `FR-RPT-009`; Proposal §5.2.11, §5.4.2 |
| ดู Audit Trail และค้นหาเหตุการณ์พื้นฐาน | `FR-AUD-004`; `TRC-017` |
| Detailed Audit Viewer และ Advanced Audit Search | SRS §9 ข้อ 8; Proposal §5.4.2 |
| Notification ภายในระบบ | Proposal §5.4.2 |
| จัดการหรือจัดเก็บรหัสผ่าน KKU ใน SEMS | PRD Out of Scope; Proposal §5.1.2, §5.2.1 |
| ระบบสมัครทุนออนไลน์สำหรับนักศึกษา | Proposal §5.3 ข้อ 1 |
| การอนุมัติทุนขั้นสุดท้ายระดับนโยบาย/คณะกรรมการ | Proposal §5.3 ข้อ 2 |
| ประกาศผลทุนแก่ผู้สมัครโดยตรง | Proposal §5.3 ข้อ 3 |
| โอนเงินทุนหรือจัดการทางการเงิน | PRD Out of Scope; Proposal §5.3 ข้อ 4 |
| เชื่อมตรงหรือแทนฐานข้อมูลทะเบียน/ระบบทุนกลาง | PRD Out of Scope; Proposal §5.3 ข้อ 5 |
| ให้ผู้สมัครเข้าสู่ SEMS โดยตรง | Proposal §5.3 ข้อ 7 |
| Native Mobile Application | PRD Out of Scope; Proposal §5.3 ข้อ 8 |
| จัดคิว/ห้องสัมภาษณ์ Zoom หรือควบคุมประชุมออนไลน์ | Proposal §5.3 ข้อ 10; SRS §3.6 `FR-EVA-018` |
| รองรับ National ID ใน Release 1 | PRD Out of Scope; `US-DAT-005`; `RD-016`, `RD-029` |
| [Supporting] Transport/OIDC/Session Security | `SEC-001`–`SEC-008`, `NFR-SEC-010`; `RD-034`, `RD-035`; `TRC-018` |
| [Supporting] File Safety | `FR-DOC-006`, `FR-DOC-007`; `SEC-009`, `SEC-010`; `RD-038`, `RD-039`; `TRC-019` |
| [Supporting] Input/Error/Secret Safety | `SEC-008`, `SEC-012`, `SEC-014`, `SEC-015`; `NFR-MNT-003` |
| [Supporting] Data Minimization/PII | `SEC-011`, `SEC-013`, `SEC-016`; `NFR-SEC-010`; `RD-016`, `RD-022`, `RD-029` |
| [Supporting] Transaction/Concurrency/DB Integrity | `NFR-REL-001`, `NFR-REL-002`; `TRC-004`, `TRC-008`, `TRC-011`, `TRC-012` |
| [Supporting] Audit Integrity | `FR-AUD-001`–`FR-AUD-003`; `TRC-017` |
| [Supporting] Retention/Deletion | `NFR-RET-001`; `RD-030`–`RD-033`; `TRC-020` |
| [Supporting] Backup/Restore | `NFR-BCP-001`; `RD-041`; `TRC-020` |
| [Supporting] Performance/Capacity | `NFR-PERF-001`–`NFR-PERF-004`, `NFR-CAP-001`; `RD-040`; `TRC-020` |
| [Supporting] Availability/Observability/Time | `NFR-AVL-001`, `NFR-OBS-001`, `NFR-LOC-001` |
| [Supporting] Usability/Accessibility/Compatibility | `NFR-USA-001`–`NFR-USA-003`, `NFR-ACC-001`, `NFR-COMP-001` |
| [Supporting] Maintainability/Migration/Delivery | `NFR-MNT-001`–`NFR-MNT-003`, `NFR-DEL-001`, `NFR-REL-002` |
| [Constraint] Binary outside PostgreSQL | Proposal §5.3 ข้อ 9; `FR-DOC-002` |
| [Prohibited] Uncontrolled post-submit change | Proposal §5.3 ข้อ 6; `RD-008`, `RD-027` |

## 9. สรุปจำนวน Feature

### 9.1 Functional Features

| กลุ่ม | จำนวน Feature | สัดส่วนโดยประมาณ |
| :--- | ---: | ---: |
| Must have | 34 | 53.13% |
| Should have | 9 | 14.06% |
| Could have | 9 | 14.06% |
| Won't have | 12 | 18.75% |
| **รวม** | **64** | **100.0%** |

Must have ต่ำกว่า 60% หลังรวม Technical Controls และ Supporting Requirements ออกจากตารางหลัก และทบทวน Feature กรณียกเว้นตามคำถามว่า “หากไม่มี Core Flow ปกติยังทำงานครบหรือไม่” การเปลี่ยนกลุ่มไม่ได้ทำเพื่อให้สัดส่วนสมดุล แต่มีเหตุผลราย Feature ในตาราง

### 9.2 Supporting Requirements

| ระดับความจำเป็น | จำนวนรายการ |
| :--- | ---: |
| Must have | 6 |
| Should have | 6 |
| **รวม** | **12** |

## 10. การเปลี่ยน Priority จากเอกสาร v0.1

| Feature / Story | กลุ่มเดิม | กลุ่มใหม่ | เหตุผลที่เปลี่ยน |
| :-------------- | :-------: | :-------: | :--------------- |
| Archive รอบทุน (`US-RND-003`) | Must have | Should have | Core Flow ปกติจบที่ Close/Export ได้โดยยังไม่ Archive และสอดคล้อง Priority เดิมใน User Story |
| Controlled Correction (`US-COR-001`) | Must have | Should have | ใช้แก้กรณีข้อมูลผิดหลังเริ่มประเมิน; รอบที่ข้อมูลถูกต้องทำ Core Flow ได้ครบโดยไม่ใช้ Feature |
| Code List Management (`FR-COD-001`) | Must have | Should have | ระบบใช้ค่ามาตรฐานที่เตรียมไว้ล่วงหน้าได้ก่อน Dynamic administration จึงเลื่อนได้ |
| Reopen Submitted Evaluation (`US-SUB-003`) | Must have | Should have | เป็น exception flow หลังส่งผิด; normal Review/Submit/Calculate/Export ไม่พึ่ง Reopen และตรง Priority เดิมใน User Story |
| Exceptional Round Reopen (`US-RND-004`) | Must have | Should have | รอบปกติ Close และ Export ได้โดยไม่เปิดรอบที่ปิดแล้ว |
| Dashboard drill-down (`US-DSH-002`) | Must have | Should have | Dashboard รวมและ Applicant list ยังใช้ติดตามได้ Drill-down ลดเวลาแต่ไม่บล็อก Core Flow |
| Report profiles/Interim/Final lifecycle (`US-RPT-003`) | Must have | Should have | Fixed safe Excel/CSV ยังส่งมอบผลหลักได้ หลาย profile และ lifecycle ขั้นสูงเลื่อนได้ |
| Audit Trail Viewer (`FR-AUD-004`) | Must have | Should have | การบันทึก Audit ยังคงเป็น Supporting Must แต่หน้าดู/ค้นหาไม่จำเป็นต่อ Normal Core Flow และเลื่อนได้ |
| Session timeout/absolute lifetime/revocation | Functional Must | Supporting Must | ระดับความจำเป็นด้าน Security ไม่เปลี่ยน แต่ย้ายออกเพราะเป็น quality/control ไม่ใช่ Feature ที่ผู้ใช้เรียก |
| File signature/MIME/malware/quarantine | Functional Must | Supporting Must | ระดับความจำเป็นที่ trust boundary ไม่เปลี่ยน แต่เป็น control ภายใน Upload Feature |
| Data minimization/การปฏิเสธ National ID | Functional Must | Supporting Must | ระดับ Privacy control ไม่เปลี่ยน แต่ไม่ใช่ Functional Capability แบบเดียวกับ “รองรับ National ID” |
| Retention/Legal Hold/Secure Deletion | Functional Must | Supporting Should | Core Flow ปกติทำงานได้ก่อนมี automation เต็มรูปแบบ แต่ต้องเตรียมก่อนข้อมูลครบอายุและ production operation |
| Backup/Restore/RPO/RTO | Functional Must | Supporting Should | ไม่บล็อก Normal Core Flow แต่จำเป็นต่อ recovery เมื่อเกิด incident จึงเป็น operational requirement ที่เลื่อนได้จาก functional release |
| Capacity/Load-test baseline | Functional Must | Supporting Should | เป็นเป้าหมายคุณภาพและหลักฐานทดสอบ ไม่ใช่ Feature และ Core logic ทำงานได้ก่อนมีผลวัดจริง |
| เก็บ Binary ใน PostgreSQL | Won't have | Design Constraint | เป็น storage architecture ที่ไม่เลือกใช้ ไม่ใช่ Functional Feature ที่ทีมพิจารณาแล้วตัดออก |
| แก้ผลโดยไม่มี Approval/Revision/Audit | Won't have | Prohibited Behaviour | เป็นพฤติกรรมที่ระบบต้องปฏิเสธ ไม่ใช่ Capability ที่ต้องจัด MoSCoW |

`US-SEL-003` ยังคง **Should have** และ Functional Could/Won't เดิมที่ยังอยู่ในตารางไม่เปลี่ยนกลุ่ม

## 11. รายการที่ย้ายออกจาก Functional Table

| รายการเดิม | ตำแหน่งใหม่ | เหตุผล |
| :--- | :--- | :--- |
| Session timeout/absolute lifetime/revocation | Supporting — Transport/OIDC/Session Security | เป็น Security quality/control ไม่ใช่ Feature ที่ผู้ใช้เรียกโดยตรง |
| File signature/MIME/malware/quarantine | Supporting — File Safety | เป็น trust-boundary control ของ Upload Feature |
| Data minimization/การปฏิเสธ National ID ใน Core Flow | Supporting — Data Minimization/PII | เป็น Privacy control; ส่วน “รองรับ National ID” ยังคงเป็น Won't-have capability |
| Retention/Legal Hold/Secure Deletion | Supporting — Retention/Deletion | เป็นข้อมูล lifecycle policy ไม่ใช่ Functional Feature |
| Backup/Restore/RPO/RTO | Supporting — Backup/Restore | เป็น operational continuity requirement |
| Capacity/Load-test baseline | Supporting — Performance/Capacity | เป็น quality target และหลักฐานทดสอบ ไม่ใช่ Feature |
| เก็บ Binary ใน PostgreSQL | Design Constraint | เป็น storage design choice ไม่ใช่ Feature ที่ตกลงไม่ทำ |
| แก้ผลโดยไม่มี Approval/Revision/Audit | Prohibited Behaviour | เป็นพฤติกรรมที่ระบบต้องปฏิเสธ ไม่ใช่ Feature ที่เสนอให้พัฒนา |

## 12. รายการที่ต้องให้ Stakeholder หรืออาจารย์ยืนยัน

1. Priority ในเอกสารต้นทางยังขัดกับการตีความตาม Comment สำหรับ `US-DSH-002` (User Story Must แต่เอกสารนี้ Should), `FR-COD-001` (SRS Must แต่เอกสารนี้ Should), Controlled Correction, Exceptional Reopen และ Report lifecycle; ไม่ได้แก้ Source Documents อัตโนมัติ
2. `US-SEL-003` ระบุ Should แต่ SRS §12 `FR-EVA-018` ระบุ Must; เอกสารนี้คง Should เพราะเป็น exception flow
3. SRS ใช้ `FR-EVA-017` และ `FR-EVA-018` ซ้ำระหว่าง §3.6 กับ §12 โดยมีความหมายต่างกัน ตาราง Traceability ใส่ Section เพื่อแยกชั่วคราว แต่ต้องแก้ ID ก่อนทำ row-level baseline
4. `TRC-004` ยังระบุ “DB key open” แต่ `RD-015`, `RD-024`, `RD-025` ยืนยัน key แล้ว และ `TRC-017` ระบุ Audit retention ว่า open ทั้งที่ `RD-030` ยืนยันแล้ว
5. SRS ยังแสดง `FR-CRI-004` และ `FR-EVA-012` เป็น Open ขณะที่ Decision Register ระบุว่าไม่มี Critical/High Release 1 decision ค้าง
6. Formal approver, approval date/signature, production assignments และผลวัดจริงของ `RD-040`/`RD-045` ยังไม่มีหลักฐาน จึงไม่กล่าวอ้างว่าอนุมัติหรือบรรลุผลแล้ว
7. National ID มีสองความหมายที่ไม่ขัดกัน: “รองรับ National ID” เป็น Won't have ส่วน “ปฏิเสธ/ไม่เก็บ National ID” เป็น Supporting Must ด้าน Privacy

## 13. แหล่งอ้างอิง

1. [SEMS Product Requirements Document](./PRD/SEMS-PRD.md)
2. [SEMS — User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
3. [Software Requirements Specification](./SRS/SEMS-SRS.md)
4. [Requirement Decision Register](./SEMS_Requirement_Decision_Register.md)
5. [Requirement Decision Analysis](./SEMS_Requirement_Decision_Analysis.md)
6. [SEMS Traceability Matrix](./SEMS_Traceability_Matrix.md)
7. [ข้อเสนอโครงการ SEMS](./Proposal/SEMS-project-proposal.md)

## 14. Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.3 | 2026-07-25 | SEMS Requirements Team | จัด Functional Features แยกตามกลุ่ม Must, Should, Could และ Won't และเรียงภายในแต่ละกลุ่มตาม Core Flow โดยไม่เปลี่ยน Priority |
| v0.2 | 2026-07-25 | SEMS Requirements Team | ปรับเกณฑ์ MoSCoW ให้ตรง Comment, แยก Functional/Supporting Requirements, ย้าย Traceability ออกจากตารางหลัก และทบทวน Priority กับ Won't-have scope |
| v0.1 | 2026-07-25 | SEMS Requirements Team | สร้าง Feature Inventory และจัดกลุ่ม MoSCoW จาก Source Documents ใน Repository สำหรับตรวจทาน Release 1 |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)<br>
↑ หมวดเอกสาร: [📋 Requirements](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../START_HERE.md)<br>
→ ขั้นตอนถัดไป: ตรวจสอบการเชื่อมโยง Feature กับ Requirement และ Test Case ที่ [SEMS Traceability Matrix](./SEMS_Traceability_Matrix.md)

<!-- DOC_NAV_END -->
