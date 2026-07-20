---
name: nano-banana
description: Use quando o usuário quiser gerar imagens a partir de texto pelo terminal, usando uma API de geração de imagem (ex.: Gemini "Nano Banana" ou similar) configurada no ambiente.
---

# nano-banana — Texto-pra-imagem no terminal

## Pré-requisito
Uma chave de API de geração de imagem disponível no ambiente (ex.: `GEMINI_API_KEY` para o modelo de imagem do Gemini, apelidado "Nano Banana"). Se não houver chave configurada, diga isso claramente e ofereça alternativas locais (SVG/canvas programático) em vez de fingir gerar.

## Processo
1. **Refine o prompt antes de chamar a API** usando a fórmula da skill `banana-claude` (sujeito → estilo → composição → luz → qualidade).
2. **Chame a API via script** (curl ou Python) no terminal, salvando a imagem no diretório de trabalho com nome descritivo (`hero-banner-v1.png`).
3. **Gere variações com controle:** mude 1 variável por vez (ângulo, paleta, estilo) e nomeie os arquivos de forma comparável (`-v1`, `-v2-luz-quente`).
4. **Mostre o resultado** ao usuário (envie o arquivo) e itere a partir do feedback.

## Boas práticas
- Peça dimensões/proporção certas para o uso final (1:1 post, 16:9 hero, 9:16 story) em vez de cortar depois.
- Guarde o prompt usado junto do arquivo (ex.: `hero-banner-v1.prompt.txt`) para reprodutibilidade.
- Nunca gere imagens de pessoas reais identificáveis ou marcas de terceiros.
