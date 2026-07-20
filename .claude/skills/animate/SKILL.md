---
name: animate
description: Use ao adicionar animações, transições ou microinterações em interfaces web. Define curvas, durações e princípios de microtransição.
---

# animate — Curvas de microtransição

## Durações padrão
| Tipo | Duração |
|---|---|
| Micro-feedback (hover, toggle) | 100–150ms |
| Transição de estado (abrir menu, tab) | 200–300ms |
| Entrada/saída de elementos | 300–400ms |
| Transição de página/layout | 400–600ms |

Nunca ultrapasse 600ms para interações funcionais.

## Curvas (easing)
- **Entrada de elementos:** `cubic-bezier(0.0, 0.0, 0.2, 1)` (ease-out) — chega desacelerando.
- **Saída de elementos:** `cubic-bezier(0.4, 0.0, 1, 1)` (ease-in) — sai acelerando.
- **Movimento na tela:** `cubic-bezier(0.4, 0.0, 0.2, 1)` (standard) — natural.
- **Elástico/expressivo:** `cubic-bezier(0.34, 1.56, 0.64, 1)` — use com parcimônia, só em momentos de celebração.
- Nunca use `linear` para movimento (só para opacidade/cor contínuas).

## Princípios
1. Anime no máximo 2 propriedades por elemento; prefira `transform` e `opacity` (compostas na GPU).
2. Elementos que entram juntos devem ter *stagger* de 30–60ms entre si.
3. Toda animação precisa de propósito: orientar atenção, dar feedback ou expressar continuidade espacial.
4. Respeite `prefers-reduced-motion` — forneça alternativa sem movimento.
