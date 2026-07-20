---
name: figma-mcp
description: Use quando houver um MCP do Figma conectado — para ler frames, extrair tokens e valores exatos do arquivo de design e gerar código fiel a partir deles.
---

# figma-mcp — Lê frames, comita código

## Pré-requisito
Um servidor MCP do Figma conectado (ex.: Figma Dev Mode MCP). Se não houver, diga isso e caia para a skill `figma-implement` (trabalho a partir de screenshot/export).

## Fluxo
1. **Localize o frame:** peça ao usuário o link do frame/node específico (não o arquivo inteiro) e leia-o via MCP.
2. **Extraia dados estruturados, não interpretação visual:**
   - Variáveis/estilos definidos no arquivo (cores, textos, efeitos) → mapeie para tokens CSS com os mesmos nomes.
   - Auto-layout (direção, gap, padding, alinhamento) → flexbox/grid 1:1.
   - Medidas exatas de cada camada; nada de estimar.
3. **Respeite a nomenclatura do designer:** nomes de componentes e variantes do Figma viram nomes de componentes no código.
4. **Componha, não duplique:** instâncias de um componente Figma viram usos de um único componente no código.
5. **Verifique visualmente:** renderize o resultado (skill `playwright-mcp`) e compare com o export do frame antes de commitar.
6. **Comite** com mensagem referenciando o frame implementado.

## Sinalizações obrigatórias
- Valores fora do grid/tokens no próprio Figma: implemente fiel, mas liste como possível inconsistência do design.
- Estados não desenhados que você derivou: liste as suposições na entrega.
