"""Measure whitespace-separated words, not tokens, latency or actual loaded context.

Run from any directory: python evals/measure_reading.py --original <git-ref>
    --previous <git-ref> --output <new-json-path>
The candidate is the current working tree. Earlier refs need to exist locally.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
COMMON = ['SKILL.md', 'references/baseline.md', 'references/screenshots.md']
EARLIER = COMMON + ['references/task-completion.md', 'references/tool-execution.md',
                    'references/human-errors.md', 'references/cases-and-reports.md']


def measure(ref, direct_path):
    def read(path):
        if ref is None:
            return (ROOT / path).read_bytes()
        return subprocess.check_output(['git', 'show', f'{ref}:{path}'], cwd=ROOT)

    if ref is None:
        paths = ['SKILL.md'] + [str(p.relative_to(ROOT)) for folder in ('references', 'templates')
                               for p in (ROOT / folder).glob('*.md')]
    else:
        tracked = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', ref], cwd=ROOT).decode().splitlines()
        paths = [p for p in tracked if p == 'SKILL.md' or
                 (p.endswith('.md') and p.split('/')[0] in ('references', 'templates'))]
    files = {p: {'words': len(read(p).decode().split()), 'sha256': hashlib.sha256(read(p)).hexdigest()}
             for p in sorted(paths)}
    return {'skill_words': files['SKILL.md']['words'], 'ordinary_live_path': direct_path,
            'ordinary_live_words': sum(files[p]['words'] for p in direct_path),
            'all_markdown_words': sum(f['words'] for f in files.values()), 'files': files}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original', required=True)
    parser.add_argument('--previous', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = {'method': 'Python str.split; UTF-8; Markdown syntax and frontmatter included. '
                       'Ordinary live path means a narrow save/reopen check with familiar tools; '
                       'conditional references increase other paths. No runtime speed/token claim.',
              'original': measure(args.original, EARLIER),
              'previous': measure(args.previous, EARLIER + ['references/experience-profiles.md']),
              'candidate': measure(None, COMMON)}
    with args.output.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    for name in ('original', 'previous', 'candidate'):
        print(name, {k: result[name][k] for k in ('skill_words', 'ordinary_live_words', 'all_markdown_words')})


if __name__ == '__main__':
    main()
