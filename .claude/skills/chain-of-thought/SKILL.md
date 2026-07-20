---
name: chain-of-thought
description: Use em problemas complexos, decisões com trade-offs ou cálculos — força raciocínio passo a passo explícito antes da resposta final.
---

# chain-of-thought — Raciocínio passo a passo

## Quando ativar
Problemas com múltiplas etapas, cálculos, decisões entre alternativas, diagnóstico de erros, ou qualquer pergunta onde uma resposta imediata teria risco real de estar errada.

## Protocolo
1. **Decomponha antes de responder:** liste as sub-perguntas que precisam de resposta para chegar à conclusão.
2. **Resolva na ordem de dependência:** cada passo declara o que assume dos anteriores. Se um passo depende de um dado que você não tem, busque o dado (ferramenta, arquivo, pergunta) em vez de supor.
3. **Mostre o trabalho nos pontos de risco:** cálculos por extenso, unidades explícitas, casos extremos testados (0, 1, negativo, vazio, máximo).
4. **Cheque a conclusão contra o problema original:** a resposta final responde exatamente o que foi perguntado? Uma verificação independente (estimativa de ordem de grandeza, caminho alternativo) bate com o resultado?
5. **Só então responda**, levando a conclusão para o topo e o raciocínio como suporte.

## Regras
- Não esconda incerteza: se um passo é suposição, marque como suposição.
- Se dois caminhos de raciocínio divergem, pare e resolva a divergência — não escolha o mais conveniente.
- Raciocínio longo não é enfeite: cada passo deve mudar algo na conclusão; corte o que não muda.
