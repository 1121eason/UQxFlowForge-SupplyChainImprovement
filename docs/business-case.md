# Business case and process diagnosis

[Project overview](../README.md)

## Business objective and scope

FlowForge is a fictional component repair and resupply business serving a major client. The project evaluates opportunities to release operating capacity for additional customers while preserving existing service, repair assurance and tracking obligations. The diagnosis combines Lean waste analysis, a five-issue register, weighted prioritisation and root cause analysis to establish the rationale for seven redesign proposals.

The case connects four internal roles: Inventory Manager (IM), Inventory Officer (IO), Technician and Senior Technician. External participants are the client, carrier, interstate subcontractor and a distinct on-call recovery repairer. A handover to an external repairer does not mean that a part has been repaired or returned to the client.

The analysis follows parts and information through intake, spare allocation, workshop repair, dispatch, returns and reconciliation. It distinguishes a new request from a return record, a daily control cycle and a recovery case that can remain open across days. These distinctions prevent per-item work from being confused with once-daily activity.

## Lean diagnosis

| Waste | Mechanism in this case | Implication for redesign |
| --- | --- | --- |
| Defects | Failed rig tests, wrong-scope arrivals and physical/record discrepancies create corrective work | Investigate causes and reuse valid evidence while retaining required assurance |
| Overproduction | Shipping outputs can be prepared for a spare that cannot be found; several representations of the same event are maintained | Verify stock first and agree which records must remain authoritative |
| Waiting | Required request documents arrive separately; service windows and external recovery can delay progress | Measure elapsed dependency and review latency separately from paid labour |
| Non-utilised talent | Skilled roles perform repeated clerical work and may repeat usable diagnostic work | Improve capture and route evidence-sufficient cases appropriately |
| Transportation | Wrong-scope parts and missed-item recovery can require additional movement | Screen scope earlier and improve visibility; retain necessary subcontracting and delivery |
| Inventory | Parts can wait for release or remain in a recorded Open state after completion | Distinguish physical condition, location and case state |
| Motion | Meetings and physical searches require movement between work areas | Measure avoidable movement without treating the whole inspection as waste |
| Extra-processing | Dispatch references and return details are entered repeatedly | Reuse verified information and retain audit outputs, rather than removing the obligation |

Necessary tests, legitimate identity creation and required physical checks are not assumed removable.

## Five issues and prioritisation

Scores use analyst judgement on a 1-5 scale. Base weights are capacity exposure 45%, service/traceability risk 35% and growth capability 20%. The scores communicate priorities, not measured financial returns.

| Issue | Operational problem | Capacity / service / growth | Weighted score | Rank |
| --- | --- | --- | ---: | ---: |
| I-01 Repeated manual record maintenance | Dispatch and return information is copied between records | 5 / 3 / 5 | 4.30 | 1 |
| I-02 Escalation and repeat effort | Initial test failure adds Senior work and possible rebuilding | 4 / 5 / 3 | 4.15 | 2 |
| I-03 Weak part and status visibility | Physical stock and recorded state can disagree | 3 / 5 / 4 | 3.90 | 3 |
| I-04 Intake and scope delays | Document dependencies and late checks delay valid work or create returns | 2 / 3 / 3 | 2.55 | 5 |
| I-05 Late urgent-change review | Changes may be reviewed after the remaining service opportunity | 2 / 4 / 3 | 2.90 | 4 |

The top-three set remains I-01/I-02/I-03 under service-led weights of 30%/50%/20% and growth-led weights of 35%/25%/40%; first place changes. The sensitivity analysis supports a consistent priority group while showing that the ordering depends on judgement weights and uncertain operational inputs. [Priority sensitivity results](../analysis/results.csv).

I-01 is the starting point because repeated capture spans several stages and constrains scalable reporting. I-02 has explicit failure rates and activity times but an uncertain preventable share. I-03 has strong traceability implications even though the stock-miss rate is unknown. Targeted intake and urgent-change controls remain necessary; integration does not automatically solve I-04 or I-05.

## Root cause reasoning for I-01

**Effect:** repeated manual record maintenance and reconciliation.

| Category | Case-supported mechanism | Hypothesis requiring investigation | Design response |
| --- | --- | --- | --- |
| Process | Completion of a transaction triggers further record entry | Overlapping fields could be captured once and reused safely | R1/R2 controlled reuse with reconciliation |
| People | IM and IO perform recurring record work | Recording responsibility may be separated from the role performing the physical event | R4 event ownership at the point of work |
| Policies | A parallel paper record supports an end-of-day check | The control outcome may be achievable without separate human entry | Agree record authority and retirement criteria before removing duplicate capture |
| Systems | The described workflow uses manual operations across repositories | Verified fields and completion events may not be reused consistently | Validate mappings, acknowledgements, correction history and failure handling |

The case does not establish employee resistance, missing APIs or incompatible databases. Those explanations must be investigated rather than asserted. The recommendation therefore starts with common identifiers, authoritative event data and accountable exceptions instead of assuming a wholesale system replacement.

## Recommended operating direction

The recommendation is a phased pilot beginning with controlled record capture and reuse, followed by inventory visibility and evidence-based repair routing. Physical verification, mandatory tests and contractual service constraints remain in place until the relevant owner has evidence to approve a change. [Redesign decisions](redesign.md) link the seven proposals to process changes; [quantitative analysis](quantitative-analysis.md) defines their estimated benefits and conditions.

Source: team report, Sections 1-6, PDF pp. 3-12; source register and publication treatment in [provenance](evidence/README.md).
