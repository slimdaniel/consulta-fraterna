---
name: generative-ui
description: Use ao gerar interfaces dinâmicas a partir de dados ou respostas — widgets responsivos que se adaptam ao conteúdo (listas, cards, formulários, visualizações) em vez de texto corrido.
---

# generative-ui — Widgets responsivos

## Princípio
Quando a resposta é estruturada (comparação, lista de opções, série de dados, formulário), gere um **widget** adequado à estrutura, não parágrafos de texto.

## Mapeamento estrutura → widget
| Estrutura do conteúdo | Widget |
|---|---|
| Comparação de 2–4 opções | Cards lado a lado com prós/contras |
| Série temporal / quantidades | Gráfico (linha/barra) com 1 mensagem anotada |
| Passos de um processo | Stepper/timeline vertical |
| Coleção de itens homogêneos | Grid de cards com hierarquia interna |
| Escolha do usuário | Grupo de botões/opções clicáveis |
| Dados tabulares curtos | Tabela; longos → tabela com busca/ordenação |

## Regras de construção
1. **O dado dita o layout:** projete para 0, 1, N e "muitos" itens — o widget não pode quebrar quando o conteúdo variar.
2. **Responsivo por padrão:** grid com `auto-fit/minmax`, sem larguras fixas; teste mentalmente em 375px.
3. **Hierarquia interna:** cada card/item tem 1 elemento dominante (número, título) e detalhes secundários menores.
4. **Autocontido:** HTML/CSS/JS inline, sem dependências externas (CSP de artifacts bloqueia CDN).
5. **Acessível:** HTML semântico, contraste AA, navegável por teclado.
