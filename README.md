# FlowForge | Supply Chain Process Improvement

**Repair operations · Inventory control · Reverse logistics · Lean analysis · SAP Signavio · BPMN 2.0**

How can a component repair business support more customers while preserving repair quality, inventory traceability and service commitments?

This case study connects process discovery to an improvement business case: map the current operation, identify waste and capacity constraints, compare redesign options, and define how a pilot would demonstrate value. It covers request intake, spare allocation, workshop repair, external repair, dispatch, returns and daily reconciliation.

**[Business case](docs/business-case.md) · [AS-IS / TO-BE gallery](docs/model-gallery.md) · [Quantitative analysis](docs/quantitative-analysis.md) · [Redesign decisions](docs/redesign.md) · [繁體中文](README.zh-TW.md)**

![Supply chain improvement: from fragmented records to controlled fulfilment](docs/assets/case-overview.svg)

## My contribution

I participated in **process analysis, AS-IS and TO-BE BPMN modelling, improvement design, quantitative analysis and report preparation** in a University of Queensland BISM7216 team project. This repository presents that work as a professional portfolio case, with reproducible calculations and navigable model evidence.

**Context:** fictional academic case, October 2026. The redesigned process is a proposal. Financial figures are scenario estimates of labour effort or capacity value; no implementation, achieved savings or production performance is claimed.

## What I can bring to an operations or business analyst role

| Capability | Application in this project | Reviewable evidence |
| --- | --- | --- |
| Supply chain process discovery | Connect information, physical parts and responsibility across repair, warehouse and logistics roles | [16 BPMN diagram previews](docs/model-gallery.md), [AS-IS XML](models/flowforge-as-is.bpmn), [TO-BE XML](models/flowforge-to-be.bpmn) |
| Lean and root cause analysis | Apply all eight waste categories; distinguish symptoms, required controls and causal hypotheses | [Five-issue register and root cause analysis](docs/business-case.md) |
| Quantitative problem solving | Reconcile route volumes, estimate activity cost, examine repair paths and challenge capacity assumptions | [Formula walkthrough](docs/quantitative-analysis.md), [reproducible scenarios](analysis/results.csv) |
| Inventory and reverse logistics design | Verify and reserve stock before shipping outputs; retain return identity, traceability and exception ownership | [R2, R4 and R5](docs/redesign.md) |
| Practical process redesign | Link seven changes to issues, heuristics, BPMN locations and acceptance conditions | [Redesign traceability](docs/redesign.md) |
| Measurement and implementation planning | Define event data, operational owners, quality guardrails and a phased pilot | [KPI and pilot plan](docs/measurement-plan.md) |

## Three findings that shaped the recommendation

| Finding | Analysis | Decision |
| --- | --- | --- |
| Repeated dispatch recording consumes administrative capacity | The selected spare/interstate cohort generates **296 IM minutes**, equivalent to **AU$740** at the case labour rate | Capture the actual handover once and reuse verified data for required reports; retain reconciliation and failure recovery |
| Repair escalation has a material, bounded workload | The full-repeat scenario gives **74.40 minutes** from initial technical testing to tray placement and **AU$1,417.92** in selected post-failure effort per cohort | Reuse sufficient diagnostic evidence, with full-diagnostic fallback and mandatory final tests |
| Inventory automation can add more work than it removes | With the stated control-reduction and volume assumptions, additional scans break even at about **13.15 seconds** each | Start at high-risk movements and measure overhead before reducing physical controls |

These figures have different scopes and must not be added together. The cohort is an analytical allocation of 160 arrivals, not proven daily completion capacity. [See assumptions and calculations](docs/quantitative-analysis.md).

## The proposed operating design

| Current friction | Proposed change | Control preserved |
| --- | --- | --- |
| The same dispatch and return information is entered repeatedly | R1 consolidated dispatch capture; R2 verified return-data reuse | Mandatory reports, audit evidence, correction history and output reconciliation |
| Senior intervention can repeat diagnostic work | R3 evidence-based triage | Full diagnostics when needed, final rig test and bounded rebuild/retest |
| Stock and recorded state can disagree | R4 capture at the point of work; R5 physical verification before shipping outputs | Reservation, part/location linkage, discrepancy ownership and manual fallback |
| Intake depends on matching documents and late scope checks | R6 structured intake and earlier scope validation | Required references, agreed record authority and human clarification |
| Urgent changes are reviewed late in the day | R7 review on receipt against the existing case | Service-window rules, technical authority and completed shipment history |

The design improves how work is captured and coordinated while retaining necessary repair assurance and service controls. [Explore the complete rationale](docs/redesign.md).

## Review in five minutes

1. Read the [business case](docs/business-case.md) for the problem, priorities and root causes.
2. Compare the [AS-IS and TO-BE diagrams](docs/model-gallery.md), especially stock verification, repair escalation and dispatch reporting.
3. Challenge the [scenario assumptions](docs/quantitative-analysis.md) and inspect the [pilot acceptance conditions](docs/measurement-plan.md).

To reproduce the public numerical outputs and model inventory with Python 3.10+ and its standard library:

```bash
git clone https://github.com/1121eason/UQxFlowForge-SupplyChainImprovement.git
cd UQxFlowForge-SupplyChainImprovement
python3 scripts/calculate_scenarios.py --check
python3 scripts/inspect_models.py --check
```

The checks compare calculations and limited XML integrity results with committed evidence. They do not execute the BPMN or replace native Signavio convention checks. [Evidence and limitations](docs/evidence/README.md).

## Repository guide

| Location | Contents |
| --- | --- |
| [Business case](docs/business-case.md) | Lean analysis, issue prioritisation and root cause reasoning |
| [Quantitative analysis](docs/quantitative-analysis.md) | Units, formulas, sensitivities and benefit boundaries |
| [Redesign](docs/redesign.md) | R1-R7, before/after choices, responsibilities and model traceability |
| [Measurement plan](docs/measurement-plan.md) | KPIs, data requirements, pilot stages and acceptance |
| [Model gallery](docs/model-gallery.md) | All eight diagrams from each supplied model |
| [Interview discussion](docs/interview-guide.md) | A concise walkthrough and questions the analysis can support |
| `models/`, `analysis/`, `scripts/` | BPMN source, scenario inputs/results and reproduction tools |

**Portfolio:** Yi Cheng Lee (Eason) · Team project, University of Queensland. The case and submitted analysis are attributed in [provenance](docs/evidence/README.md). Portfolio editing, previews and reproduction tooling were prepared with AI assistance. Assignment materials and personal student identifiers are excluded. See [usage notes](NOTICE.md).
