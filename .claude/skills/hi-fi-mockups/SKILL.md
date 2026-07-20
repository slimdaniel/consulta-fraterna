---
name: hi-fi-mockups
description: Use para criar mockups de alta fidelidade de interfaces (telas de app, sites, dashboards) como imagens apresentáveis — para validar ideias antes de implementar.
---

# hi-fi-mockups — Mockups de UI no canvas

## Objetivo
Produzir imagens de telas realistas o suficiente para decisão de stakeholder, sem construir a aplicação real.

## Processo
1. **Construa o mockup em HTML/CSS real** (uma página estática autocontida) — mais rápido e fiel do que desenhar pixels — e capture screenshot com Playwright na resolução do dispositivo alvo.
2. **Use conteúdo realista, nunca lorem ipsum:** nomes plausíveis, números com a magnitude certa, textos no idioma do produto. Dados fake mas críveis são o que separa hi-fi de wireframe.
3. **Aplique o sistema de design completo:** tokens de cor, tipografia e espaçamento das skills `impeccable`/`theme-factory`. O mockup deve parecer produto lançado.
4. **Enquadre no dispositivo:** moldura simples de browser (barra com URL) ou de celular (cantos arredondados, status bar) desenhada em CSS.
5. **Monte variações lado a lado** quando houver decisão a tomar (ex.: 2 direções de layout) — mesmo conteúdo, direções diferentes.

## Entrega
- PNG(s) em 2× para nitidez + o HTML fonte para edições futuras.
- Estados principais: a tela "feliz" sempre; vazio/erro/loading quando relevantes à decisão.
