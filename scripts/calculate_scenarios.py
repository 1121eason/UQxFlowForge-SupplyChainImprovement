#!/usr/bin/env python3
"""Reproduce the case's selected calculations. Python 3.10+, standard library only."""
import argparse
import csv
import io
import json
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fraction(value):
    if not D(0) <= value <= D(1):
        raise ValueError(f"Invalid share: {value}")
    return value


def calculate(p):
    cohort, rates, rec, repair, inv = (
        p['reference_cohort'], p['rates_aud_per_hour'], p['recording_minutes'],
        p['repair'], p['inventory']
    )
    n = cohort['arrivals']
    spare = n * fraction(cohort['allocated_spare_share'])
    rejects = n * fraction(cohort['out_of_scope_share'])
    valid_no_spare = n - spare - rejects
    if n <= 0 or valid_no_spare < 0:
        raise ValueError('Invalid route population')
    s = fraction(cohort['illustrative_shelf_miss_share'])
    external = valid_no_spare * fraction(cohort['interstate_share_of_valid_no_spare'])
    w = valid_no_spare - external
    d = spare + external
    physical_spare, interstate = spare * (1-s), external + spare*s
    if physical_spare + interstate + w + rejects != n:
        raise ValueError('Routes do not conserve the arrival population')
    for role, rate in rates.items():
        if rate <= 0:
            raise ValueError(f'Invalid labour rate for {role}')
    for key in ('IM', 'IO', 'Technician', 'Senior'):
        rates[key] /= D(60)
    rows = []

    def add(metric, scenario, value, unit, scope):
        rows.append([metric, scenario, str(value.quantize(D('.01'), rounding=ROUND_HALF_UP)), unit, scope])

    for name, value in [('available_spares',physical_spare),('interstate_handovers',interstate),
                        ('internal_workshop',w),('out_of_scope',rejects),('route_total',n),
                        ('selected_dispatch_population',d)]:
        add(name, 'reference_shelf_miss_5pct', value, 'expected parts', 'arrival cohort')
    baseline = rec['dispatch_repeated_entry'] * d
    add('dispatch_repeated_entry', 'selected_routes', baseline, 'IM minutes', 'arrival cohort')
    add('dispatch_repeated_entry_cost', 'selected_routes', baseline*rates['IM'], 'AUD', 'arrival cohort')
    add('literal_intake_and_search', '12_plus_15_minutes_per_arrival', n*D(27)/D(60), 'IM hours', 'arrival cohort; feasibility unresolved')
    for verify in rec['r1_verification_scenarios']:
        retained = rec['retained_completeness_check']
        reduction = baseline + retained - (verify*d + retained)
        add('r1_selected_capacity_value', f'verify_{verify}_min', reduction*rates['IM'], 'AUD', 'arrival cohort; before failure recovery')
    add('r1_broader_capacity_value', 'include_internal_repairs_verify_0.25_min',
        (rec['dispatch_repeated_entry']-rec['r1_verification_scenarios'][0])*(d+w)*rates['IM'],
        'AUD', 'alternative boundary; not additive to selected R1')
    add('r2_capacity_value', 'per_return_verification',
        (rec['duplicate_audit_per_return']-rec['r2_output_verification_per_return'])*rates['IO'],
        'AUD per return', 'per-record interpretation; before failure recovery')

    first_fail = fraction(repair['initial_failure_share'])
    second_fail = fraction(repair['conditional_subsequent_failure_share'])
    escalate, rebuild = w*first_fail, w*first_fail*second_fail
    add('escalations', 'reference', escalate, 'expected cases', 'arrival cohort')
    add('rebuilds', 'reference', rebuild, 'expected cases', 'arrival cohort')
    for repeat in repair['senior_repeat_minutes_scenarios']:
        extra = escalate*repair['technician_escalation_minutes']*rates['Technician']
        extra += (escalate*repeat + rebuild*repair['rebuild_plus_retest_minutes'])*rates['Senior']
        add('post_failure_effort_cost', f'senior_repeat_{repeat}_min', extra, 'AUD', 'arrival cohort; not recoverable in full')
    base_time = repair['initial_pass_to_tray_minutes']
    senior_path = base_time + repair['technician_escalation_minutes'] + repair['r3_baseline_repeat_minutes']
    rebuild_path = senior_path + repair['rebuild_plus_retest_minutes']
    expected_time = ((1-first_fail)*base_time + first_fail*(1-second_fail)*senior_path
                     + first_fail*second_fail*rebuild_path)
    add('technical_to_tray', 'full_repeat_baseline', expected_time, 'minutes per internal case', 'excludes queues intake transport dispatch waiting')
    for eligible in repair['r3_reuse_eligible_shares']:
        fraction(eligible)
        released_per_escalation = (repair['r3_baseline_repeat_minutes']-repair['r3_targeted_repeat_minutes'])*eligible-repair['r3_senior_review_minutes']
        net_value = escalate*released_per_escalation*rates['Senior'] - w*repair['r3_technician_capture_minutes']*rates['Technician']
        tag = f'reuse_eligible_{eligible}'
        add('r3_net_capacity_value', tag, net_value, 'AUD', 'arrival cohort; unchanged failure rates')
        add('r3_technical_to_tray', tag, expected_time-first_fail*released_per_escalation+repair['r3_technician_capture_minutes'],
            'minutes per internal case', 'unchanged failure rates')
        if eligible == D('.5'):
            threshold = second_fail + net_value/(escalate*repair['rebuild_plus_retest_minutes']*rates['Senior'])
            add('r3_economic_failure_threshold', tag, threshold*D(100), 'percent', 'stress test; not acceptable quality loss')

    control = inv['daily_io_control_minutes']
    for miss in inv['shelf_miss_scenarios']:
        fraction(miss)
        cost = control*rates['IO'] + spare*miss*inv['shelf_miss_selected_im_minutes']*rates['IM']
        add('inventory_control_and_exception_cost', f'shelf_miss_{miss}', cost, 'AUD', 'hypothetical steady-state day; not all avoidable')
    k = fraction(inv['reducible_control_share'])
    scans = inv['additional_scans']
    if scans <= 0:
        raise ValueError('Additional scan count must be positive')
    ticket = spare*s*inv['r5_avoided_unusable_ticket_minutes']*rates['IM']
    for seconds in inv['scan_seconds_scenarios']:
        if seconds < 0:
            raise ValueError('Negative scan duration')
        value = (control*k-scans*seconds/D(60))*rates['IO']+ticket
        add('r4_r5_net_capacity_value', f'scan_{seconds}_sec', value, 'AUD', 'hypothetical steady-state day; IO-priced scans')
    breakeven_seconds = (control*k+ticket/rates['IO'])/scans*D(60)
    add('r4_r5_scan_breakeven', 'reference', breakeven_seconds, 'seconds per added scan', 'hypothetical steady-state day')

    for label, weights in p['priority_weights'].items():
        if len(weights) != 3 or sum(weights) != D(1):
            raise ValueError('Priority weights must contain three shares summing to one')
        for weight in weights:
            fraction(weight)
        for issue, scores in p['priority_scores'].items():
            if len(scores) != 3 or any(not D(1) <= v <= D(5) for v in scores):
                raise ValueError(f'Invalid scores for {issue}')
            add('priority_weighted_score', f'{label}_{issue}', sum(v*t for v,t in zip(scores,weights)),
                'score', 'analyst judgement; not measured ROI')
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate analysis/results.csv')
    parser.add_argument('--check', action='store_true', help='Compare calculated results with the committed CSV')
    args = parser.parse_args()
    p = json.loads((ROOT/'analysis/scenario_inputs.json').read_text(), parse_float=D, parse_int=D)
    output = io.StringIO(newline='')
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(['metric','scenario','value','unit','scope'])
    writer.writerows(calculate(p))
    result = output.getvalue()
    destination = ROOT/'analysis/results.csv'
    if args.write:
        destination.write_text(result)
    if args.check:
        if not destination.exists() or destination.read_text() != result:
            raise SystemExit('FAIL: results differ; inspect assumptions and regenerate with --write')
        print('PASS: route conservation, input ranges and calculated CSV agree. Scenario estimates only.')
    elif not args.write:
        print(result, end='')


if __name__ == '__main__':
    main()
