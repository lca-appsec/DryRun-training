# Kit do aluno / Student kit

Este kit acompanha a edição 2 do treinamento DryRun, de 23/10/2026.
This kit accompanies edition 2 of the DryRun course, dated 2026-10-23.

## Português

Leia primeiro a preparação no PDF ou em treinamento-fonte.md. O curso cria duas
pastas diferentes: `material` guarda o conteúdo; `repo` recebe os exercícios.
Não crie PRs vulneráveis no repositório que guarda o treinamento.

No modo ZIP, extraia os arquivos em `$HOME/dryrun-student/material/laboratorios`.
No modo clone, o roteiro já coloca os arquivos nesse caminho. O módulo 2 cria
`session.sh`, sem tokens; carregue-o em cada terminal novo. O código completo
dos auxiliares está no apêndice do PDF.

As mensagens dos scripts são em inglês nos dois idiomas. O texto de cada passo
explica o que deve aparecer. Algumas falhas de teste são intencionais; não
mescle as versões vulneráveis na main.

## English

Read setup in the PDF or training-source-en.md first. The course uses two separate
folders: `material` stores the content; `repo` hosts exercises. Do not create
vulnerable PRs in the training-material repository.

For ZIP setup, extract files into `$HOME/dryrun-student/material/laboratorios`.
Clone setup already places them there. Module 2 generates `session.sh` without
tokens; load it in each new terminal. Full helper source is in the PDF appendix.

Scripts use English messages in both editions; each step explains expected
output. Some test failures are intentional. Do not merge vulnerable versions
into main.

## Files

- `app.py`, `test_app.py`: safe local application and two tests.
- `change.py`: toggles only the educational SQL query after checking its state.
- `lab.sh`: explained Bash helpers for branches, PRs, evidence and API reads.
- `save_session.py`: stores paths/repo identity, never API keys.
- `receiver.py`: local teaching webhook receiver, not a production service.
- `jira_payload.py`: generates a reviewable Jira payload; makes no network calls.
- `event-example.json`: synthetic event.
- `treinamento-fonte.md`, `training-source-en.md`: full editable student guides.
- `verificacao-local.json`: authoring test results, not evidence of live scans.

## Local baseline test

Run in the folder containing app.py and test_app.py:

```bash
python3 -m unittest -v
```

Real DryRun, Jira and Codex operations require your own credentials and access.
No credentials are included. Local test results do not claim those integrations
were executed in your accounts.
