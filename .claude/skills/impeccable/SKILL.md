---
name: impeccable
description: Use ao refinar ou revisar CSS/estilos de uma interface para nível de acabamento profissional. Aplica cor em OKLCH, grid de 4px e regras de consistência pixel-perfect.
---

# impeccable — OKLCH e grids de 4px

## Regras de cor
1. Defina cores em **OKLCH** (`oklch(L C H)`) — luminosidade perceptual uniforme facilita criar variações consistentes.
2. Derive estados (hover, active, disabled) alterando apenas L e C, mantendo o H (matiz) fixo.
3. Contraste mínimo: 4.5:1 para texto normal, 3:1 para texto grande e elementos de UI (WCAG AA).
4. Nunca use `#000` puro sobre `#fff` puro — use neutros com leve matiz da cor da marca.

## Regras de espaçamento
1. **Tudo em múltiplos de 4px** (4, 8, 12, 16, 24, 32, 48, 64…). Sem valores mágicos como `13px` ou `margin: 7px`.
2. Espaçamento interno (padding) sempre menor ou igual ao externo (margin/gap) do mesmo contexto.
3. Elementos relacionados ficam mais próximos entre si do que de elementos não relacionados (lei da proximidade).

## Regras de tipografia
1. Escala tipográfica modular (ex.: 12/14/16/20/24/32/48).
2. `line-height` sem unidade (1.2 para títulos, 1.5–1.6 para corpo).
3. Comprimento de linha entre 45–75 caracteres.

## Verificação
Antes de entregar, varra o CSS procurando: valores fora do grid de 4px, cores fora da paleta definida, contrastes reprovados e tamanhos de fonte fora da escala.
