"""Save non-secret student paths; no token is stored."""
from pathlib import Path
import re
import shlex
import sys


def save(repo, root):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('Expected OWNER/REPO, not a URL')
    root = Path(root).resolve()
    kit = root / 'material' / 'laboratorios'
    work = root / 'repo'
    if not (kit / 'lab.sh').is_file() or not (work / '.git').exists():
        raise ValueError('Expected material/laboratorios and initialized repo')
    q = shlex.quote
    content = '\n'.join([
        '# Generated course session: no credentials.',
        'export KIT=' + q(str(kit)),
        'export GH_REPO=' + q(repo),
        'cd ' + q(str(work)) + ' || return',
        'mkdir -p .evidence',
        'source "$KIT/lab.sh"',
        '',
    ])
    (root / 'session.sh').write_text(content)
    print('Session saved:', root / 'session.sh')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 save_session.py OWNER/REPO')
    save(sys.argv[1], Path.home() / 'dryrun-student')
