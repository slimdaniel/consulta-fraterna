---
name: banana-claude
description: Use ao escrever ou melhorar prompts de geração de imagem. Aplica uma fórmula de 5 partes que produz prompts consistentes e controláveis.
---

# banana-claude — Fórmula de prompt em 5 partes

Todo prompt de imagem deve ser montado nesta ordem:

## A fórmula
1. **Sujeito** — o que aparece, com especificidade: "uma manopla de moto em close macro" > "uma peça".
2. **Estilo** — direção visual nomeada: "fotografia de produto editorial", "ilustração flat vetorial", "render 3D clay", "aquarela solta".
3. **Composição** — enquadramento e arranjo: ângulo (top-down, 3/4, close), regra dos terços ou centralizado, espaço negativo para texto se for peça de design.
4. **Luz** — qualidade e direção: "luz difusa de estúdio", "golden hour lateral", "neon dual-tone azul/magenta", "sombra dura de meio-dia".
5. **Qualidade/técnica** — acabamento: "alta nitidez, fundo limpo", "grão de filme sutil", "8k render", "paleta limitada a 3 cores".

## Exemplo montado
> "Manopla de guidão de moto em borracha preta [sujeito], fotografia de produto editorial [estilo], close 3/4 sobre fundo cinza com espaço negativo à direita [composição], luz difusa de estúdio com reflexo suave [luz], alta nitidez e fundo limpo [qualidade]."

## Regras
- Uma ideia por prompt; para comparar alternativas, gere prompts separados variando **uma** parte da fórmula.
- Especifique proporção/dimensão para o uso final.
- Prefira descrever o que **deve** aparecer; use negações só para vícios recorrentes do modelo.
