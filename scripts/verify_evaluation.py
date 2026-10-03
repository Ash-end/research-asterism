"""Verify retained evaluation bytes, not scientific conclusions."""
import argparse
import hashlib
import json
from pathlib import Path

def verify(root):
    root=Path(root)
    run=json.loads((root/'evals/results/scientific-run.json').read_text(encoding='utf-8'))
    checks=[]
    for group in ['source_sha256','packaged_artifact_sha256']:
        for name,expected in run[group].items():
            actual_name='evals/snapshots/v0.3.0/'+name if name=='SKILL.md' or name.startswith('references/') else name
            checks.append({'recorded':name,'retained':actual_name,'ok':hashlib.sha256((root/actual_name).read_bytes()).hexdigest()==expected})
    snapshot=root/'evals/snapshots/v0.4.1'
    for name,expected in json.loads((snapshot/'sha256.json').read_text(encoding='utf-8')).items():
        checks.append({'recorded':'v0.4.1/'+name,'retained':(snapshot/name).relative_to(root).as_posix(),'ok':hashlib.sha256((snapshot/name).read_bytes()).hexdigest()==expected})
    prior=json.loads((root/'evals/results/intervention-chain-author-run.json').read_text(encoding='utf-8'))
    for name,expected in prior['source_sha256'].items():
        retained='evals/snapshots/v0.4.1/'+name if name=='SKILL.md' or name.startswith('references/') else name
        checks.append({'recorded':'p05/'+name,'retained':retained,'ok':hashlib.sha256((root/retained).read_bytes()).hexdigest()==expected})
    current=root/'evals/v0.5.0/run.json'
    if current.is_file():
        run=json.loads(current.read_text(encoding='utf-8'))
        for group in ['candidate_source_sha256','packaged_artifact_sha256']:
            for name,expected in run[group].items():
                checks.append({'recorded':'v0.5.0/'+name,'retained':name,'ok':hashlib.sha256((root/name).read_bytes()).hexdigest()==expected})
    return checks

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path)
    args=parser.parse_args()
    checks=verify(args.root)
    print(json.dumps({'ok':all(c['ok'] for c in checks),'checks':checks,'scope':'Historical bytes only'},indent=2))
    raise SystemExit(any(not c['ok'] for c in checks))
