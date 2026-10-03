"""Recompute recorded mask preferences and lengths; no semantic grading."""
import argparse
import json
from pathlib import Path

def check(root):
    directory=Path(root)/'evals/v0.5.0'
    run=json.loads((directory/'run.json').read_text(encoding='utf-8'))
    summary=json.loads((directory/'summary.json').read_text(encoding='utf-8'))
    decoded={}
    counts={}
    for direction in ['forward','reverse']:
        comparisons=json.loads((directory/f'comparison-{direction}.json').read_text(encoding='utf-8'))['comparisons']
        if len(comparisons)!=len(run['cases']) or {c['id'] for c in comparisons}!=set(run['cases']):
            raise ValueError('Comparison IDs do not match executed tasks')
        decoded[direction]={}
        counts[direction]={g:{k:0 for k in ['new','old','tie']} for g in ['all','development','independent']}
        for case in comparisons:
            winner=case['winner']
            if winner not in ['A','B','TIE']:
                raise ValueError('Invalid anonymous preference')
            id=case['id']
            actual='tie' if winner=='TIE' else run['identity_map'][id][direction][winner]
            decoded[direction][id]=actual
            group='development' if id.startswith('d') else 'independent'
            counts[direction]['all'][actual]+=1
            counts[direction][group][actual]+=1
    if counts!=summary['counts'] or counts!=run['comparison_summary'] or decoded!=summary['decoded_case_preferences']:
        raise ValueError('Recorded preference summary differs from actual judgments and masks')
    disagreement=[id for id in run['cases'] if decoded['forward'][id]!=decoded['reverse'][id]]
    if disagreement!=summary['disagreements'] or disagreement!=run['disagreements']:
        raise ValueError('Recorded disagreements differ')
    lengths={}
    for condition,suffix in [('old','a'),('new','b')]:
        paths=[]
        for id in run['cases']:
            paths.extend([directory/'outputs'/f'{id}-{suffix}-turn1.md',directory/'outputs'/f'{id}-{suffix}-turn2.md'] if id=='d02' else [directory/'outputs'/f'{id}-{suffix}.md'])
        lengths[condition]=sum(len(path.read_text(encoding='utf-8').strip()) for path in paths)
    if lengths!=run['lengths_unicode']:
        raise ValueError('Recorded answer lengths differ')
    return {'ok':True,'counts':counts,'disagreements':disagreement,'lengths':lengths,'scope':'Recorded mask arithmetic and lengths only; not scientific judgment'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root',type=Path)
    args=parser.parse_args()
    print(json.dumps(check(args.root),indent=2))
