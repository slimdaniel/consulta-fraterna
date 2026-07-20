---
name: ae-motion
description: Use para automatizar o After Effects com scripts JSX (ExtendScript) — criar composições, camadas, keyframes e expressões programaticamente.
---

# ae-motion — Scripts JSX no After Effects

## Contexto
Scripts `.jsx` rodam no AE via `File > Scripts > Run Script File`. Entregue o arquivo pronto com instruções de execução — o AE roda na máquina do usuário, não neste ambiente.

## Estrutura padrão
```jsx
app.beginUndoGroup("Nome da acao");        // toda ação num undo group único
var comp = app.project.items.addComp("Titulo", 1920, 1080, 1, 10, 30);
var layer = comp.layers.addText("Olá");
var pos = layer.property("Position");
pos.setValueAtTime(0, [960, 640]);
pos.setValueAtTime(1, [960, 540]);
app.endUndoGroup();
```

## Padrões essenciais
- **Easing programático:** `setTemporalEaseAtKey` com `KeyframeEase(velocidade, influência)` — influência 33–75 para curvas suaves.
- **Expressões para movimento vivo:** aplique via `property.expression`, ex.: inércia pós-keyframe (overshoot) e `wiggle()` sutil para câmera.
- **Stagger de camadas:** loop deslocando `layer.startTime` em 2–4 frames por item.
- **Null como controlador:** crie um Null com Slider Controls e aponte expressões para ele — o usuário ajusta timing sem reabrir o script.

## Regras
- Sempre `beginUndoGroup`/`endUndoGroup` — o usuário precisa desfazer com 1 Ctrl+Z.
- Cheque `app.project.activeItem` antes de assumir composição ativa.
- Parâmetros (textos, cores, durações) declarados no topo do script.
