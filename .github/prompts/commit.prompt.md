---
mode: 'agent'
description: 'Versionar o projeto usando Conventional Commits'
---

1. Verifique cada uma das alterações que você fez no [projeto](./) através do comando `git status -uall`.
2. Entenda o que cada alteração representa: se é uma nova funcionalidade, uma correção de bug, uma melhoria, etc. Para isso execute o comando `git --no-pager diff` para ver as diferenças entre os arquivos modificados e a última versão commitada.
3. Certifique-se de que as alterações estão prontas para serem commitadas e que não há erros ou problemas pendentes.
4. PARA TODOS ARQUIVOS PENDENTES, Escreva o commit na forma

   ```
   <tipo>[escopo][!]: <descrição>
   ```

   – tipo (`feat`, `fix`, etc.), escopo opcional em parênteses, `!` para indicar breaking change.
5. [Opcional] Após uma linha em branco, acrescente o corpo para contexto e detalhes.
6. [Opcional] Após outra linha em branco, acrescente footers:

   * `BREAKING CHANGE: descrição`
   * e/ou `<token>: valor` (e.g. `Refs: #123`, `Reviewed-by: X`) .
7. Submeta o commit através do comando `git commit -m "<mensagem do commit>"`.
