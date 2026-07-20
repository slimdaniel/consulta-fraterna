---
name: token-budgets
description: Use em tarefas longas ou com muito material para gerenciar o orçamento de contexto — decidir o que ler inteiro, o que resumir e o que deixar de fora.
---

# token-budgets — Conta de tokens do contexto

## Princípio
Contexto é orçamento finito. Cada leitura integral de arquivo grande é um gasto que compete com a capacidade de raciocinar no fim da tarefa.

## Regras de leitura
1. **Busque antes de ler:** use grep/glob para localizar o trecho relevante; leia só a faixa de linhas necessária, não o arquivo inteiro.
2. **Arquivos > 500 linhas:** leia por partes direcionadas; nunca "por garantia".
3. **Outputs de comandos:** filtre na origem (`head`, `grep`, `--quiet`) em vez de despejar logs inteiros no contexto.
4. **Não releia o que já sabe:** se o conteúdo já passou pela conversa, referencie de memória; releitura só se houve edição externa.

## Regras de escrita
1. **Resuma marcos:** ao concluir uma etapa longa, registre em 3–5 linhas o que foi decidido/feito (no chat ou num arquivo de notas), para sobreviver a sumarizações de contexto.
2. **Anote em arquivo o que não pode se perder:** decisões, seeds, valores medidos — arquivos persistem; contexto, não.

## Sinais de orçamento estourando
Conversa muito longa, mesmos arquivos relidos, respostas repetindo contexto. Reação: consolidar estado num arquivo de notas, e propor dividir a tarefa (skill `task-decomposition`).
