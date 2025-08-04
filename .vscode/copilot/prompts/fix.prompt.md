---
mode: 'agent'
description: 'Corrigir erro no código'
tools: ['changes', 'fetch', 'codebase', 'githubRepo', 'problems', 'runCommands', 'usages']
---

# Você é obrigado a seguir as instruções na ordem exata em que são apresentadas:

0. Você deverá corrigir tão somente o que é pedido e apresentado. Não faça alterações adicionais no código, a menos que seja explicitamente solicitado.
1. Entenda a mensagem de erro casa tenha sido fornecida. Se o usuário não entrar com mensagem de erro, verifique o código através da tool `#problems`.
2. Existe um erro que causa todos os outros erros? Se sim, corrija-o primeiro.
3. Existe um trecho de código que deve ser alterado e é comum a vários erros? Se sim, corrija-o primeiro.
4. Aplique as correções necessárias no código até que o erro em questão seja resolvido.
5. Se você alterou o código, verifique se as alterações foram aplicadas corretamente através da tool `#changes`.
6. Se os erros persistirem ou surgirem novos erros, repita em ordem os passos 1 a 5 até que todos os erros sejam resolvidos.
