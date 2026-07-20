---
name: design-motion
description: Use para auditar e revisar animações existentes em uma interface. Avalia o movimento por 3 lentes — propósito, física e performance — e reporta correções.
---

# design-motion — Auditor de movimento (3 lentes)

Ao revisar qualquer animação existente, avalie por estas 3 lentes e reporte um veredito por lente:

## Lente 1 — Propósito
- Esta animação orienta a atenção, dá feedback ou cria continuidade espacial?
- Se a resposta for "é só decoração": **remover** (ou reduzir a 100ms sutil).
- O usuário espera algo enquanto ela roda? Se sim, ela está mascarando lentidão ou causando lentidão?

## Lente 2 — Física
- O movimento tem aceleração/desaceleração naturais (nada aparece ou para "seco")?
- Objetos relacionados se movem como um sistema coerente (mesma direção de origem, timings relacionados)?
- Distâncias maiores levam proporcionalmente mais tempo?

## Lente 3 — Performance
- Anima apenas `transform`/`opacity`? Propriedades que causam reflow (`width`, `height`, `top`, `left`, `margin`) são proibidas em animação contínua.
- Roda a 60fps em dispositivo médio? Verifique com DevTools/Playwright se disponível.
- Há `will-change` vazando (aplicado permanentemente em vez de só durante a animação)?

## Formato do relatório
Para cada animação auditada: `[elemento] — Propósito: ✓/✗ · Física: ✓/✗ · Performance: ✓/✗ — correção sugerida`.
