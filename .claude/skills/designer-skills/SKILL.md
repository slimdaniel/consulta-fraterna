---
name: designer-skills
description: Use ao entregar design para implementação por outra pessoa/equipe — gera especificações de handoff profissionais com tokens, medidas, estados e comportamento responsivo.
---

# designer-skills — Specs de handoff profissional

## Objetivo
Nenhuma decisão de design deve ficar na cabeça: o handoff permite implementar sem perguntar nada de volta.

## Estrutura da spec
1. **Visão geral** — o que é o componente/tela, onde aparece, variantes existentes.
2. **Tokens usados** — tabela com nome do token → valor (cores, fontes, espaçamentos, raios, sombras). Nunca valores soltos sem nome.
3. **Anatomia** — lista numerada das partes do componente com medidas (padding, gap, tamanhos) em px, todas no grid de 4px.
4. **Estados** — default, hover, focus, active, disabled, loading, erro, vazio. Para cada um: o que muda (token a token) e a transição (duração + curva).
5. **Comportamento responsivo** — o que acontece em cada breakpoint; o que trunca, quebra, esconde ou reordena.
6. **Conteúdo dinâmico** — limites de caracteres, comportamento com texto longo/curto, estados com 0, 1 e N itens.
7. **Acessibilidade** — roles/labels ARIA, ordem de foco, contraste verificado, alvo de toque mínimo 44×44px.

## Regra de ouro
Se o implementador puder fazer duas interpretações diferentes de algum ponto, a spec está incompleta.
