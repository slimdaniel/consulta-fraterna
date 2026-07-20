---
name: brandkit-sync
description: Use para manter um guia de marca reutilizável no projeto (brand.md / tokens) e aplicá-lo automaticamente em toda entrega visual — sites, peças, slides, vídeos.
---

# brandkit-sync — Guia de marca reutilizável

## Princípio
A identidade da marca é definida **uma vez**, num arquivo versionado, e toda entrega visual lê dele. Nada de redefinir cores "de cabeça" a cada tarefa.

## Estrutura do guia (`brand/brand.md` no repositório)
```md
# Marca: <nome>
## Essência
Posicionamento em 1 frase · 3 adjetivos
## Cores
primary: oklch(...) #hex · accent: ... · neutros: ...
## Tipografia
Display: <família, pesos> · Texto: <família, pesos> · Escala: 12/14/16/20/24/32/48
## Voz
somos/não-somos (3 pares) · exemplos de frase
## Regras
raio de borda padrão · estilo de ícones · estilo de fotografia/ilustração
```

## Fluxo de trabalho
1. **Antes de qualquer entrega visual, leia `brand/brand.md`.** Se não existir, crie-o com o usuário (use a skill `brandkit`) antes de produzir peças.
2. **Aplique os tokens literalmente** — cores, fontes e raios vêm do guia, nunca inventados na hora.
3. **Divergência intencional** (ex.: campanha especial) deve ser anotada no próprio guia, numa seção "Exceções".
4. **Evolução:** quando o usuário aprovar uma decisão visual nova, atualize o guia no mesmo commit — o guia acompanha a marca, não fica para trás.
