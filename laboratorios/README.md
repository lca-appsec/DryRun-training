# Kit do treinamento DryRun Security

Leia o PDF antes de executar os laboratórios. Os arquivos são exemplos autorais;
não há credenciais incluídas e nenhum script envia dados automaticamente ao Jira.

- lab.sh: funções Bash do curso; carregue com `source "$KIT/lab.sh"`.
- app.py: aplicação local segura, usando apenas Python padrão.
- test_app.py: teste funcional e teste de regressão de SQL injection.
- change.py: alterna a consulta de app.py entre segura e vulnerável, somente no lab.
- receiver.py: captura webhooks em `.evidence/events`; não é serviço de produção.
- jira_payload.py: gera payload Jira v3 de um item em `results` para revisão.
- event-example.json: evento sintético para testar a transformação.
- treinamento-fonte.md: versão editável do conteúdo do PDF.
- verificacao-local.json: resumo dos testes executados na autoria.

Use um repositório privado dedicado. Apenas app.py e test_app.py são copiados
para a base inicial. Os demais arquivos ficam fora do repositório analisado.
Não mescle código vulnerável na main. As funções lab_* não são uma CLI DryRun.

Execução dos testes da base segura, na pasta que contém os dois arquivos:

```bash
python3 -m unittest -v
```

As integrações reais exigem suas próprias credenciais e não foram executadas
nas suas contas durante a criação deste material.
