# Redesign decisions and traceability

[Back to portfolio](../README.md) · [Model gallery](model-gallery.md)

The seven changes form a coordinated operating design. They retain service windows, repair assurance, physical identity, reporting and exception ownership. Automation is proposed behaviour; no working carrier integration or deployed system is evidenced.

| Change | Before → proposed behaviour | Issue / heuristic | TO-BE location | Proposed accountable role and acceptance |
| --- | --- | --- | --- | --- |
| R1 Consolidate dispatch capture | Retype references into parallel records → capture the actual handover once and derive required outputs | I-01; elimination, composition, automation | T4 capture and explicit output-success decision; recovery-record detail in T6 | IM: mandatory outputs reconcile; failures have an owner; no dispatch event before physical handover |
| R2 Reuse verified return information | Re-enter return information for audit/training → reuse verified fields, acknowledge output delivery and repair failures | I-01; elimination, automation | T5 verified audit output and repair/retry/manual alternative | IO: every eligible return retains audit evidence, identity and provenance |
| R3 Triage Senior intervention | Potentially repeat the full diagnostic sequence → review evidence and choose targeted work only when justified | I-02; triage, resource optimisation | T3 evidence gateway, full-diagnostic alternative, final rig test and bounded rebuild/retest | Senior lead: reusable evidence is documented; mandatory tests pass; no deterioration in repeat repairs |
| R4 Capture at the point of work | Reconstruct part location and completion later → record actor, part, case, location and time at selected transitions | I-03; automation, resource optimisation | T2 stock discrepancy; T3 completion; T4 handover; T5 history; T6 reconciliation | Performing role owns capture; IO owns discrepancies; controlled manual capture reconciles after device/label failure |
| R5 Verify stock before outputs | Book/print before checking the shelf → reserve, verify physically, then create route-appropriate outputs | I-03; resequencing | T2 reserved-spare verification before T4 booking | IM/IO: no double allocation; a shelf miss remains an explicit exception and recovery route |
| R6 Structure intake and validate scope | Match separate documents and assess scope late → validate required references and scope earlier under an agreed record-authority rule | I-04; communication, resequencing, automation | T1 authority, legacy evidence, duplicate correlation and clarification paths | IM with client agreement: valid cases are not falsely excluded; already-arrived rejects retain physical-return handling |
| R7 Review changes on receipt | Review after the cut-off → timestamp, correlate and assess each change against the active case and remaining window | I-05; communication, resource optimisation | T7 dispatched/not-dispatched decision and authorised plan/disposition tasks | IM and technical decision-maker: traceable accept/defer/reject outcome; completed shipment history preserved |

## Important design choices

**Separate business states.** Repair complete, ready for dispatch, sent to subcontractor, dispatched, rejected and exception open have different meanings. Reports consume evidence of events; producing a report does not establish that a physical event occurred.

**Give failures visible owners.** Data capture and output generation can fail. The proposal retains correction history, retry or controlled manual output, and reconciliation. T4/T5 draw explicit failure decisions; T6 places some fallback requirements in task documentation. T7 documents version checking and duplicate prevention as implementation requirements. These documented controls are not demonstrated software.

**Preserve repair assurance.** Reuse requires sufficient diagnostic evidence. Otherwise, the full path remains. Mandatory rig tests and rebuild/retest are not removed to make a time estimate look better.

**Separate daily closing from recovery completion.** Daily closing reconciles the day's postings and assigns carry-over. Open external recovery cases remain open until physical receipt and dispatch; a timer or late notice cannot stand in for a returned part.

**Retain operational agreements.** An agreed electronic authority can remove unnecessary document waiting only after client approval. The 3 PM service constraint and discretionary outside-hours treatment remain. Earlier screening after a part arrives cannot recover freight already spent.

## Alternatives considered

| Alternative | Reason for the selected approach |
| --- | --- |
| Remove all physical inspection | Digital capture reliability and discrepancy rates are unmeasured; reduce scope only after a successful pilot |
| Send all work to Seniors or external repairers | Shifts cost and capacity without evidence that it improves the whole system |
| Replace every system at once | Integration requirements and cost are unknown; first validate identifiers, mappings and exception ownership |
| Make one employee's tasks parallel | A diagram cannot create resource capacity; manual work remains constrained by the performing role |
| Remove final tests or the dispatch cut-off | Changes quality or contractual commitments; requires a separate decision and supporting evidence |

## Model comparison rule

Both models have an overview and seven subprocess diagrams, but their decomposition differs. AS-IS returns/history are combined in TO-BE T5; dispatch is consolidated in T4. Some XML IDs are reused for different scopes. Compare business behaviour and R identifiers rather than treating a shared ID as an unchanged activity. [Model review and verification limits](evidence/README.md).

Source: team report Sections 6, 9 and 10, PDF pp. 11-12 and 15-17, checked against the supplied TO-BE XML.
