"""Offline package checks. No model calls or scientific judgments."""

import argparse
import ast
import json
import re
from pathlib import Path


def release_paths(root):
    manifest = json.loads((root / 'release-files.json').read_text(encoding='utf-8'))
    paths = manifest['files']
    if not isinstance(paths, list) or not paths or len(paths) != len(set(paths)):
        raise ValueError('Release manifest must contain unique file paths')
    for item in paths:
        if not isinstance(item, str) or '\\' in item or ':' in item:
            raise ValueError(f'Invalid release path: {item!r}')
        p = Path(item)
        if p.is_absolute() or '..' in p.parts or p.as_posix() != item:
            raise ValueError(f'Unsafe release path: {item!r}')
        target = root / p
        if target.is_symlink() or not target.is_file():
            raise ValueError(f'Missing file or symbolic link: {item}')
        if not target.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Release path escapes package: {item}')
        if any(parent.is_symlink() for parent in target.parents if parent != root.parent):
            raise ValueError(f'Symbolic link ancestor: {item}')
    return paths


def validate(root, *, installed=False):
    # A source checkout/archive may have any directory name. An installation
    # must retain the advertised skill name at the discovery path.
    installed_name = Path(root).absolute().name
    root = Path(root).resolve()
    errors = []
    try:
        content = (root / 'SKILL.md').read_text(encoding='utf-8')
        front, body = content.removeprefix('---\n').split('\n---\n', 1)
        if not content.startswith('---\n'):
            raise ValueError('Missing YAML frontmatter')
        fields = {}
        for line in front.splitlines():
            key, value = line.split(':', 1)
            if key in fields:
                raise ValueError('Duplicate frontmatter key')
            value = value.strip()
            fields[key] = json.loads(value) if value.startswith('"') else value
        if set(fields) != {'name', 'description', 'license'}:
            raise ValueError('This package uses name, description, license scalar fields')
        if fields['name'] != 'research-methodology' or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields['name']):
            raise ValueError('Skill name must be research-methodology in hyphen-case')
        if installed and fields['name'] != installed_name:
            raise ValueError('Installed folder must match the skill name')
        if len(fields['name']) > 64 or not 1 <= len(fields['description']) <= 1024:
            raise ValueError('Frontmatter length outside supported range')
        if fields['license'] != 'MIT' or len(body.splitlines()) > 120:
            raise ValueError('Unexpected license or entrypoint exceeds maintenance limit')
        if '[TODO:' in content:
            raise ValueError('Unfinished scaffold placeholder')
    except (ValueError, OSError, TypeError, KeyError) as exc:
        errors.append(f'entrypoint: {exc}')

    try:
        paths = release_paths(root)
    except (ValueError, OSError, TypeError, KeyError) as exc:
        errors.append(f'release manifest: {exc}')
        paths = []

    for name in paths:
        path = root / name
        if path.suffix == '.md':
            text = path.read_text(encoding='utf-8')
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                if re.match(r'^(?:https?://|mailto:|#)', link):
                    continue
                destination = link.split('#', 1)[0]
                if not (path.parent / destination).is_file():
                    errors.append(f'{name}: missing relative link {link}')
        if path.suffix == '.py':
            try:
                ast.parse(path.read_text(encoding='utf-8'), filename=name)
            except SyntaxError as exc:
                errors.append(f'{name}: {exc}')
        if path.suffix == '.json':
            try:
                json.loads(path.read_text(encoding='utf-8'))
            except ValueError as exc:
                errors.append(f'{name}: {exc}')

    try:
        cases = json.loads((root / 'evals/cases.json').read_text(encoding='utf-8'))['cases']
        triggers = json.loads((root / 'evals/triggers.json').read_text(encoding='utf-8'))['cases']
        labels = json.loads((root / 'evals/trigger-labels.json').read_text(encoding='utf-8'))['expected']
        for group in (cases, triggers):
            ids = [c['id'] for c in group]
            if len(ids) != len(set(ids)) or any(not c['request'].strip() for c in group):
                raise ValueError('Duplicate IDs or empty raw requests')
        if {x['id'] for x in labels} != {x['id'] for x in triggers} or len(labels) != len(triggers):
            raise ValueError('Trigger labels must correspond exactly to requests')
        if any(type(x['should_trigger']) is not bool for x in labels):
            raise ValueError('Trigger labels must be boolean')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        errors.append(f'evaluation fixtures: {exc}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--installed', action='store_true', help='Also check the installation directory name')
    args = parser.parse_args()
    errors = validate(args.root, installed=args.installed)
    print(json.dumps({'ok': not errors, 'errors': errors, 'mode': 'installed' if args.installed else 'source', 'scope': 'package structure only'}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
