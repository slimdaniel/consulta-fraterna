---
name: figma-implement
description: Use ao implementar em código um design vindo do Figma (screenshot, export ou link). Garante tradução fiel do design, não uma aproximação.
---

# figma-implement — Tradução direta do design

## Princípio
O design do Figma é a especificação, não uma sugestão. A meta é diferença visual zero.

## Processo
1. **Extraia os tokens antes de codar:** cores exatas, famílias/pesos/tamanhos de fonte, espaçamentos, raios de borda, sombras. Liste-os primeiro como variáveis CSS.
2. **Meça, não estime.** Se tiver acesso ao arquivo/MCP do Figma, leia os valores dos frames. Se for screenshot, meça proporções na imagem.
3. **Reproduza a estrutura de auto-layout** como flexbox/grid: direção, gap, padding e alinhamento do Figma mapeiam 1:1.
4. **Estados e variantes:** implemente todos os estados desenhados (hover, focus, disabled, erro). Se um estado não foi desenhado, derive-o dos tokens e sinalize a suposição.
5. **O que o design não define** (breakpoints não desenhados, conteúdo dinâmico maior que o mock): resolva mantendo os tokens e a intenção, e liste as decisões tomadas.

## Verificação
- Compare lado a lado (screenshot do resultado vs. design) antes de entregar.
- Divergências intencionais (acessibilidade, conteúdo real) devem ser listadas explicitamente na entrega.
