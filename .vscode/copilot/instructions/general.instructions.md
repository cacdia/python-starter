---
applyTo: '**'
---

# Copilot Instructions

- Estamos em 2025
- Nunca assuma informações
- Faça tão somente o que é pedido
- Prefira o explícito ao implícito
- Garanta sempre que a qualidade do código seja nível de produção industrial
- Garanta sempre que a qualidade da documentação seja nível de produção industrial
- Sempre que tratar de Python, utilize o guia [python.instructions.md](./.vscode/copilot/instructions/python.instructions.md) para instruções gerais
- Sempre que tratar de Python, utilize o [uv](https://docs.astral.sh/uv/) para executar arquivos e gerenciar versões, ambientes virtuais e pacotes
- Sempre que tratar de Python, utilize o [ruff](https://docs.astral.sh/ruff/) para lintar e formatar o código
- Sempre que tratar de Python, utilize o [pyproject.toml](./pyproject.toml) para definir as configurações do projeto
- Execute `uv run ruff format . --check` para verificar a formatação do código
- Execute `uv run ruff check . --fix` para corrigir problemas de lint
