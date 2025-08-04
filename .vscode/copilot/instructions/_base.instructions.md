---
applyTo: '**'
---

# Instruções Copilot

- Sempre garanta qualidade de código e documentação em nível industrial e de produção.
- Siga rigorosamente os padrões PEP 8, PEP 20, PEP 257 e PEP 484.
- Utilize Python 3.13.x ou superior.
- Prefira o explícito ao implícito e o simples ao complexo.
- Prefira estilos de programação funcional e determinístico.
- Sempre utilize type hints nas assinaturas de parâmetros e retornos das funções.
- Uma função deve fazer apenas uma coisa e fazê-la bem.
- Não utilize uma classe se uma função for suficiente.
- Sempre use nomes descritivos e significativos para variáveis, funções e classes.
- O código jamais deve falhar silenciosamente; falhe imediatamente e de forma explícita.
- Não propague dados inválidos esperando que outra parte do código trate o erro.
- Comentários só devem ser usados quando a lógica não for trivial.
- As docstrings devem ser objetivas, sem prolixidade ou redundância.
- Nunca assuma informações não explicitadas.
- Faça, mostre e edite apenas o que for solicitado.
- Sempre inicie sua resposta explicando ao usuário o que será feito e como será feito.
- Execute `uv run ruff format .` para formatar o código.
- Execute `uv run ruff check . --fix` para corrigir problemas de lint.
- Use mensagens de commit seguindo o padrão `conventional commits`.
- Utilize `Pydantic 2.x` para validação de dados.
- Evite o uso de `dict` ou `Any` sem validação imediata e mapeamento para `TypedDict` ou `BaseModel` do `Pydantic 2.x`.
- Utilize a tool `context7` para buscar documentação de pacotes e bibliotecas.
- Não pré-otimize.
- Não utilize gambiarras ou soluções temporárias para contornar problemas.
- Não implemente mockups ou dados fictícios sem solicitação explícita.
- O ano atual é 2025.
