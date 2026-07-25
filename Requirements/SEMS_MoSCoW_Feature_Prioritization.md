# การจัดลำดับความสำคัญ Feature ด้วยวิธี MoSCoW — SEMS

| Metadata | Value |
| :--- | :--- |
| Document ID | `SEMS-MOSCOW-001` |
| Version | **v0.1** |
| Last Updated | **2026-07-25** |
| Status | **Draft — Pending Review** |
| Author | **SEMS Requirements Team** |

[START HERE](../START_HERE.md) › [📋 Requirements](./README.md) › การจัดลำดับความสำคัญ Feature ด้วยวิธี MoSCoW — SEMS

## 1. วัตถุประสงค์

เอกสารนี้รวบรวมความสามารถที่มีหลักฐานอยู่ในขอบเขตของ Scholarship Evaluation Management System (SEMS) และจัดลำดับความสำคัญแบบ MoSCoW เพื่อใช้ตรวจทานขอบเขต Release 1 โดยไม่เพิ่ม Feature ที่ไม่มีแหล่งอ้างอิงใน Repository

## 2. ขอบเขต

- ครอบคลุม User Stories หลัก, Confirmed-response Release 1 stories, Functional/Non-functional Requirements ที่ยืนยันแล้ว, Optional Features และ Out-of-Scope Features
- รวมความสามารถด้าน Authentication, Authorization, Audit, Security, Privacy, Data Integrity, Retention และ Controlled Correction ที่จำเป็นต่อการทำงานอย่างปลอดภัย
- Acceptance Criteria ใช้เป็นหลักฐานประกอบเหตุผลและ Traceability แต่ไม่แยกเป็น Feature ใหม่
- รายการซ้ำต่างเอกสารถูกรวมเป็นแถวเดียวและระบุ Story ID, Requirement, Decision หรือ Trace ID ที่เกี่ยวข้อง
- เอกสารนี้เป็น Draft สำหรับตรวจทาน ไม่ใช่หลักฐานอนุมัติ Requirement Baseline

## 3. นิยาม MoSCoW ที่ใช้ในโครงการ

| กลุ่ม | นิยามสำหรับ SEMS |
| :--- | :--- |
| **Must have** | หากไม่มีแล้ว Core Flow ตั้งแต่ Login ถึง Export ทำงานไม่ครบ, Feature อื่นทำงานไม่ได้, คะแนน/ข้อมูลไม่ถูกต้อง หรือเกิดช่องว่างด้าน Authentication, Authorization, Audit, Privacy หรือ Security |
| **Should have** | สำคัญต่อการใช้งานจริงหรือกรณียกเว้น แต่ Core Flow ปกติยังทำงานได้และสามารถเลื่อนไป Release ถัดไปได้ |
| **Could have** | เป็นความสะดวก, UX หรือรูปแบบเสริมที่มีวิธีพื้นฐานรองรับอยู่แล้ว และเอกสารระบุเป็น Optional/Enhancement |
| **Won't have** | เอกสารระบุชัดว่าอยู่นอกขอบเขตโครงการหรือไม่รองรับใน Release 1 |

## 4. หลักเกณฑ์การจัดกลุ่ม

1. ใช้ลำดับ Source of Truth ตามงานนี้: PRD → User Stories → SRS → Decision Register → Decision Analysis → Traceability Matrix → Proposal/Scope
2. ใช้ Priority เดิมใน User Story เป็นค่าเริ่มต้น และเปลี่ยนเฉพาะเมื่อ PRD, Release 1 dependency, Security, Privacy หรือ Data Integrity ให้หลักฐานที่ชัดกว่า
3. ใช้หนึ่ง User Story หลักเป็นหนึ่ง Feature เว้นแต่ Story/Requirement หลายรายการอธิบายความสามารถเดียวกัน หรือ Confirmed-response story ครอบคลุมข้อควบคุมหลายโมดูล
4. ใช้ `TRC-xxx` เพื่อเชื่อมกลับไปยัง Requirement, User Story, Design และ Test Case ตาม Traceability Matrix; รายการที่ไม่มี Story ID ใช้ Requirement, Decision, Optional Note หรือ PRD/Proposal scope เป็น Reference
5. ไม่ลดจำนวน Must เพื่อทำให้สัดส่วนสมดุล เพราะ PRD และ SRS ระบุ Core Flow, Security และ Data Integrity จำนวนมากเป็นเงื่อนไขส่งมอบ

## 5. ตาราง Feature ตามโมดูลและ Core Flow

| Story ID / Reference | Feature | กลุ่ม | เหตุผลที่จัดไว้กลุ่มนี้ |
| :--- | :--- | :---: | :--- |
| `US-AUTH-001`; `FR-AUT-001..005`; `TRC-001` | 01 — เข้าสู่ระบบด้วย KKU Account ผ่าน OAuth/OIDC | Must have | หากไม่มี ผู้ใช้ทุกบทบาทเริ่ม Core Flow ไม่ได้; การตรวจ token, state, nonce และ PKCE เป็นขอบเขต Authentication ที่ป้องกันการปลอม Session |
| `US-AUTH-002`; `FR-AUT-006`; `SEC-005`; `TRC-001` | 01 — Authorization และ RBAC ระดับเมนู API รอบทุน และ Ownership | Must have | Feature ทุกโมดูลพึ่งพาการตรวจสิทธิ์ฝั่ง Backend; หากขาด ผู้ประเมินอาจอ่านหรือแก้ผลของผู้อื่นและข้อมูลส่วนบุคคลรั่วไหล |
| `US-AUTH-003`; `FR-AUT-005`; `SEC-007`; `TRC-001` | 01 — ออกจากระบบ SEMS และยกเลิก Session | Must have | หากยกเลิก Session ไม่ได้ การเข้าถึงค้างบนอุปกรณ์ร่วมจะยังใช้ข้อมูลผู้สมัครได้; Core security จึงไม่สมบูรณ์แม้ KKU SSO ยังทำงาน |
| `US-USR-001`; `FR-AUT-007..010`; `TRC-002` | 02 — ค้นหาและดูบัญชี SEMS | Must have | Admin ต้องระบุตัวผู้ใช้และสถานะก่อนกำหนดสิทธิ์; หากไม่มีจะบริหารบัญชีที่เข้า Core Flow และตรวจสอบความผิดพลาดของสิทธิ์ไม่ได้ |
| `US-USR-002`; `US-SEC-004`; `FR-AUT-011`; `RD-036`; `TRC-002`, `TRC-018` | 02 — Pre-provision บัญชี เชื่อม KKU Identity และกำหนดบทบาท | Must have | ป้องกันผู้มี KKU Account ได้สิทธิ์อัตโนมัติ; Login และ RBAC พึ่งพาการ bind `sub` กับบัญชีที่ Admin อนุมัติ |
| `US-USR-003`; `FR-AUT-009..011`; `RD-035`; `TRC-002`, `TRC-018` | 02 — เปิดหรือปิดสิทธิ์บัญชี SEMS | Must have | หากปิดบัญชีแล้ว API ยังยอมรับคำขอ ผู้ที่ถูกถอนสิทธิ์ยังเข้าถึง PII และผลประเมินได้; ต้องบังคับใช้กับคำขอถัดไป |
| `US-SEC-004`; `NFR-SEC-010`; `RD-034..035`; `TRC-018` | 02 — Session timeout, absolute lifetime และการเพิกถอน Session | Must have | Session อายุไม่จำกัดเพิ่มความเสี่ยงยึดบัญชี; ข้อกำหนด 30 นาที/8 ชั่วโมงและ revocation เป็น Release 1 security control |
| `US-RND-001`; `FR-RND-001..003`; `TRC-003` | 03 — สร้างรอบทุน | Must have | ผู้สมัคร เกณฑ์ Evaluation และรายงานทุกชุดต้องผูกกับรอบทุน; หากไม่มีจะเริ่มกระบวนการประเมินและแยกข้อมูลไม่ได้ |
| `US-RND-002`; `FR-RND-004..005`; `RD-023`; `TRC-003` | 03 — แก้ไข ตรวจความพร้อม และเปิดรอบทุน | Must have | การเลือกผู้สมัครและสร้าง Evaluation ต้องใช้รอบ `OPEN` ที่มี Applicant และ Active Criteria; หากขาด Core Flow จะหยุดก่อนการประเมิน |
| `US-RND-003`; `FR-RND-009`, `FR-RND-011`; `RD-048`; `TRC-003` | 03 — Archive รอบทุนเป็น Read-only | Must have | PRD ระบุการจัดเก็บรอบเป็น Core Feature และ Archived ต้องป้องกันการแก้หลักฐานย้อนหลัง; จึงยกระดับจาก Should ใน User Story เป็น Must |
| `US-IMP-001`; `FR-IMP-001..004`; `TRC-004` | 04 — อัปโหลด `.xlsx`/`.csv` และจับคู่คอลัมน์ | Must have | เป็นทางเข้าข้อมูลผู้สมัครที่ Proposal กำหนด; หากไม่มี Admin จะไม่มี Applicant สำหรับเปิดรอบและประเมิน |
| `US-IMP-002`; `FR-IMP-005..011`, `FR-IMP-016..017`; `RD-015`, `RD-017`, `RD-019..020`; `TRC-004` | 04 — Preview, Normalize และ Validation ก่อน Import | Must have | ป้องกันข้อมูลผิดรูปแบบ ขาดฟิลด์ หรือ identifier เสียก่อนเขียนฐานข้อมูล; Feature ประเมินและคำนวณคะแนนพึ่งข้อมูลที่ผ่านกฎนี้ |
| `US-IMP-003`; `FR-IMP-012..015`; `RD-018..019`; `TRC-004` | 04 — ยืนยัน Import แบบ Transaction และเก็บประวัติ Batch | Must have | หาก Confirm ไม่เป็น atomic อาจเกิดข้อมูลครึ่งชุดหรือ duplicate; Core Flow จะใช้ Applicant ที่ไม่สอดคล้องและตรวจย้อนกลับไม่ได้ |
| `US-APP-004`; `FR-APP-008`; `RD-015`, `RD-024..025`; `TRC-005` | 05 — รองรับผู้สมัครหนึ่งคนสมัครหลายประเภททุนในรอบเดียว | Must have | Release 1 ยืนยัน business key `(round,type,student)` และแต่ละใบสมัครมีผลแยกกัน; หากไม่มีจะทับข้อมูลหรือรวมคะแนนข้ามประเภททุน |
| `FR-APP-001..007`; `RD-026`, `RD-028`; `TRC-005`; Proposal §5.2.4, §5.2.6 | 05 — ดูและจัดการข้อมูลผู้สมัครกับประวัติทุน/กยศ. แบบ Snapshot ต่อรอบ | Must have | ผู้ประเมินต้องใช้ข้อมูลประกอบที่ถูกผูกกับรอบเพื่อให้คะแนน และ Result Summary ต้องไม่ซ้ำ; หากไม่มีการประเมินขาดข้อมูลหลักและเสี่ยงใช้ประวัติผิดรอบ |
| `US-COR-001`; `FR-APP-009`; `RD-027`; `TRC-005` | 05 — Controlled Correction พร้อมเหตุผล Before/After และ Audit | Must have | PRD กำหนดเป็น Controlled Release 1; หลังมี Evaluation การแก้ข้อมูลที่กระทบคะแนนโดยไม่มี revision จะทำให้ผลไม่ตรวจสอบย้อนกลับ |
| `US-DOC-001`; `FR-DOC-001..002`; `TRC-006` | 06 — อัปโหลดเอกสารผู้สมัครและเก็บ Binary ใน Private Storage | Must have | เอกสารเป็นข้อมูลประกอบการประเมิน; metadata/checksum และ private storage จำเป็นต่อความครบถ้วนและป้องกันไฟล์เปิดสาธารณะ |
| `US-DOC-002`; `FR-DOC-003..005`; `SEC-010`; `TRC-006` | 06 — Preview/Download เอกสารหลังตรวจสิทธิ์ระดับ Applicant | Must have | ผู้ประเมินต้องดูหลักฐานของรายการที่ตนเป็นเจ้าของ แต่ห้ามเข้าถึงของผู้อื่น; หากไม่มี Core evaluation หรือ data isolation อย่างใดอย่างหนึ่งจะล้มเหลว |
| `US-SEC-004`; `FR-DOC-006..007`; `RD-038..039`; `SEC-009`; `TRC-019` | 06 — ตรวจชนิด ขนาด Signature และ Malware พร้อม Quarantine | Must have | ไฟล์อัปโหลดเป็น trust boundary; หากไม่มีไฟล์ปลอม/มัลแวร์อาจถูกเผยแพร่ผ่านระบบ จึงเลื่อนไม่ได้โดยไม่เพิ่มความเสี่ยง Security |
| `US-CRI-001`; `FR-CRI-001..004`, `FR-CRI-010..011`; `RD-012..014`, `RD-047`; `TRC-007` | 07 — สร้างชุดเกณฑ์ คะแนน และ Outcome Fields สำหรับรอบทุน | Must have | ไม่มีเกณฑ์จะกรอก/ตรวจคะแนนไม่ได้ และการแยก Amount/Comment ออกจาก 100 คะแนนจำเป็นต่อความถูกต้องของสูตร |
| `US-CRI-002`; `FR-CRI-005..006`; `TRC-007` | 07 — Validate และ Activate Criteria Version | Must have | การเปิดรอบและสร้าง Evaluation พึ่ง Active Criteria ที่คะแนนเต็มและกฎครบ; หากขาดอาจ Submit ผลจากเกณฑ์ไม่สมบูรณ์ |
| `US-CRI-003`; `FR-CRI-007..009`, `FR-CRI-013`; `RD-012`, `RD-014`; `TRC-007` | 07 — ล็อกเกณฑ์ที่ใช้งานและสร้าง Version ใหม่ | Must have | ป้องกันการเปลี่ยนสูตรย้อนหลังหลังมี Draft; Evaluation และการคำนวณใหม่พึ่ง version snapshot เดิมเพื่อรักษา Data Integrity |
| `FR-COD-001`; `RD-046` | 07 — จัดการ Code List แบบมี Version และ Audit | Must have | Release 1 ยืนยันให้ค่ามาตรฐานเปลี่ยนได้โดยไม่ทำลายประวัติ; หาก hard-code หรือทับค่าเดิม Import และข้อมูลย้อนหลังอาจตีความต่างกัน |
| `US-SEL-001`; `FR-EVA-001`; `TRC-008` | 08 — ค้นหาผู้สมัครในรอบที่เปิด | Must have | เป็นจุดเริ่ม Core Flow ของผู้ประเมิน; หากไม่มีจะเลือกรายการสัมภาษณ์และสร้าง Draft ไม่ได้ |
| `US-SEL-002`; `FR-EVA-001..006`; `RD-001..005`; `TRC-008` | 08 — เลือกผู้สมัครและสร้าง Evaluation Draft ไม่ซ้ำ สูงสุด 3 คน | Must have | หากไม่บังคับ owner/จำนวน/transaction จะเกิดผู้ประเมินซ้ำหรือเกิน 3 ทำให้สูตรและสถานะผิด; Draft ทั้งหมดพึ่ง Feature นี้ |
| `US-DRF-001`; `FR-EVA-007`; `TRC-009` | 09 — แสดงข้อมูล ผู้สมัคร เอกสาร ประวัติ และเกณฑ์ในหน้าประเมิน | Must have | ผู้ประเมินต้องเห็นข้อมูลที่ได้รับสิทธิ์ก่อนตัดสินคะแนน; หากไม่มี Core Flow ต้องกลับไปใช้ไฟล์ภายนอกและไม่บรรลุเป้าหมายระบบ |
| `US-DRF-002`; `FR-EVA-008`; `FR-SCO-015`; `RD-013`, `RD-047`; `TRC-009` | 09 — กรอกคะแนน ความคิดเห็น และคำแนะนำภายใต้ Validation | Must have | คะแนนรายเกณฑ์เป็น input ของผลสรุป; การไม่ตรวจช่วง/เหตุผล/เพดานจะทำให้คะแนนหรือ Amount ผิดกฎ |
| `US-DRF-003`; `FR-EVA-009`; `TRC-009` | 09 — Manual Save และกลับมาแก้ Draft | Must have | การประเมินอาจทำหลายช่วง; หากบันทึก Draft ไม่ได้ ผู้ใช้เสี่ยงสูญข้อมูลและไม่สามารถทำ Core Flow ต่อเนื่องจน Submit |
| `US-SUB-001`; `FR-EVA-010`; `TRC-010` | 10 — Review คะแนน ความคิดเห็น Outcome และยอดรวมก่อนส่ง | Must have | เป็นด่านตรวจความครบถ้วนก่อนข้อมูลเข้าสูตรคำนวณ; หากไม่มีผู้ประเมินอาจ Submit ค่าผิดโดยไม่เห็นผลรวมที่จะใช้ |
| `US-SUB-002`; `FR-EVA-011..013`; `TRC-011` | 10 — ยืนยัน Submit และล็อกผลประเมิน | Must have | หากไม่มีผล `SUBMITTED` คะแนนจะไม่เข้าสู่ Result Summary และ Export; การล็อกหลังส่งป้องกันผลเปลี่ยนโดยไม่มีประวัติ |
| `US-SUB-003`, `US-EVA-010`; `FR-EVA-015`, SRS §12 `FR-EVA-017`; `RD-008`; `TRC-003`, `TRC-009` | 10 — ขอ อนุมัติ และ Reopen Submitted Evaluation พร้อม Immutable Revision | Must have | PRD ระบุ Reopen แบบควบคุมเป็น Release 1 และต้องรักษาหลักฐานเดิม; จึงยกระดับจาก Should ใน User Story เพื่อป้องกันการแก้คะแนนที่ตรวจสอบไม่ได้ |
| `US-SCR-001`; `FR-SCO-001..004`; `RD-010..011`; `TRC-012` | 11 — คำนวณคะแนนรวมรายผู้ประเมินจาก Embedded Points | Must have | Result Summary พึ่งผลรวม 10 เกณฑ์ที่ไม่คูณน้ำหนักซ้ำ; หากผิดจะทำให้คะแนนและรายงานทุกช่องทางผิด |
| `US-SCR-002`; `FR-SCO-005..006`, `FR-SCO-008..010`; `RD-004`, `RD-006`, `RD-010..011`; `TRC-012` | 11 — สร้างคะแนนสรุปเมื่อมี Submitted ครบ 2 คน | Must have | เป็นผลลัพธ์หลักของ SEMS; หากไม่มี Core Flow ไม่สามารถตัดสินสถานะ Minimum Complete ปิดรอบ หรือ Export คะแนนสรุป |
| `US-SCR-003`; `FR-SCO-007`, `FR-SCO-011..012`; `RD-005`, `RD-010..011`; `TRC-013` | 11 — คำนวณใหม่เมื่อผู้ประเมินคนที่ 3 Submit | Must have | PRD กำหนดรองรับ 2–3 คน; หากไม่คำนวณใหม่ Dashboard/Report จะค้างที่ผล 2 คนและไม่ตรงฐานข้อมูล |
| `US-CLS-001`, `US-RND-004`; `FR-RND-006..008`, `FR-RND-010`; `RD-007`; `TRC-003`, `TRC-014` | 12 — ตรวจความครบถ้วนและปิดรอบแบบ Controlled Close | Must have | การปิดรอบกำหนด Final/Closed Incomplete; หากไม่มี warning, confirmation และ reason อาจสร้าง Final Score จากข้อมูลไม่ครบ |
| `US-CLS-002`; `FR-SCO-009..012`; `RD-006..008`; `TRC-014` | 12 — กำหนด Finalized หรือ Closed Incomplete หลังปิดรอบ | Must have | Dashboard และรายงานพึ่งสถานะ/Final Score เดียวกัน; ผู้สมัครที่ Submitted ต่ำกว่า 2 ต้องไม่มี Final Score เพื่อรักษาความถูกต้อง |
| `US-RND-004`; `FR-RND-011`; `RD-048..049`; `TRC-003`, `TRC-016` | 12 — Exceptional Round Reopen และสร้าง Final Snapshot ทดแทนแบบ Superseded | Must have | PRD ระบุเป็น Controlled Release 1; หากเขียนทับ Final เดิมจะสูญหลักฐานและไม่สามารถ Audit การแก้ผลหลังปิดรอบ |
| `US-DSH-001`; `FR-DSH-001..003`; `TRC-015` | 13 — Dashboard ภาพรวม Submitted count และสถานะผู้สมัคร | Must have | Proposal ระบุ Simple Dashboard เป็นฟังก์ชันหลัก; Admin ต้องติดตามความครบก่อนปิดรอบและค่าต้องใช้ Submitted เท่านั้น |
| `US-DSH-002`; `FR-RPT-001..002`; `TRC-015` | 13 — กรองและเจาะดูรายการจาก Dashboard | Must have | หากดูได้เพียงยอดรวม Admin จะระบุผู้สมัครที่ค้างหรือผิดสถานะเพื่อดำเนินการก่อน Close ไม่ได้ |
| `US-RPT-001`; `FR-RPT-003..006`; `RD-021`; `TRC-016` | 14 — ส่งออก Excel/CSV ที่ตรง Result Summary | Must have | Export เป็นปลายทาง Core Flow และวัตถุประสงค์ส่งมอบ; หากไม่มีหรือค่าต่างจาก DB กระบวนการประเมินไม่สามารถนำผลไปใช้ |
| `US-RPT-002`; `FR-RPT-007..008`; `RD-022`; `TRC-016`, `TRC-017` | 14 — จำกัด PII และบันทึก Audit ทุก Export | Must have | รายงานมีข้อมูลอ่อนไหว; permission, masking และ audit จำเป็นต่อ Privacy และการตรวจผู้ส่งออกย้อนหลัง |
| `US-RPT-003`; `FR-RPT-010`; `RD-021..022`, `RD-031..032`, `RD-049`; `TRC-016` | 14 — Report profiles, Interim export และ Immutable Final Snapshot | Must have | Release 1 ยืนยันโปรไฟล์ข้อมูลและอายุไฟล์; Final ต้องไม่ถูกเขียนทับเพื่อให้รายงานหลัง Reopen ตรวจสอบย้อนกลับได้ |
| `FR-AUD-001..004`; `SEC-012`; `TRC-017` | 15 — Audit Trail แบบ Append-only และหน้าค้นหาพื้นฐาน | Must have | การเปลี่ยนผู้ใช้ รอบ Import คะแนน Submit Reopen Close และ Export ต้องตอบได้ว่าใครทำอะไรเมื่อใด; หากไม่มี Security/Data Integrity controls ตรวจสอบไม่ได้ |
| `US-DAT-005`; `NFR-SEC-010`; `RD-016`, `RD-029`; `TRC-018` | 16 — Data minimization และการปฏิเสธ National ID ตลอด Core Flow | Must have | Release 1 ไม่มี lawful/security approval ให้ใช้ National ID; การบล็อกทั้ง Import, schema, UI, export, log และ test ป้องกัน PII เกินจำเป็น |
| `US-DAT-005`; `FR-IMP-017`; `RD-019`, `RD-028` | 16 — กำหนด Required-before-evaluation ตามรอบ/ประเภททุน | Must have | ป้องกันสร้าง Evaluation จากข้อมูลสำคัญที่ขาด และให้ปรับกฎตาม Criteria ได้โดยไม่แก้โค้ด; คะแนนจึงอ้างข้อมูลครบตามรอบ |
| `NFR-RET-001`; `RD-030..033`; `TRC-020` | 16 — Retention, Legal Hold และ Secure Deletion | Must have | Core records/Audit/Final snapshot ต้องเก็บตามช่วงที่ยืนยันและลบอย่างควบคุม; หากไม่มีอาจสูญหลักฐานหรือเก็บ PII เกินกำหนด |
| `NFR-BCP-001`; `RD-041`; `TRC-020` | 16 — Backup, Restore Test และ RPO/RTO | Must have | ข้อมูลคะแนน เอกสาร และ Audit สูญหายแล้วสร้างใหม่อย่างเชื่อถือไม่ได้; backup ที่ restore ไม่ได้ทำให้ Data Integrity และความต่อเนื่องล้มเหลว |
| `NFR-CAP-001`; `RD-040`; `TRC-020` | 16 — Capacity/load-test baseline และบันทึกผลวัดจริง | Must have | Release 1 ต้องออกแบบ/ทดสอบตามเป้าหมายที่ยืนยันเพื่อไม่ให้ Core Flow ล้มภายใต้ปริมาณใช้งาน; ห้ามอ้างว่าเป็นผลวัดจนมีหลักฐานจริง |
| `US-SEL-003`, `US-EVA-010`; `FR-EVA-014`, SRS §12 `FR-EVA-018`; `RD-009`; `TRC-009` | 08 — ยกเลิก Draft แบบ Soft Cancel และคืน evaluator slot | Should have | ช่วยแก้การเลือกผิดและลดงาน Admin แต่ Core Flow ปกติยังเลือก บันทึก และ Submit ได้; คง Priority เดิมของ User Story แม้ SRS ระบุ Must จนกว่าจะยืนยันความขัดแย้ง |
| `US-AUTH-003` Optional Note | 01 — Full KKU Logout | Could have | SEMS logout ยกเลิก Session ภายในได้ครบด้านความปลอดภัยแล้ว; การออกจากทุกบริการ KKU ทำได้เฉพาะเมื่อผู้ให้บริการรองรับและผู้ใช้ยืนยัน |
| `US-RPT-003`; `RD-021`; `FR-RPT-006` | 14 — รวมไฟล์ CSV สองไฟล์เป็น ZIP | Could have | CSV สองไฟล์ส่งมอบ Core Report ได้อยู่แล้ว และ Decision ระบุ ZIP ว่า optional packaging; ไม่มีผลต่อคะแนนหรือข้อมูลในไฟล์ |
| `FR-CRI-012`; Proposal §5.4.2 | 07 — คัดลอกเกณฑ์จากรอบเดิมเป็น Draft | Could have | ลดงานตั้งค่าเกณฑ์ แต่ Admin ยังสร้าง Criteria Set ใหม่ได้ด้วย Core Feature และ SRS ระบุ Nice to have |
| `FR-RPT-009`; Proposal §5.2.11, §5.4.2 | 14 — PDF Export, Custom Template และรูปแบบรายงานเสริม | Could have | Excel/CSV เป็นรูปแบบส่งมอบหลักแล้ว; Proposal และ SRS ระบุ PDF/Custom Template เป็น Optional และไม่มีแล้ว Core acceptance ยังผ่าน |
| SRS §9 ข้อ 8; Proposal §5.4.2 | 15 — Detailed Audit Viewer และ Advanced Audit Search | Could have | Append-only Audit กับหน้าค้นหาพื้นฐานยังรองรับการตรวจเหตุการณ์หลัก; มุมมองละเอียดเป็น Optional UX สำหรับสืบค้นเร็วขึ้น |
| `US-DRF-003` Optional Note; Proposal §5.4.2 | 09 — Autosave ระหว่างกรอกคะแนน | Could have | Manual Save เป็น Core และรองรับกลับมาแก้ Draft แล้ว; Autosave ลดโอกาสลืมบันทึกแต่ไม่เปลี่ยน Business Rule |
| Proposal §5.4.2 | 17 — Notification ภายในระบบ | Could have | ผู้ใช้ยังติดตามงานผ่าน Dashboard/สถานะได้; Proposal ระบุให้ทำเมื่อมีเวลาและไม่มี Feature หลักพึ่งพา Notification |
| Proposal §5.4.2 | 17 — Advanced Search | Could have | การค้นหา/กรองพื้นฐานใน User Stories รองรับ Core Flow แล้ว; Advanced Search เพิ่มความเร็วในการหาเคสแต่ไม่บล็อกการประเมิน |
| Proposal §5.4.2 | 17 — หมายเหตุภายในสำหรับ Admin | Could have | Admin ยังจัดการผู้สมัครและตรวจ Audit ได้โดยไม่มีช่องหมายเหตุเสริม; Proposal จัดเป็นฟังก์ชันเมื่อมีเวลา |
| PRD Out of Scope; Proposal §5.1.2, §5.2.1 | 18 — จัดการหรือจัดเก็บรหัสผ่าน KKU ใน SEMS | Won't have | KKU SSO เป็นผู้ยืนยันรหัสผ่านและ SEMS ต้องไม่รับ/เก็บรหัสผ่าน; การทำ Feature นี้ซ้ำระบบกลางและเพิ่มความเสี่ยง credential |
| Proposal §5.3 ข้อ 1 | 18 — ระบบสมัครทุนออนไลน์สำหรับนักศึกษา | Won't have | SEMS เริ่มจากข้อมูลที่งานทุนนำเข้า ไม่ได้ครอบคลุมการรับใบสมัคร; Core Flow ฝั่ง Admin/Evaluator ยังทำงานครบโดยไม่มี portal สมัครทุน |
| Proposal §5.3 ข้อ 2 | 18 — การอนุมัติทุนขั้นสุดท้ายระดับนโยบาย/คณะกรรมการ | Won't have | SEMS คำนวณและส่งออกรายงานเพื่อใช้ประกอบการตัดสินใจ แต่ไม่แทนอำนาจอนุมัติของคณะกรรมการ |
| Proposal §5.3 ข้อ 3 | 18 — ประกาศผลทุนแก่ผู้สมัครโดยตรง | Won't have | ผู้สมัครไม่ได้เป็นผู้ใช้ SEMS ในโครงการนี้; ระบบส่งมอบผลผ่านรายงานให้หน่วยงานดำเนินการต่อ |
| PRD Out of Scope; Proposal §5.3 ข้อ 4 | 18 — โอนเงินทุนหรือจัดการทางการเงิน | Won't have | วัตถุประสงค์สิ้นสุดที่การประเมินและ Export; ธุรกรรมการเงินต้องใช้ขอบเขตและการควบคุมอีกระบบหนึ่ง |
| PRD Out of Scope; Proposal §5.3 ข้อ 5 | 18 — เชื่อมตรงหรือแทนฐานข้อมูลทะเบียน/ระบบทุนกลาง | Won't have | Release 1 ใช้ไฟล์ Import และไม่แทน Source System กลาง; direct integration ต้องมีข้อตกลง interface และ scope แยก |
| Proposal §5.3 ข้อ 6; `RD-008`, `RD-027` | 18 — แก้ผลหลัง Submit โดยไม่มีการอนุมัติ/ประวัติ | Won't have | ขัดกับ Controlled Correction/Reopen และทำลาย Audit/Data Integrity; Release 1 อนุญาตเฉพาะกระบวนการควบคุมที่เก็บ revision |
| Proposal §5.3 ข้อ 7 | 18 — ให้ผู้สมัครเข้าสู่ SEMS โดยตรง | Won't have | บทบาทที่ยืนยันมีเพียง Admin/Evaluator และข้อมูลผู้สมัครเข้าทาง Import; การเพิ่ม applicant identity/consent flow เป็น scope ใหม่ |
| PRD Out of Scope; Proposal §5.3 ข้อ 8 | 18 — Native Mobile Application | Won't have | SEMS เป็น Web Application และ SRS รองรับ Browser; Native app ต้องมี codebase, release และ security review เพิ่มนอก Release 1 |
| Proposal §5.3 ข้อ 9; `FR-DOC-002` | 18 — เก็บ Binary Document ใน PostgreSQL | Won't have | แบบที่ยืนยันใช้ Private File/Object Storage และเก็บ metadata ใน DB; การเก็บ Binary ใน DB ขัดข้อกำหนด storage ปัจจุบัน |
| Proposal §5.3 ข้อ 10; SRS §3.6 `FR-EVA-018` | 18 — จัดคิว/ห้องสัมภาษณ์ Zoom หรือควบคุมประชุมออนไลน์ | Won't have | SEMS รองรับการเลือกผู้สมัครที่กำลังสัมภาษณ์ ไม่ได้จัดการการประชุม; ไม่มีส่วนนี้ Core evaluation ยังครบ |
| Proposal §5.3 ข้อ 11 | 18 — มอบหมายผู้สมัครให้อาจารย์ล่วงหน้า | Won't have | Workflow ที่ยืนยันให้อาจารย์ค้นหาและเลือกผู้สมัครเองพร้อมเพดาน 3 คน; pre-assignment เป็น workflow คนละแบบ |
| PRD Out of Scope; `US-DAT-005`; `RD-016`, `RD-029` | 18 — รองรับ National ID ใน Release 1 | Won't have | ระบุชัดว่า Out of Scope จนมี lawful-need และ security approval แยก; Release 1 ต้องปฏิเสธแทนการจัดเก็บหรือใช้เป็น key |
| `US-IMP-001` Optional/Out-of-Scope Note | 18 — Import ไฟล์ Legacy `.xls` | Won't have | Release 1 รับเฉพาะ `.xlsx`/`.csv`; การเพิ่ม parser `.xls` ไม่จำเป็นต่อ pipeline ที่ยืนยันและไม่มีหลักฐานว่าเป็น Core acceptance |

## 6. สรุปจำนวน Feature

| กลุ่ม | จำนวน Feature | สัดส่วนโดยประมาณ |
| :--- | ---: | ---: |
| Must have | 48 | 66.7% |
| Should have | 1 | 1.4% |
| Could have | 9 | 12.5% |
| Won't have | 14 | 19.4% |
| **รวม** | **72** | **100.0%** |

Must have มีสัดส่วนสูงเพราะเอกสารต้นทางแยก Core Flow เป็น Story รายขั้น และกำหนด Security, Privacy, Audit, Data Integrity, Retention และ Recovery เป็น Release 1 requirements ที่เลื่อนไม่ได้ การทบทวนซ้ำไม่พบหลักฐานรองรับให้ลดรายการเหล่านี้เพียงเพื่อทำให้สัดส่วนสมดุล

## 7. การเปลี่ยน Priority จาก User Stories

| Story ID | Priority เดิม | กลุ่มในเอกสารนี้ | เหตุผล |
| :--- | :---: | :---: | :--- |
| `US-RND-003` | Should have | Must have | PRD Core Features ระบุการปิด/จัดเก็บรอบ และ Controlled Release 1 ระบุว่า Archived เป็น read-only/reopen ไม่ได้; การ Archive จึงเป็น lifecycle/data-integrity control ของ Release 1 |
| `US-SUB-003` | Should have | Must have | PRD ระบุ Controlled Evaluation Reopen, independent approval และ immutable revision เป็นความสามารถแบบควบคุมใน Release 1; SRS/RD-008 ยืนยันกฎเดียวกัน |

`US-SEL-003` คง **Should have** ตาม User Stories แม้ `FR-EVA-014`/`FR-EVA-018` ใน SRS ระบุ Must have เพราะ PRD ไม่ระบุ Cancel Draft เป็น Core/Controlled Feature โดยตรง ความขัดแย้งนี้ต้องให้ผู้มีอำนาจยืนยันก่อนเปลี่ยน Priority

## 8. ข้อสังเกตและรายการที่ต้องยืนยัน

1. Requirement Baseline ทั้งชุดยังเป็น **Pending Formal Approval**; เอกสารนี้จึงห้ามใช้แทน Approval Record
2. Stakeholder ควรยืนยัน Priority ของ Cancel Draft (`US-SEL-003` Should เทียบกับ SRS Must) ให้ตรงกันใน Source Documents
3. `TRC-004` ยังระบุ “DB key open” แต่ `RD-015`, `RD-024..025` ยืนยัน key `(round,type,student)` แล้ว; Traceability Matrix ควรแก้สถานะในรอบปรับ baseline ถัดไป
4. `TRC-017` ระบุ Audit retention ว่า open แต่ `RD-030` ยืนยัน retention หกปีแล้ว; ต้องซิงก์สถานะโดยไม่เปลี่ยนมติ
5. SRS ใช้ `FR-EVA-017` และ `FR-EVA-018` ซ้ำระหว่าง §3.6 กับ §12 โดยมีความหมายต่างกัน; ตารางนี้ใส่เลข Section เพื่อแยกชั่วคราว แต่ต้องแก้ ID ให้ไม่ซ้ำก่อนทำ row-level traceability
6. SRS ยังแสดง `FR-CRI-004` และ `FR-EVA-012` เป็น `Open` ขณะที่ Decision Register ระบุว่าไม่มี Critical/High Release 1 decision ค้าง; ต้องตรวจว่าเป็นสถานะเอกสารตกค้างหรือยังต้องมีมติ
7. ชื่อผู้อนุมัติ วันที่ ลายเซ็น ผู้รับผิดชอบ production และผลวัดจริงของ `RD-040`/`RD-045` ยังไม่มีหลักฐาน จึงไม่กล่าวอ้างว่าอนุมัติหรือบรรลุผลแล้ว
8. National ID ปรากฏสองมุมที่ไม่ขัดกัน: การ **บังคับไม่ให้ National ID เข้าสู่ Core Flow** เป็น Must security/privacy control ส่วน Feature **รองรับ National ID** เป็น Won't have ใน Release 1

## 9. แหล่งอ้างอิง

เรียงตามลำดับ Source of Truth ที่ใช้ในเอกสารนี้:

1. [SEMS Product Requirements Document](./PRD/SEMS-PRD.md)
2. [SEMS — User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)
3. [Software Requirements Specification](./SRS/SEMS-SRS.md)
4. [Requirement Decision Register](./SEMS_Requirement_Decision_Register.md)
5. [Requirement Decision Analysis](./SEMS_Requirement_Decision_Analysis.md)
6. [SEMS Traceability Matrix](./SEMS_Traceability_Matrix.md)
7. [ข้อเสนอโครงการ SEMS](./Proposal/SEMS-project-proposal.md)

## 10. Revision History

| Version | Date | Author | Change |
| :--- | :---: | :--- | :--- |
| v0.1 | 2026-07-25 | SEMS Requirements Team | สร้าง Feature Inventory และจัดกลุ่ม MoSCoW จาก Source Documents ใน Repository สำหรับตรวจทาน Release 1 |

<!-- DOC_NAV_START -->

---

## การนำทางเอกสาร

← ก่อนหน้า: [SEMS — User Stories และ Acceptance Criteria](./User_Stories/SEMS_User_Stories_and_Acceptance_Criteria.md)<br>
↑ หมวดเอกสาร: [📋 Requirements](./README.md)<br>
⌂ หน้าหลัก: [START HERE](../START_HERE.md)<br>
→ ขั้นตอนถัดไป: ตรวจสอบการเชื่อมโยง Feature กับ Requirement และ Test Case ที่ [SEMS Traceability Matrix](./SEMS_Traceability_Matrix.md)

<!-- DOC_NAV_END -->
