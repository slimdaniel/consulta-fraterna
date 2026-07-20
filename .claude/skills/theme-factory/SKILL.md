---
name: theme-factory
description: Use para gerar temas de cor completos (rampas claras/escuras, tokens semânticos) a partir de uma cor de marca ou direção estética.
---

# theme-factory — Rampas de cor automáticas

## Processo
1. **Parta de 1 cor-semente** (cor da marca ou escolhida pela direção estética).
2. **Gere a rampa em OKLCH**, variando a luminosidade em passos regulares e mantendo o matiz:
   - `50` (L≈0.97) · `100` (0.93) · `200` (0.87) · `300` (0.78) · `400` (0.68) · `500` (0.58, a cor-semente) · `600` (0.50) · `700` (0.42) · `800` (0.34) · `900` (0.26) · `950` (0.18)
   - Reduza levemente o chroma (C) nas pontas da rampa para evitar cores sujas.
3. **Gere neutros com matiz** — cinzas com 2–5% do chroma da cor-semente, mesmo H.
4. **Derive tokens semânticos** (nunca use a rampa direto na UI):
   - `--bg`, `--bg-subtle`, `--surface`, `--border`, `--text`, `--text-muted`, `--primary`, `--primary-hover`, `--accent`, `--danger`, `--success`, `--warning`.
5. **Tema escuro não é inversão:** reduza o chroma geral, clareie a cor primária 1–2 passos (para contraste sobre fundo escuro) e use superfícies em camadas (bg < surface < surface-raised).

## Verificação
- Texto sobre cada fundo do tema passa WCAG AA (4.5:1).
- Estados hover/active distinguíveis em ambos os temas.
- Entregue como CSS custom properties com `@media (prefers-color-scheme: dark)` e/ou `[data-theme]`.
