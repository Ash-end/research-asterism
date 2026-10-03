"""Regression tests for release boundaries and structural failures."""

import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from package_release import package
from validate import validate
from install_skill import install
from verify_evaluation import verify


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'research-methodology'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def tearDown(self):
        self.temp.cleanup()

    def test_missing_reference_is_reported(self):
        (self.root / 'references/field-map.md').unlink()
        self.assertTrue(validate(self.root))

    def test_traversal_manifest_is_rejected(self):
        (self.root / 'release-files.json').write_text(json.dumps({'files': ['../private.txt']}), encoding='utf-8')
        with self.assertRaises(ValueError):
            package(self.root, Path(self.temp.name) / 'release.zip')

    def test_unlisted_private_file_never_enters_release(self):
        (self.root / 'private-notes.txt').write_text('synthetic exclusion marker', encoding='utf-8')
        output = Path(self.temp.name) / 'release.zip'
        package(self.root, output)
        with zipfile.ZipFile(output) as archive:
            self.assertFalse(any('private-notes' in n for n in archive.namelist()))
            self.assertIsNone(archive.testzip())

    def test_existing_output_is_preserved(self):
        output = Path(self.temp.name) / 'release.zip'
        output.write_bytes(b'user-existing-file')
        with self.assertRaises(FileExistsError):
            package(self.root, output)
        self.assertEqual(output.read_bytes(), b'user-existing-file')

    def test_duplicate_case_is_reported(self):
        path = self.root / 'evals/cases.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['cases'].append(data['cases'][0])
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('evaluation fixtures' in e for e in validate(self.root)))

    def test_source_directory_names_do_not_change_skill_identity(self):
        for name in ('research-methodology-main', 'my-checkout'):
            with self.subTest(name=name):
                renamed = Path(self.temp.name) / name
                self.root.rename(renamed)
                self.assertEqual(validate(renamed), [])
                output = Path(self.temp.name) / f'{name}.zip'
                package(renamed, output)
                with zipfile.ZipFile(output) as archive:
                    self.assertTrue(all(n.startswith('research-methodology/') for n in archive.namelist()))
                renamed.rename(self.root)

    def test_installed_directory_must_match_name(self):
        renamed = Path(self.temp.name) / 'research-methodology-main'
        self.root.rename(renamed)
        self.assertTrue(any('Installed folder' in e for e in validate(renamed, installed=True)))

    def test_correct_installation_directory_passes(self):
        self.assertEqual(validate(self.root, installed=True), [])

    def test_source_mode_preserves_expected_skill_name(self):
        path = self.root / 'SKILL.md'
        path.write_text(path.read_text(encoding='utf-8').replace('name: research-methodology', 'name: renamed-skill', 1), encoding='utf-8')
        self.assertTrue(any('Skill name must be research-methodology' in e for e in validate(self.root)))

    def test_scientific_raw_case_drift_is_reported(self):
        path = self.root / 'evals/scientific-inputs/r01.json'
        raw = json.loads(path.read_text(encoding='utf-8'))
        raw['request'] += ' synthetic divergent input'
        path.write_text(json.dumps(raw), encoding='utf-8')
        self.assertTrue(any('Aggregate/raw case mismatch' in e for e in validate(self.root)))

    def test_duplicate_scientific_case_is_reported(self):
        path = self.root / 'evals/scientific-cases.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['cases'].append(data['cases'][0])
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('Scientific cases need unique IDs' in e for e in validate(self.root)))

    def test_runtime_install_excludes_docs_and_retains_entrypoint(self):
        target=Path(self.temp.name)/'project/.agents/skills/research-methodology'
        result=install(self.root,target)
        self.assertEqual(result['runtime_files'],11)
        self.assertTrue((target/'SKILL.md').is_file())
        self.assertTrue((target/'references/claim-design.md').is_file())
        self.assertFalse((target/'docs').exists())
        self.assertFalse((target/'evals').exists())
        self.assertEqual(install(self.root,target,check=True)['mode'],'check')

    def test_runtime_install_preserves_existing_target(self):
        target=Path(self.temp.name)/'project/.agents/skills/research-methodology'
        target.mkdir(parents=True)
        marker=target/'user-notes.txt'
        marker.write_text('existing user content',encoding='utf-8')
        with self.assertRaises(FileExistsError):
            install(self.root,target)
        self.assertEqual(marker.read_text(encoding='utf-8'),'existing user content')

    def test_historical_fingerprint_drift_is_detected(self):
        self.assertTrue(all(c['ok'] for c in verify(self.root)))
        old=self.root/'evals/snapshots/v0.3.0/SKILL.md'
        old.write_bytes(old.read_bytes()+b'changed historical bytes')
        self.assertFalse(all(c['ok'] for c in verify(self.root)))

    def test_current_evaluation_output_drift_is_detected(self):
        self.assertTrue(all(c['ok'] for c in verify(self.root)))
        output=self.root/'evals/v0.5.0/outputs/d01-a.md'
        output.write_bytes(output.read_bytes()+b'changed retained behavior output')
        self.assertFalse(all(c['ok'] for c in verify(self.root)))

    def test_comparison_baseline_drift_is_detected(self):
        baseline=self.root/'evals/snapshots/v0.4.1/references/first-principles.md'
        baseline.write_bytes(baseline.read_bytes()+b'changed comparison baseline')
        self.assertFalse(all(c['ok'] for c in verify(self.root)))

    def test_current_raw_case_drift_is_reported(self):
        path=self.root/'evals/v0.5.0/inputs/i01.json'
        raw=json.loads(path.read_text(encoding='utf-8'))
        raw['request']+=' divergent raw fixture'
        path.write_text(json.dumps(raw),encoding='utf-8')
        self.assertTrue(any('Current aggregate/raw mismatch' in e for e in validate(self.root)))


if __name__ == '__main__':
    unittest.main()
