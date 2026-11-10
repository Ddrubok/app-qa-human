"""Check optional experience extension 1.0; never certify execution or isolation.

Usage: python scripts/validate_experience.py report.json [--require-experience]
Uses only the Python standard library. Does not modify the report.
"""
import argparse
import json
from pathlib import Path
import sys


def validate(report, require_experience=False):
    def check(condition, message):
        if not condition:
            raise ValueError(message)

    def obj(value, label):
        check(isinstance(value, dict), label + ' must be an object')
        return value

    def seq(value, label):
        check(isinstance(value, list), label + ' must be an array')
        return value

    def text(value, label):
        check(isinstance(value, str) and bool(value.strip()), label + ' must be nonempty text')
        return value

    def choice(value, options, label):
        check(isinstance(value, str) and value in options, label + ' has an unsupported value')

    obj(report, 'report')
    if 'experience' not in report:
        check(not require_experience, 'experience is required')
        return {'extension': 'absent', 'validation': 'legacy report not evaluated'}
    check(report.get('schema_version') == '2.0', 'experience 1.0 requires report schema_version 2.0')
    exp = obj(report['experience'], 'experience')
    check(exp.get('contract_version') == '1.0', 'unsupported experience contract_version')
    for key in ('campaign_id', 'run_id'):
        text(exp.get(key), key)
    choice(exp.get('profile'), ('L0', 'L1', 'L2', 'Lapsed'), 'profile')
    choice(exp.get('experience_basis'), ('none', 'observed', 'seeded', 'mixed'), 'experience_basis')
    source_ids = set()
    for source in seq(report.get('sources'), 'sources'):
        obj(source, 'source')
        if 'id' in source and 'source_id' in source:
            check(source['id'] == source['source_id'], 'source id and source_id disagree')
        source_id = text(source.get('id', source.get('source_id')), 'source ID')
        check(source_id not in source_ids, 'duplicate source ID: ' + source_id)
        source_ids.add(source_id)

    def refs(value, label, required=False):
        values = seq(value, label)
        check(not required or bool(values), label + ' needs evidence references')
        for ref in values:
            text(ref, label + ' reference')
            check(ref in source_ids, label + ' unresolved reference: ' + ref)
        return values

    previous = refs(exp.get('previous_run_refs'), 'previous_run_refs')
    boundary = obj(exp.get('knowledge_boundary'), 'knowledge_boundary')
    choice(boundary.get('status'), ('verified', 'informed', 'contaminated', 'unverified'), 'boundary status')
    choice(boundary.get('observation_mode'), ('visual', 'assistive', 'guided'), 'observation_mode')
    refs(boundary.get('basis_refs'), 'boundary basis_refs', boundary['status'] == 'verified')
    exposures = seq(boundary.get('exposures'), 'exposures')
    check(boundary['status'] != 'verified' or not exposures, 'verified boundary cannot have exposures')
    check(not exposures or boundary['status'] in ('informed', 'contaminated'),
          'known exposures must be labeled informed or contaminated')
    state = obj(exp.get('state'), 'state')
    choice(state.get('setup'), ('fresh', 'retained', 'seeded', 'unknown'), 'state setup')
    text(state.get('description'), 'state description')
    refs(state.get('evidence_refs'), 'state evidence_refs')
    assistance = obj(exp.get('assistance'), 'assistance')
    check(isinstance(assistance.get('external'), bool), 'assistance.external must be boolean')
    events = seq(assistance.get('events'), 'assistance events')
    external_events = False
    for event in events:
        obj(event, 'assistance event')
        choice(event.get('kind'), ('in-product', 'external'), 'assistance kind')
        text(event.get('step_id'), 'assistance step_id')
        refs(event.get('evidence_refs'), 'assistance evidence_refs', True)
        external_events = external_events or event['kind'] == 'external'
    check(assistance['external'] == external_events, 'assistance.external must match recorded events')
    if assistance['external']:
        check(boundary['status'] in ('informed', 'contaminated'), 'external assistance cannot be an unassisted boundary')
        check(bool(previous), 'assisted continuation needs a prior attempt reference')

    origins = set()
    knowledge_ids = set()
    for collection in ('knowledge_before', 'knowledge_after'):
        for entry in seq(exp.get(collection), collection):
            obj(entry, 'knowledge entry')
            entry_id = text(entry.get('id'), 'knowledge ID')
            check(entry_id not in knowledge_ids, 'duplicate knowledge ID: ' + entry_id)
            knowledge_ids.add(entry_id)
            text(entry.get('claim'), 'knowledge claim')
            choice(entry.get('origin'), ('observed', 'provided'), 'knowledge origin')
            refs(entry.get('source_refs'), 'knowledge source_refs', True)
            check('build' in entry, 'knowledge build must be present (null if unknown)')
            if entry['origin'] == 'observed':
                learned = text(entry.get('learned_in_run'), 'learned_in_run')
                if collection == 'knowledge_after':
                    check(learned == exp['run_id'], 'new learning must refer to the current run')
                else:
                    check(learned != exp['run_id'], 'prior learning cannot come from the current run')
                    check(bool(previous), 'observed prior learning needs a prior report reference')
            else:
                check('learned_in_run' in entry and entry['learned_in_run'] is None,
                      'provided knowledge must not claim a learned_in_run')
            if collection == 'knowledge_before':
                origins.add(entry['origin'])
    seq(exp.get('unresolved'), 'unresolved')
    expected_origins = {'none': set(), 'observed': {'observed'}, 'seeded': {'provided'}, 'mixed': {'observed', 'provided'}}
    check(origins == expected_origins[exp['experience_basis']], 'experience_basis does not match prior knowledge origins')
    if exp['profile'] == 'L0' and boundary['status'] == 'verified':
        check(not exp['knowledge_before'], 'cold L0 cannot start with product knowledge')
        check(boundary['observation_mode'] != 'guided', 'guided L0 cannot certify cold discovery')

    executed = False
    case_ids = set()
    for case in seq(report.get('cases'), 'cases'):
        obj(case, 'case')
        case_id = text(case.get('id'), 'case ID')
        check(case_id not in case_ids, 'duplicate case ID within run: ' + case_id)
        case_ids.add(case_id)
        status = case.get('status')
        choice(status, ('not-run', 'passed', 'failed', 'blocked', 'not-applicable'), 'case status')
        evidence = refs(case.get('evidence_refs'), 'case evidence_refs', status in ('passed', 'failed'))
        if status in ('passed', 'failed'):
            check(case.get('actual_result') not in (None, '', [], {}), 'executed pass/fail needs actual_result')
        if status == 'not-run':
            check(case.get('actual_result') is None and not evidence, 'not-run cannot carry execution results')
        executed = executed or status in ('passed', 'failed')
    if executed and exp['profile'] != 'L0':
        check(exp['experience_basis'] != 'none', 'executed experienced profile needs prior knowledge')
    for finding in seq(report.get('findings', []), 'findings'):
        obj(finding, 'finding')
        level = finding.get('evidence_level')
        choice(level, ('reproduced', 'code-confirmed', 'needs-verification'), 'finding evidence_level')
        refs(finding.get('evidence_refs'), 'finding evidence_refs', level != 'needs-verification')
    return {'extension': '1.0', 'run_id': exp['run_id'], 'validation': 'record consistency only; execution and isolation not verified'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--require-experience', action='store_true')
    args = parser.parse_args()
    try:
        report = json.loads(args.source.read_text(encoding='utf-8-sig'))
        result = validate(report, args.require_experience)
    except (OSError, UnicodeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
