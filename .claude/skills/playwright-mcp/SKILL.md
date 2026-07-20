---
name: playwright-mcp
description: Use ao desenvolver ou depurar UI web para ver o resultado real no browser — screenshots, interação e iteração visual com Playwright em vez de codar às cegas.
---

# playwright-mcp — Feedback ao vivo no browser

## Princípio
Nunca entregue UI sem tê-la visto renderizada. Código que "deveria funcionar" não é evidência.

## Processo
1. **Suba a aplicação** (dev server ou arquivo estático) e abra com Playwright (MCP do Playwright se disponível; senão, script Node/Python com o Chromium pré-instalado).
2. **Ciclo de iteração:** alterar código → screenshot → comparar com a intenção → corrigir → repetir. Não acumule várias mudanças sem verificar.
3. **Capture os estados que importam:**
   - Viewports: 375px (mobile), 768px (tablet), 1440px (desktop).
   - Estados interativos: hover, focus visível, formulário com erro, loading, vazio.
   - Temas claro e escuro, se existirem.
4. **Verifique o console:** erros de JS e requests falhando invalidam a entrega mesmo que o screenshot pareça bom.
5. **Interaja de verdade:** clique nos botões, preencha os formulários, navegue o fluxo principal — não apenas fotografe a página inicial.

## Notas do ambiente
- Chromium já está instalado em `/opt/pw-browsers/chromium` (`PLAYWRIGHT_BROWSERS_PATH` configurado). Não rode `playwright install`.
- Envie os screenshots relevantes ao usuário quando forem a evidência da entrega.
