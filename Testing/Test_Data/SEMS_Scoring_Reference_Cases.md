# SEMS Scoring Reference Cases

| Metadata | Value |
|---|---|
| Document ID | `SEMS-SCORE-DATA-001` |
| Version | **v0.2** |
| Last Updated | **2026-07-24** |
| Status | **Confirmed Response — Pending Formal Approval** |

กฎ: `EMBEDDED_POINT`; คะแนน option เป็นคะแนนหลังถ่วงน้ำหนักแล้ว, `weight_percent` เป็น metadata และห้ามคูณซ้ำ ใช้ Decimal, Submitted ที่ผู้ประเมินไม่ซ้ำ 2–3 คนเท่านั้น และปัด Applicant Summary สุดท้าย 2 ตำแหน่งแบบ `HALF_UP`

## Criterion Scores

| Case / Evaluator | CRT-01 | CRT-02 | CRT-03 | CRT-04 | CRT-05 | CRT-06 | CRT-07 | CRT-08 | CRT-09 | CRT-10 | Evaluator Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MIN / E1 Submitted | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| MAX / E1 Submitted | 10 | 10 | 10 | 20 | 10 | 10 | 5 | 5 | 10 | 10 | 100 |
| AVG2 / E1 Submitted | 5 | 5 | 10 | 20 | 10 | 5 | 5 | 5 | 10 | 0 | 75 |
| AVG2 / E2 Submitted | 10 | 10 | 10 | 15 | 10 | 10 | 5 | 5 | 5 | 0 | 80 |
| AVG3 / E3 Submitted | 10 | 10 | 10 | 20 | 10 | 10 | 5 | 5 | 10 | 0 | 90 |
| EXCLUDED / E3 Draft | 10 | 10 | 10 | 20 | 10 | 10 | 5 | 5 | 10 | 10 | 100 |
| EXCLUDED / E3 Cancelled | 10 | 10 | 10 | 20 | 10 | 10 | 5 | 5 | 10 | 10 | 100 |

## Expected Summaries

| Case | Eligible Totals | Unrounded Average | Rounded Summary | Expected Applicant Status |
|---|---|---:|---:|---|
| Minimum boundary | 5, 5 | 5 | 5.00 | `MINIMUM_COMPLETE` |
| Maximum boundary | 100, 100 | 100 | 100.00 | `MINIMUM_COMPLETE` |
| Two evaluators | 75, 80 | 77.5 | 77.50 | `MINIMUM_COMPLETE` |
| Third evaluator recalculation | 75, 80, 90 | 81.666666… | 81.67 | `FULLY_COMPLETE` |
| Draft excluded | 75 Submitted, 80 Submitted, 100 Draft | 77.5 | 77.50 | `MINIMUM_COMPLETE` |
| Cancelled excluded | 75 Submitted, 80 Submitted, 100 Cancelled | 77.5 | 77.50 | `MINIMUM_COMPLETE` |

## Calculation Assertions

- Embedded point case `75` remains `75`; multiplying by weight again is a failure.
- Every current required criterion gives minimum total **5**, not 0, because `CRT-04` minimum is 5.
- Criteria version on every score row must match the Evaluation binding; mismatch returns `CRITERION_VERSION_MISMATCH`.
- Criteria Version is locked from the first Evaluation creation, including Draft; every later revision remains bound to that version.
- Custom discretion score is an integer 0–10; a non-standard option needs a reason. Custom Amount and general comments never enter the 100-point total.
- Rounding engine boundary fixture: Decimal totals `80.00` and `80.01` average to `80.005` and must produce `80.01` with `HALF_UP`. This fixture tests the Decimal/rounding function, not the current integer-only option set.

## Revision History

| Version | Date | Author | Change |
|---|---|---|---|
| v0.2 | 2026-07-24 | SEMS QA Team | Confirmed scoring status and added criteria-lock/custom-score/non-scoring assertions. |
| v0.1 | 2026-07-23 | SEMS QA Team | Added provisional min/max, two/three evaluator, exclusion, embedded-point, version and rounding reference cases. |
