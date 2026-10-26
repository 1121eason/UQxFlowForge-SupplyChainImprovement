# Quantitative analysis and decision boundaries

[Back to portfolio](../README.md) · [Inputs](../analysis/scenario_inputs.json) · [Calculated results](../analysis/results.csv)

The analysis estimates activity effort from the teaching case and disclosed assumptions. It is not an operational benchmark or a simulation of executable BPMN. All monetary figures are Australian dollars at the case role rates: IM 150/hour, IO 100/hour, Technician 30/hour and Senior Technician 80/hour.

## 1. Reconcile the reference population

Use 160 arrivals as a reference cohort and assume one request per part. Interpret 60% spare allocation, 5% out-of-scope rejection and 35% valid no-spare work as mutually exclusive. Of the valid no-spare population, 40% goes interstate. The shelf-miss share `s` is unknown; 5% is an illustrative input.

| Route | Formula at s = 5% | Expected parts |
| --- | --- | ---: |
| Physically available spare | 160 × 0.60 × 0.95 | 91.2 |
| Interstate handover | 160 × 0.35 × 0.40 + 160 × 0.60 × 0.05 | 27.2 |
| Internal workshop repair, W | 160 × 0.35 × 0.60 | 33.6 |
| Out-of-scope return | 160 × 0.05 | 8.0 |
| Total | Sum of routes | 160.0 |

Fractional results are expected counts. The described spare/interstate dispatch population `D = 118.4`; it remains constant as shelf misses move parts between those two routes. Returns `R` and actual shipments tracked that day `Q` are separate populations with unknown sizes.

**Capacity challenge:** taking 12 minutes of request creation plus 15 minutes of spare searching literally per arrival gives `160 × 27 = 4,320 minutes`, or 72 IM hours. One IM cannot perform this in an assumed eight-hour productive day. Verify execution units, hands-on versus elapsed time, staffing and backlog before treating the arrival cohort as daily throughput. The analysis does not introduce convenient batching to hide this inconsistency.

## 2. Repeated recording and a bounded R1 benefit

Selected baseline dispatch entry consists of one minute of paper-reference copying plus 1.5 minutes of report entry per D event:

```text
Baseline effort = 2.5 × 118.4 = 296 IM minutes
Labour-cost equivalent = 296 × 150/60 = AU$740 per cohort
```

R1 assumes 0.25 minutes of verification per event and the same ten-minute completeness check before and after:

```text
Selected reduction = (2.5D + 10) - (0.25D + 10)
                   = 266.4 IM minutes
                   = AU$666 per cohort
```

At 0.5 verification minutes, the equivalent falls to AU$592. Capture/output failures and their recovery must be deducted during a pilot. This selected estimate excludes any reduction in the unit-sensitive tracking task and prices additional scanning separately.

The AS-IS model also sends 33.6 workshop repairs through dispatch reporting. Extending the boundary to `D + W = 152` gives AU$950 baseline exposure and AU$855 selected R1 capacity value. Those are alternative boundary estimates, not additional benefits.

Return auditing is separate: replacing 30 minutes of duplicate IO entry with 0.5 minutes of output verification gives `29.5R` minutes, or approximately `AU$49.17R`. If that baseline activity is once daily, the estimate becomes AU$49.17 per day. Initial receipt verification and valid new-ID creation remain required. The report's initial return-recording formula also treats the 15-minute unadvised block as inclusive of record creation; measuring that boundary is necessary before operational use.

## 3. Repair escalation, expected time and quality risk

With W = 33.6, 40% initial failures and 30% conditional subsequent failures:

```text
Expected escalations = 33.6 × 0.40 = 13.44
Expected rebuilds = 33.6 × 0.40 × 0.30 = 4.032
```

The full-repeat interpretation uses 39 Senior minutes per escalation and 130 minutes for rebuild/retest. Technician escalation takes three minutes.

| Selected post-failure work | Labour minutes | Cost equivalent |
| --- | ---: | ---: |
| Technician escalation | 40.32 | AU$20.16 |
| Senior repeat work | 524.16 | AU$698.88 |
| Senior rebuild/retest | 524.16 | AU$698.88 |
| Total | 1,088.64 | AU$1,417.92 |

If Senior repeat work is 25 minutes, selected cost is AU$1,167.04. The case does not prove that every escalation repeats 39 minutes of work.

Using a consistent boundary from initial technical testing to tray placement, the three full-repeat paths take 42, 84 and 214 minutes with probabilities 0.60, 0.28 and 0.12:

```text
Expected technical-to-tray time = 0.60(42) + 0.28(84) + 0.12(214)
                                = 74.40 minutes
```

This excludes intake, meetings, queues, transport and dispatch-window waiting. It is not end-to-end lead time or a bottleneck proof.

R3 adds three Senior review minutes per escalation and 0.5 Technician evidence-capture minutes per internal case. Only the share `e` with reusable evidence reduces repeat work from 39 to 25 minutes; failure rates stay unchanged.

| Reuse-eligible share | Net labour-cost equivalent released per cohort |
| --- | ---: |
| 25% | AU$0.56 |
| 50% | AU$63.28 |
| 100% | AU$188.72 |

At e = 50%, expected technical-to-tray time is 73.30 minutes. A rise in conditional subsequent failure to about 32.72% would erase the AU$63.28 economic benefit. This is a stress test, not permission to accept worse repair quality. If the baseline is already 25 minutes, review may add work without a saving.

## 4. Stock visibility and scanning break-even

The daily control cycle is assumed to contain 111.5 IO minutes. It is not all avoidable waste. Let `k` be its reducible share, `V` additional scan events and `δ` added minutes per scan. Keep the shelf-miss rate unchanged and credit only avoided unusable-ticket work:

```text
Selected capacity value = (111.5k - Vδ) × 100/60
                        + (96s × 2) × 150/60
```

For an explicitly hypothetical steady-state day with k = 50%, s = 5% and V = 320:

| Additional time per scan | Selected net equivalent |
| --- | ---: |
| 5 seconds | AU$72.47 |
| 10 seconds | AU$28.03 |
| 15 seconds | -AU$16.42 |

Break-even is about **13.15 seconds per added scan**. This supports selective capture and measurement before reducing physical controls. The illustration prices scans at the IO rate; an actual evaluation must use the performing role. Moving stock verification earlier avoids unusable outputs but does not itself prevent stock discrepancies or remove recovery routing.

## 5. What remains unpriced

Intake, urgent-change effects, actual freight, external fees, software, integration, training, support and implementation costs are not sufficiently specified. No aggregate daily saving, annualised saving, cash ROI or staffing reduction is asserted. The report's weights, route interpretation, stock-miss rates, reuse eligibility and TO-BE times are assumptions or proposed trial inputs.

Run `python3 scripts/calculate_scenarios.py --check` to reproduce the displayed figures and prioritisation sensitivity. The script checks route conservation, probability bounds, unit ranges and known report results, then compares outputs with the committed CSV. It does not establish that the assumed workloads are feasible.

Source: team report Sections 1, 3, 4 and 7, PDF pp. 3-4, 6-9 and 12-13. [Provenance](evidence/README.md).
