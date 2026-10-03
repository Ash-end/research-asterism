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
    return checks

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path)
    args=parser.parse_args()
    checks=verify(args.root)
    print(json.dumps({'ok':all(c['ok'] for c in checks),'checks':checks,'scope':'Historical bytes only'},indent=2))
    raise SystemExit(any(not c['ok'] for c in checks))
