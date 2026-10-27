# Measurement and pilot plan

[Project overview](../README.md)

The measurement framework translates the seven redesign proposals into ten operational measurement areas, a minimum event-data contract and a six-stage pilot plan. It connects administrative effort, stock visibility, repair quality and service responsiveness to explicit acceptance conditions. The event fields and pilot staging extend the source analysis as proposed implementation design; baseline values, trial thresholds and SLA changes remain subject to operational agreement.

## Outcome measures

| Measure | Definition and denominator | Proposed owner | Evaluation objective |
| --- | --- | --- | --- |
| Manual recording effort | Hands-on capture, verification, reconciliation and failure-recovery minutes / eligible event, separated by route and role | IM / IO | Net administrative capacity released after added verification and recovery work |
| Required-output completeness | Eligible events with all mandatory outputs acknowledged and reconciled / eligible events | IM / IO | Reporting and audit coverage following consolidation of repeated entry |
| Stock-pick discrepancy | Reserved-spare pick attempts with missing or mismatched physical stock / reserved-spare pick attempts | IO | Alignment between physical and recorded stock availability |
| Location accuracy | Independently checked parts with correct ID and location / checked parts | IO | Evidence for a controlled reduction in existing inspection scope |
| Status accuracy | Audited cases whose recorded state matches physical evidence / audited cases | IO | Alignment of recorded case states with physical repair and dispatch events |
| Technical-to-tray time | Tray-placement time minus first technical-test time, by fault/part/route; hands-on time and queue time recorded separately | Senior lead | Repair-path performance following diagnostic reuse on comparable cases |
| Repair quality | Final-test failures, repeat repairs and customer returns, each with its eligible denominator and observation window | Senior lead | Repair assurance alongside any time or capacity improvement |
| Additional capture burden | Added scan/capture seconds by performing role, plus failures and later reconciliation | IO / operational leads | Net value of point-of-work capture after its additional workload |
| Urgent-change review latency | First substantive review minus receipt time; median, upper tail and count received before but reviewed after cut-off | IM | Change responsiveness within the remaining service window |
| Scope and readiness | Out-of-scope physical arrivals / offered requests; false exclusions; receipt-to-document-ready time | IM with client | Prevention of avoidable physical returns while admitting valid requests |

## Minimum event and identity contract

| Data group | Proposed fields | Integrity requirement |
| --- | --- | --- |
| Case identity | CRN, purchase order, work order and line, linked change reference | Submissions correlated to the existing case before another case is created |
| Physical identity | Serial/internal part ID, source location, destination location, reservation reference | Verified physical identity, including legitimate first registration |
| Event | Event ID, event type, occurred-at time, recorded-at time, actor and role | Physical occurrence distinguished from late recording, with duplicate-posting prevention |
| Repair evidence | Test result, fault observation, intervention, reuse decision, final rig result | Evidence linked to the part and repair attempt, with full-diagnostic fallback retained |
| Dispatch evidence | Selected route, consignment, actual handover time and recipient | External repair handover distinguished from customer fulfilment |
| Output/exception | Required output, acknowledgement, error, owner, due date, resolution and correction history | Failed generation remains visible; manual fallback is reconciled |

## Pilot stages and acceptance

| Stage | Proposed work | Acceptance condition |
| --- | --- | --- |
| 1. Baseline definition | Observation of actual work, route mix, execution units, returns and tracking populations; effort measured separately from waiting | Owners agree identifiers, feasible workload and measurement boundaries |
| 2. Record reuse: R1/R2 | Comparison of manual effort and output completeness on eligible dispatch/return events | All mandatory outputs retained; exceptions assigned; lower net effort on comparable work |
| 3. Inventory controls: R4/R5 | Independent physical checks alongside measurement of scan overhead, discrepancies and reservation behaviour | Correct ID/location linkage; no false dispatch or double allocation; measured reduction exceeds added effort |
| 4. Diagnostic reuse: R3 | Senior-approved reuse criteria, comparable fault/part mix and retained mandatory tests | Final tests pass and quality does not deteriorate; review/capture burden included |
| 5. Intake and change control: R6/R7 | Client agreement on record authority and scope, with correlated and reviewed urgent changes | No unjustified exclusions; traceable dispositions; service constraints retained |
| 6. Scale-up assessment | Review of workload, quality, exceptions, cost of change and support burden | Owners accept evidence; SOPs/training updated; controls retired only where justified |

The proposed comparison uses comparable baseline and pilot populations with retained case-mix information. An arrival cohort is distinct from completed daily work. Sample size, duration and performance thresholds require owner agreement; the supplied materials do not establish them. Failed data-quality or required-output checks prevent expansion until outstanding events are reconciled, with the existing control retained.

Source: team report Section 7, PDF pp. 12-13, and state/integration requirements on PDF p. 16. Detailed event fields and staging are supporting project design.
