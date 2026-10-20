"""Converte UM finding do webhook generico para Jira Cloud v3."""
import json
import os
import sys
from pathlib import Path

event = json.loads(Path(sys.argv[1]).read_text())
index = int(sys.argv[2]) if len(sys.argv) > 2 else 0
finding = event['results'][index]
repo = event.get('repo_full_name', 'repository-not-provided')
ident = str(finding['id'])
import hashlib
label = 'dryrun-' + hashlib.sha256(
    (repo + ':' + ident).encode()).hexdigest()[:24]
text = '\n'.join([
    'DryRun finding: ' + ident,
    'Repository: ' + repo,
    'PR: ' + str(event.get('pr_number', '')),
    'Risk: ' + str(finding.get('risk', '')),
    'File: ' + str(finding.get('filename', '')),
    'Line: ' + str(finding.get('line_start', '')),
    str(finding.get('description', '')),
    'Dashboard: ' + str(event.get('dashboard_url', '')),
])
payload = {'fields': {
    'project': {'key': os.environ['JIRA_PROJECT']},
    'issuetype': {'id': os.environ['JIRA_ISSUETYPE_ID']},
    'summary': ('[DryRun] ' + str(finding.get('type', 'Finding'))
                + ' - ' + repo)[:240],
    'labels': [label],
    'description': {'type': 'doc', 'version': 1, 'content': [
        {'type': 'paragraph', 'content': [{'type': 'text', 'text': text}]}]},
}}
Path('.evidence/jira-create.json').write_text(json.dumps(payload, indent=2))
Path('.evidence/jira-label.txt').write_text(label)
print('Payload pronto. Label:', label)
