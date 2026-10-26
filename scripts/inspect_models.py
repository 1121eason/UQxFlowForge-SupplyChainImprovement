#!/usr/bin/env python3
"""Inspect limited BPMN XML integrity and reproduce the source inventory."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
B = 'http://www.omg.org/spec/BPMN/20100524/MODEL'
DI = 'http://www.omg.org/spec/BPMN/20100524/DI'
NS = {'b': B, 'd': DI}


def inspect(path):
    raw = path.read_bytes()
    root = ET.fromstring(raw)
    id_values = [e.get('id') for e in root.iter() if e.get('id')]
    by_id = {e.get('id'): e for e in root.iter() if e.get('id')}
    duplicate_ids = sorted(k for k,v in Counter(id_values).items() if v > 1)
    counts = Counter(e.tag.split('}')[-1] for e in root.iter() if e.tag.startswith('{'+B+'}'))
    unresolved = []
    for e in root.iter():
        for key in ('sourceRef','targetRef','processRef','bpmnElement','dataStoreRef','attachedToRef','messageRef','errorRef'):
            ref = e.get(key)
            if ref and ref not in by_id:
                unresolved.append({'element':e.get('id'), 'attribute':key, 'reference':ref})
        if e.tag in ('{'+B+'}sequenceFlow','{'+B+'}messageFlow'):
            for key in ('sourceRef','targetRef'):
                if not e.get(key):
                    unresolved.append({'element':e.get('id'),'attribute':key,'reference':None})
        if e.tag in ('{'+B+'}incoming','{'+B+'}outgoing','{'+B+'}flowNodeRef'):
            ref = (e.text or '').strip()
            if ref and ref not in by_id:
                unresolved.append({'element':None,'attribute':e.tag.split('}')[-1],'reference':ref})
    diagrams = []
    for d in root.findall('d:BPMNDiagram',NS):
        plane = d.find('d:BPMNPlane',NS)
        ref = plane.get('bpmnElement')
        element = by_id.get(ref)
        diagrams.append({'id':d.get('id'),'element':ref,
                         'name':element.get('name') or root.get('name') if element is not None else None})
    drawn = {d['element'] for d in diagrams}
    missing_subprocess_diagrams = [e.get('id') for e in root.findall('.//b:subProcess',NS) if e.get('id') not in drawn]
    timers = []
    for e in root.findall('.//b:timerEventDefinition',NS):
        timers.append({'id':e.get('id'),'expressions':[
            {'kind':c.tag.split('}')[-1],'value':''.join(c.itertext()).strip()} for c in e]})
    return {'path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),
            'exporter':root.get('exporter'),'exporterVersion':root.get('exporterVersion'),
            'counts':dict(sorted(counts.items())),'diagrams':diagrams,
            'duplicate_ids':duplicate_ids,'unresolved_references_or_endpoints':unresolved,
            'subprocesses_without_diagrams':missing_subprocess_diagrams,'timers':timers,
            'scope':'XML inventory and selected references only; no process execution, XSD, token-soundness or native convention check'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args=parser.parse_args()
    result={'models':[inspect(ROOT/'models'/name) for name in ('flowforge-as-is.bpmn','flowforge-to-be.bpmn')]}
    rendered=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    destination=ROOT/'docs/evidence/model-inventory.json'
    if args.write:
        destination.write_text(rendered)
    if args.check:
        problems=[m['path'] for m in result['models'] if m['duplicate_ids'] or m['unresolved_references_or_endpoints'] or m['subprocesses_without_diagrams']]
        if problems:
            raise SystemExit('FAIL: limited integrity issues in '+', '.join(problems))
        if not destination.exists() or destination.read_text()!=rendered:
            raise SystemExit('FAIL: inventory differs; inspect and regenerate with --write')
        print('PASS: both XML files parse; unique IDs, selected references, subprocess diagram coverage and inventory agree.')
        print('This does not establish native Signavio compliance or operational feasibility.')
    elif not args.write:
        print(rendered,end='')


if __name__=='__main__':
    main()
