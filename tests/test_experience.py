"""Targeted data-contract regressions; no claims about live QA performance."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_experience import validate


def planned():
    return json.loads((ROOT / 'templates/experience-run.json').read_text(encoding='utf-8'))


def observed():
    report = planned()
    report['sources'] = [{'id': 'PRIOR', 'path': 'run-previous.json'}, {'id': 'OBS', 'path': 'action-01.json'}]
    exp = report['experience']
    exp.update(profile='L1', experience_basis='observed', previous_run_refs=['PRIOR'])
    exp['knowledge_before'] = [{'id': 'K1', 'claim': 'Save is in the visible editor', 'origin': 'observed',
                                'source_refs': ['OBS'], 'learned_in_run': 'RUN-PREVIOUS', 'build': None}]
    report['cases'] = [{'id': 'TC1', 'status': 'passed', 'actual_result': 'Reopened the saved text', 'evidence_refs': ['OBS']}]
    return report


class ExperienceTests(unittest.TestCase):
    def test_unexecuted_template_and_legacy(self):
        self.assertEqual(validate(planned())['extension'], '1.0')
        self.assertEqual(validate({'schema_version': '2.0'})['extension'], 'absent')
        with self.assertRaises(ValueError):
            validate({}, require_experience=True)

    def test_observed_repeat_and_unearned_experience(self):
        self.assertEqual(validate(observed())['extension'], '1.0')
        report = planned()
        report['experience']['profile'] = 'L2'
        report['cases'] = observed()['cases']
        with self.assertRaisesRegex(ValueError, 'prior knowledge'):
            validate(report)

    def test_cold_boundary_requires_evidence(self):
        report = planned()
        report['experience']['knowledge_boundary']['status'] = 'verified'
        with self.assertRaisesRegex(ValueError, 'evidence references'):
            validate(report)
        report['sources'] = [{'id': 'SETUP', 'path': 'setup.json'}]
        report['experience']['knowledge_boundary']['basis_refs'] = ['SETUP']
        validate(report)
        report['experience']['knowledge_boundary']['exposures'] = ['PRD route']
        with self.assertRaisesRegex(ValueError, 'exposures'):
            validate(report)

    def test_guided_l0_not_cold(self):
        report = planned()
        report['sources'] = [{'source_id': 'SETUP'}]
        report['experience']['knowledge_boundary'].update(status='verified', observation_mode='guided', basis_refs=['SETUP'])
        with self.assertRaisesRegex(ValueError, 'guided L0'):
            validate(report)

    def test_seeded_and_mixed_provenance(self):
        report = observed()
        exp = report['experience']
        exp['knowledge_before'][0].update(origin='provided', learned_in_run=None)
        exp['experience_basis'] = 'seeded'
        validate(report)
        exp['experience_basis'] = 'observed'
        with self.assertRaisesRegex(ValueError, 'origins'):
            validate(report)
        exp['knowledge_before'].append(copy.deepcopy(observed()['experience']['knowledge_before'][0]))
        exp['knowledge_before'][1]['id'] = 'K2'
        exp['experience_basis'] = 'mixed'
        validate(report)

    def test_unresolved_and_missing_prior_references(self):
        report = observed()
        report['experience']['knowledge_before'][0]['source_refs'] = ['MISSING']
        with self.assertRaisesRegex(ValueError, 'unresolved reference'):
            validate(report)
        report = observed()
        report['experience']['previous_run_refs'] = []
        with self.assertRaisesRegex(ValueError, 'prior report'):
            validate(report)

    def test_assistance_preserves_link(self):
        report = observed()
        exp = report['experience']
        exp['assistance'] = {'external': True, 'events': [{'kind': 'external', 'step_id': 'S1', 'evidence_refs': ['OBS']}]}
        with self.assertRaisesRegex(ValueError, 'unassisted'):
            validate(report)
        exp['knowledge_boundary']['status'] = 'informed'
        validate(report)

    def test_hidden_assistance_and_missing_help_evidence(self):
        report = observed()
        exp = report['experience']
        exp['assistance']['events'] = [{'kind': 'external', 'step_id': 'S1', 'evidence_refs': ['OBS']}]
        with self.assertRaisesRegex(ValueError, 'match recorded events'):
            validate(report)
        exp['assistance']['events'][0]['kind'] = 'in-product'
        validate(report)
        exp['assistance']['events'][0]['evidence_refs'] = []
        with self.assertRaisesRegex(ValueError, 'evidence references'):
            validate(report)

    def test_blocked_plan_does_not_require_invented_experience(self):
        report = planned()
        report['experience']['profile'] = 'L2'
        report['cases'] = [{'id': 'TC1', 'status': 'blocked', 'actual_result': 'No browser available', 'evidence_refs': []}]
        validate(report)

    def test_unexecuted_or_unsupported_pass(self):
        for status, result, evidence in [('not-run', 'saved', []), ('passed', 'saved', []), ('failed', None, ['OBS'])]:
            with self.subTest(status=status):
                report = planned()
                report['cases'] = [{'id': 'TC', 'status': status, 'actual_result': result, 'evidence_refs': evidence}]
                with self.assertRaises(ValueError):
                    validate(report)

    def test_malformed_extension_is_clear_error(self):
        for key, value in [('profile', []), ('knowledge_before', {}), ('knowledge_boundary', None), ('state', [])]:
            with self.subTest(key=key):
                report = planned()
                report['experience'][key] = value
                with self.assertRaises(ValueError):
                    validate(report)

    def test_new_learning_and_duplicate_ids(self):
        report = observed()
        entry = copy.deepcopy(report['experience']['knowledge_before'][0])
        entry['id'] = 'K2'
        report['experience']['knowledge_after'] = [entry]
        with self.assertRaisesRegex(ValueError, 'current run'):
            validate(report)
        entry['learned_in_run'] = report['experience']['run_id']
        validate(report)
        report['cases'].append(copy.deepcopy(report['cases'][0]))
        with self.assertRaisesRegex(ValueError, 'duplicate case'):
            validate(report)

    def test_cli_roundtrip_does_not_modify_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'run.json'
            source.write_text(json.dumps(planned()), encoding='utf-8')
            before = source.read_bytes()
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_experience.py'), str(source), '--require-experience'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('record consistency', json.loads(result.stdout)['validation'])
            self.assertEqual(before, source.read_bytes())
            source.write_text('{broken', encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_experience.py'), str(source)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn('Traceback', result.stderr)

    @unittest.skipUnless(importlib.util.find_spec('openpyxl'), 'optional openpyxl unavailable')
    def test_export_preserves_experience_and_literal_knowledge(self):
        from export_xlsx import export
        from openpyxl import load_workbook
        report = observed()
        report['experience']['knowledge_before'][0]['claim'] = '=HYPERLINK("test") 한글\n学習'
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / 'run.xlsx'
            export(report, dest)
            book = load_workbook(dest)
            context_cell = book['Sources']['B2']
            self.assertNotEqual(context_cell.data_type, 'f')
            self.assertEqual(json.loads(context_cell.value)['experience'], report['experience'])
            with self.assertRaises(FileExistsError):
                export(report, dest)


if __name__ == '__main__':
    unittest.main()
