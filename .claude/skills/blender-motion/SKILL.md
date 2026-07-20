---
name: blender-motion
description: Use para criar cenas e animações 3D no Blender via scripting Python (bpy) — modelagem procedural, materiais, câmera e render sem interface gráfica.
---

# blender-motion — Cenas 3D via Python

## Execução
Rode headless: `blender --background --python cena.py`. Se o Blender não estiver instalado no ambiente, avise e entregue o script pronto para o usuário rodar localmente.

## Estrutura padrão do script
1. **Limpeza:** remova a cena default (`bpy.ops.object.select_all` → `delete`) para partir do zero determinístico.
2. **Modelagem procedural:** primitivas (`bpy.ops.mesh.primitive_*`) + modificadores (Subdivision, Bevel, Array, Solidify) em vez de malhas manuais.
3. **Materiais:** use nodes via `material.node_tree`; para estilo "clay render", Principled BSDF com roughness 0.6–0.8 e cores da paleta do projeto.
4. **Luz em 3 pontos:** key (Area forte), fill (fraca, oposta), rim (atrás, para contorno). Ou um HDRI para realismo rápido.
5. **Câmera:** posicione e aponte com constraint `TRACK_TO` no objeto principal; distância focal 50–85mm para produto.
6. **Animação:** `obj.keyframe_insert(data_path="location", frame=n)`; interpolação com F-Curves; 30fps.
7. **Render:** Cycles para qualidade final (128–256 samples + denoise), Eevee para iteração rápida.

## Regras
- Parâmetros no topo do script (dimensões, cores, frames) — a cena inteira deve regenerar ao mudar constantes.
- Renderize um frame de preview em baixa resolução antes do render completo.
