---
name: remotion-superpowers
description: Use para criar vídeos programáticos com Remotion (React) — motion graphics, vídeos de dados, intros e animações renderizadas em MP4.
---

# remotion-superpowers — Estúdio de vídeo em React

## Setup
- Projeto: `npx create-video@latest` ou adicione `remotion @remotion/cli` a um projeto React existente.
- Estrutura: cada vídeo é uma `<Composition>` com `id`, `durationInFrames`, `fps` (use 30), `width`/`height`.

## Padrões fundamentais
1. **Tudo deriva do frame atual:** `const frame = useCurrentFrame()` — nunca use estado/efeitos para animar; a renderização precisa ser determinística por frame.
2. **Interpolação:** `interpolate(frame, [início, fim], [de, até], { extrapolateRight: 'clamp' })` para posição, opacidade e escala.
3. **Springs para vida:** `spring({ frame, fps, config: { damping: 200 } })` para entradas com física natural.
4. **Sequências:** `<Sequence from={30} durationInFrames={60}>` organiza a linha do tempo; componha cenas como componentes.
5. **Áudio:** `<Audio src={...} />` com `startFrom`; sincronize cortes com batidas definindo os frames-chave como constantes nomeadas.

## Qualidade
- Constantes de timing no topo do arquivo (`const INTRO_END = 45`) — nada de números mágicos espalhados.
- Preview com `npx remotion studio`; render final com `npx remotion render <id> out.mp4`.
- Tipografia e cor seguem as mesmas regras das skills de design (grid, paleta limitada, contraste).
