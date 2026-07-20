---
name: claude-remotion
description: Use ao animar títulos e textos em vídeos Remotion — stagger de caracteres/palavras, timing de entrada e hierarquia temporal de títulos.
---

# claude-remotion — Stagger e timing de títulos

## Padrão de stagger
Anime títulos por partes (caracteres, palavras ou linhas), nunca o bloco inteiro de uma vez:

```tsx
const chars = title.split('');
chars.map((c, i) => {
  const delay = i * 2; // 2 frames por caractere (~60ms a 30fps)
  const prog = spring({ frame: frame - delay, fps, config: { damping: 200 } });
  return (
    <span style={{
      display: 'inline-block',
      opacity: prog,
      transform: `translateY(${(1 - prog) * 30}px)`,
    }}>{c === ' ' ? ' ' : c}</span>
  );
});
```

## Regras de timing
- **Stagger:** 1–3 frames por caractere; 3–5 por palavra; 5–8 por linha. Títulos longos → stagger menor.
- **Hierarquia temporal:** título entra primeiro, subtítulo 10–15 frames depois, CTA/detalhe por último. O olho segue a ordem de entrada.
- **Duração em cena:** o texto fica legível parado por no mínimo `nº de palavras × 10` frames antes de sair.
- **Saída mais rápida que a entrada** (~60% da duração), com stagger na direção oposta ou em bloco.

## Acabamento
- Entradas com `translateY` sutil (20–40px) + opacidade; evite escala exagerada.
- `overflow: hidden` no contêiner para efeitos de "revelar de trás da linha".
- Alinhe momentos-chave dos títulos a batidas do áudio quando houver trilha.
