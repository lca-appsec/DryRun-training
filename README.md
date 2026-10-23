# DryRun Security - Student Training / Treinamento do Aluno

**Edition 2 / Edição 2 - 2026-10-23**

| Material | Português do Brasil | English |
| --- | --- | --- |
| PDF | [Guia do aluno - 81 páginas](docs/treinamento-tecnico-dryrun-pt-br.pdf) | [Student guide - 79 pages](docs/treinamento-tecnico-dryrun-en.pdf) |
| Editable source | [Guia em Markdown](guias/pt-br.md) | [Markdown guide](guias/en.md) |

[Kit de laboratórios / Lab kit ZIP](docs/kit-treinamento-dryrun.zip) · [Scripts and instructions](laboratorios/README.md)

## Português

Treinamento técnico para alunos sem experiência prévia em Git, terminal ou integrações de segurança: **25 módulos, 25 laboratórios e 167 passos guiados** em cada idioma, sem flashcards.

Cada laboratório informa pré-requisitos, onde agir (Terminal, GitHub, DryRun ou chat Codex), comandos, resultado esperado, recuperação de erros e limpeza. A preparação explica o vocabulário, instalação de ferramentas, autenticação e como retomar o curso em outra sessão.

Comece pela preparação do PDF ou do guia Markdown. O clone deste repositório guarda os materiais em `material`; o módulo 2 cria **outro repositório privado** para exercícios em `repo`. Não execute os exemplos vulneráveis como mudanças neste repositório de materiais. Não mescle versões vulneráveis na main.

O conteúdo cobre Getting Started; PR Scanning, SCA, DeepScan, Secrets e IaC; linguagens e cobertura; Reporting, Risk Register, CSI, configuração, políticas, contexto, feedback, blocking e permissões; MCP/API; webhooks, Jira, chaves, remediação e DryRun Skill.

Os comandos executáveis são equivalentes nos dois idiomas. As mensagens dos scripts permanecem em inglês, com explicação no roteiro. O kit completo também está transcrito no apêndice dos PDFs.

## English

Technical training for students without previous Git, terminal or security-integration experience: **25 modules, 25 labs and 167 guided steps** in each language, without flashcards.

Each lab identifies prerequisites, where to act (Terminal, GitHub, DryRun or Codex chat), commands, expected results, recovery and cleanup. Setup covers vocabulary, tool installation, authentication and resuming in another session.

Start with setup in the PDF or Markdown guide. This clone stores materials under `material`; module 2 creates **a separate private repository** for exercises under `repo`. Do not perform vulnerable exercises as changes to this materials repository. Do not merge vulnerable versions into main.

Coverage includes Getting Started; PR Scanning, SCA, DeepScan, Secrets and IaC; languages and coverage; Reporting, Risk Register, CSI, configuration, policies, context, feedback, blocking and permissions; MCP/API; webhooks, Jira, keys, remediation and DryRun Skill.

Both language editions use equivalent executable commands. Scripts use English messages explained in the walkthrough. Complete kit source is also included in the PDF appendices.

## Verification / Validação

[Local verification report](laboratorios/verificacao-local.json): 151 Bash blocks per language checked for syntax and command parity; safe application tests; expected SQL injection regression failure; restored tests; non-secret session generation; Jira payload conversion; local synthetic webhook delivery, duplicate handling and wrong-path rejection.

Live DryRun scans, Jira issue creation and Codex execution in the student's accounts were not performed during authoring. Those exercises require the student's credentials, permissions and configuration. Publishing these materials is separate from executing the labs.

## Sources / Fontes

Based primarily on the 25 official DryRun PDFs supplied for the course, dated 2026-10-20. Edition 2 adds beginner-oriented walkthroughs and an English edition. Sources and official external references are listed in each guide. This is independent training material, not an official vendor publication.
