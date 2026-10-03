"""Build a clean ZIP from the explicit allowlist; never traverse the parent repo."""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

from validate import release_paths, validate


def package(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    errors = validate(root)
    if errors:
        raise ValueError('; '.join(errors))
    if output.is_relative_to(root):
        raise ValueError('Output must be outside the source skill folder')
    output.parent.mkdir(parents=True, exist_ok=True)
    records = []
    # Exclusive creation prevents overwriting a user file or another release.
    with output.open('xb') as stream:
        with zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(release_paths(root)):
                data = (root / name).read_bytes()
                item = zipfile.ZipInfo(f'research-methodology/{name}', (2026, 1, 1, 0, 0, 0))
                item.compress_type = zipfile.ZIP_DEFLATED
                item.external_attr = 0o100644 << 16
                archive.writestr(item, data)
                records.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    return {'file_count': len(records), 'sha256': hashlib.sha256(output.read_bytes()).hexdigest(), 'files': records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = package(args.root, args.output)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
