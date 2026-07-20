---
name: algorithmic-art
description: Use para criar arte generativa/algorítmica — flow fields, ruído, sistemas de partículas e padrões matemáticos — como texturas, fundos ou peças autorais.
---

# algorithmic-art — Flow fields na matemática

## Técnicas centrais
1. **Flow fields:** gere um campo vetorial com ruído Perlin/simplex (`ângulo = noise(x·esc, y·esc) · 2π`) e trace milhares de partículas seguindo o campo. Varie: escala do ruído (0.001–0.01), comprimento dos traços, espessura por velocidade.
2. **Ruído em camadas (fBm):** some oitavas de ruído para texturas orgânicas (nuvens, terreno, mármore).
3. **Sistemas de partículas:** atração/repulsão simples geram órbitas e aglomerados; adicione atrito para estabilizar.
4. **Padrões matemáticos:** curvas de Lissajous, espirais de Fermat (`r = c·√n`, `θ = n·137.5°`), truchet tiles, subdivisão recursiva.

## Regras de qualidade
- **Semente fixa e registrada** (`seed`) — todo output deve ser reproduzível; guarde a seed no nome do arquivo.
- **Paleta restrita:** 2–4 cores escolhidas antes; arte generativa boa é matemática solta + cor disciplinada.
- **Densidade importa:** poucos elementos = pobre; demais = ruído. Itere na quantidade (geralmente milhares de traços finos com baixa opacidade).
- **Margens:** deixe respiro nas bordas ou sangre deliberadamente — nunca "quase encostando".

## Implementação
Python (Pillow/numpy → PNG) ou JS (canvas/SVG). Renderize em 2× a resolução final. Gere 3–4 variações de seed e deixe o usuário escolher.
