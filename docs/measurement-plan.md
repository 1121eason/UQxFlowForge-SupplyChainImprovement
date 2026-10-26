# Measurement and pilot plan

[Back to portfolio](../README.md)

This plan translates the report's acceptance conditions into a proposed pilot. Data fields and staging below are portfolio elaborations, not an existing implementation or agreed SLA. Establish a feasible observed baseline before forecasting benefits.

## Outcome measures

| Measure | Definition and denominator | Proposed owner | Decision supported |
| --- | --- | --- | --- |
| Manual recording effort | Hands-on capture, verification, reconciliation and failure-recovery minutes / eligible event, separated by route and role | IM / IO | Does R1/R2 release net capacity after added work? |
| Required-output completeness | Eligible events with all mandatory outputs acknowledged and reconciled / eligible events | IM / IO | Can repeated entry be retired without losing audit/report coverage? |
| Stock-pick discrepancy | Reserved-spare pick attempts with missing or mismatched physical stock / reserved-spare pick attempts | IO | Are physical and recorded availability aligned? |
| Location accuracy | Independently checked parts with correct ID and location / checked parts | IO | Is there evidence to reduce existing inspection scope? |
| Status accuracy | Audited cases whose recorded state matches physical evidence / audited cases | IO | Are Open, repair-complete, external and dispatched states meaningful? |
| Technical-to-tray time | Tray-placement time minus first technical-test time, by fault/part/route; hands-on time and queue time recorded separately | Senior lead | Does diagnostic reuse improve comparable repair work? |
| Repair quality | Final-test failures, repeat repairs and customer returns, each with its eligible denominator and observation window | Senior lead | Is any speed/capacity gain obtained without worse quality? |
| Additional capture burden | Added scan/capture seconds by performing role, plus failures and later reconciliation | IO / operational leads | Is R4 still worthwhile after its new work? |
| Urgent-change review latency | First substantive review minus receipt time; median, upper tail and count received before but reviewed after cut-off | IM | Does R7 preserve a usable service opportunity? |
| Scope and readiness | Out-of-scope physical arrivals / offered requests; false exclusions; receipt-to-document-ready time | IM with client | Does R6 prevent avoidable returns while admitting valid work? |

## Minimum event and identity contract

| Data group | Proposed fields | Integrity requirement |
| --- | --- | --- |
| Case identity | CRN, purchase order, work order and line, linked change reference | Correlate submissions to the existing case before creating another |
| Physical identity | Serial/internal part ID, source location, destination location, reservation reference | Verify actual identity; permit legitimate first registration |
| Event | Event ID, event type, occurred-at time, recorded-at time, actor and role | Distinguish physical occurrence from late recording; prevent duplicate posting |
| Repair evidence | Test result, fault observation, intervention, reuse decision, final rig result | Link evidence to the part and repair attempt; retain full-diagnostic fallback |
| Dispatch evidence | Selected route, consignment, actual handover time and recipient | Keep external repair handover separate from customer fulfilment |
| Output/exception | Required output, acknowledgement, error, owner, due date, resolution and correction history | Failed generation remains visible; manual fallback is reconciled |

## Pilot stages and acceptance

| Stage | Work | Gate before proceeding |
| --- | --- | --- |
| 1. Confirm the baseline | Observe actual work, route mix, execution units, returns and tracking populations; separate effort from waiting | Owners agree identifiers, feasible workload and measurement boundaries |
| 2. Trial R1/R2 with controlled reconciliation | Compare manual effort and output completeness on eligible dispatch/return events | All mandatory outputs retained; exceptions assigned; lower net effort on comparable work |
| 3. Trial R4/R5 at selected transitions | Keep independent physical checks; measure scan overhead, discrepancies and reservation behaviour | Correct ID/location linkage; no false dispatch or double allocation; measured reduction exceeds added effort |
| 4. Trial R3 on eligible repair evidence | Senior approves reuse criteria; compare similar fault/part mix; retain all tests | Final tests pass and quality does not deteriorate; review/capture burden included |
| 5. Agree and trial R6/R7 | Confirm client record authority and scope rules; correlate and review urgent changes | No unjustified exclusions; traceable dispositions; service constraints retained |
| 6. Decide whether to extend | Review workload, quality, exceptions, cost of change and support burden | Owners accept evidence; update SOPs/training; retire controls only where justified |

Use comparable baseline and pilot populations, retain case-mix information and do not treat an arrival cohort as completed daily work. Sample size, duration and performance thresholds require owner agreement; the supplied materials do not establish them. If data quality or required outputs fail, retain the existing control and reconcile outstanding events before expansion.

Source: team report Section 7, PDF pp. 12-13, and state/integration requirements on PDF p. 16. Detailed event fields and staging are portfolio additions.
