---
mode: 'agent'
description: 'Refatorar trecho de código'
tools: ['changes', 'fetch', 'codebase', 'githubRepo', 'problems', 'runCommands', 'usages']
---

# Você é obrigado a seguir as instruções na ordem exata em que são apresentadas:

0. Você deverá alterar tão somente o que é pedido e apresentado. Não faça alterações adicionais no código, a menos que seja explicitamente solicitado.
1. Entenda o que deve ser refatorado e como deve ser feito. Se o usuário não entrar com uma descrição, pare aqui, negue-se a fazer qualquer alteração e informe que não há instruções suficientes.
2. Entenda o que deve ser refatorado e como deve ser feito. Se o usuário entrar com uma descrição, utilize a tool #usages para identificar os usos daqueles trechos de código.
3. Existe um trecho de código que deve ser alterado e é comum a vários pontos do código? Se sim, altere-o primeiro.
4. A sua refatoração vai causar algum erro? Se sim, repense a sua abordagem e volte ao passo 1.
5. Se é necessário refatorar uma módulo, inicie pelas assinaturas e interfaces, depois implemente as mudanças no corpo do módulo. Leve em consideração o contexto ao qual se encontra o módulo.
6. Se é necessário refatorar uma função, inicie pela assinatura e depois implemente as mudanças no corpo da função. Leve em consideração o contexto ao qual se encontra a função.
7. Se é necessário refatorar uma classe, inicie pela assinatura e depois implemente as mudanças no corpo da classe. Leve em consideração o contexto ao qual se encontra a classe.
8. Se é necessário refatorar um trecho de código, leve em consideração o contexto ao qual se encontra.
9. Por fim, aplique as alterações necessárias no código.
10. Se você alterou o código, verifique se as alterações foram aplicadas corretamente através da tool `#changes`.
11. Se as alterações não foram aplicadas corretamente, repita em ordem os passos 1 a 10 até que as alterações sejam aplicadas corretamente.
