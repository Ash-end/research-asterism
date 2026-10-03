"""Install the small skill runtime into a new directory; never overwrite it."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from validate import release_paths, validate

def install(source, target, *, check=False):
    source, target = Path(source).resolve(), Path(target).absolute()
    if target.name != 'research-methodology':
        raise ValueError('Target directory must be named research-methodology')
    if target.is_symlink() or target.resolve().is_relative_to(source):
        raise ValueError('Target cannot be a link or be inside the source package')
    errors = validate(source)
    if errors:
        raise ValueError('; '.join(errors))
    manifest = json.loads((source / 'release-files.json').read_text(encoding='utf-8'))
    runtime = manifest['runtime_files']
    if not runtime or len(runtime) != len(set(runtime)) or not set(runtime) <= set(release_paths(source)):
        raise ValueError('Runtime must be a unique subset of the release allowlist')
    if check:
        mismatches = [name for name in runtime if not (target/name).is_file() or (target/name).read_bytes() != (source/name).read_bytes()]
        if mismatches:
            raise ValueError('Installed runtime differs from this release: '+', '.join(mismatches))
    else:
        if target.exists():
            raise FileExistsError('Target already exists; review and back up before upgrading')
        target.mkdir(parents=True, exist_ok=False)
        for name in runtime:
            destination=target/name
            destination.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source/name,destination)
    return {'target_name':target.name,'runtime_files':len(runtime),'mode':'check' if check else 'install','files':[{'path':name,'sha256':hashlib.sha256((target/name).read_bytes()).hexdigest()} for name in runtime]}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target',type=Path,required=True)
    parser.add_argument('--check',action='store_true',help='Read-only comparison with this release')
    args=parser.parse_args()
    try:
        print(json.dumps(install(Path(__file__).resolve().parents[1],args.target,check=args.check),indent=2))
    except (OSError,ValueError,KeyError) as exc:
        parser.exit(1,str(exc)+'\n')

if __name__=='__main__':
    main()
