---
name: canvas-design
description: Use para criar arte visual, posters, capas e peças gráficas de forma programática (SVG ou canvas), produzindo PNGs de qualidade a partir de vetores editáveis.
---

# canvas-design — PNGs vetoriais editáveis

## Princípio
Peças gráficas são construídas como **vetor editável primeiro** (SVG ou desenho em canvas via código), e só então exportadas para PNG. Nunca "chute" pixels: cada elemento tem posição, cor e tipografia definidas em código revisável.

## Processo
1. **Defina o formato** — dimensões finais (ex.: 1080×1080 post, 1920×1080 capa) e margem de segurança (~5%).
2. **Monte um grid** — colunas/linhas explícitas; posicione tudo em coordenadas derivadas do grid, não números mágicos.
3. **Construa em camadas:** fundo → formas/textura → elementos gráficos → tipografia → detalhes finos.
4. **Tipografia como protagonista:** em peças gráficas, o texto costuma ser o elemento visual principal — trabalhe escala, peso e espaçamento com coragem.
5. **Paleta limitada:** 2–4 cores definidas antes de começar; derive variações por opacidade, não cores novas.
6. **Exporte:** renderize o SVG para PNG (ex.: `rsvg-convert`, `resvg`, Playwright screenshot ou canvas `toBuffer`) na resolução final ×2 para nitidez.

## Verificação
- Abra/renderize o resultado e olhe: alinhamentos, texto cortado, contraste.
- Entregue o PNG **e** o fonte vetorial (SVG/script), para o usuário poder editar depois.
