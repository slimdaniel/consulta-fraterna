#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renderiza docs/preview.png a partir do STL — visualização do modelo.

Requer Pillow (pip install pillow). Usa algoritmo do pintor com
sombreamento difuso + especular simples, suficiente para pré-visualizar
uma peça convexa como a manopla.

Uso:
    python3 renderizar_preview.py [entrada.stl] [saida.png]
"""

import math
import struct
import sys

from PIL import Image, ImageDraw, ImageFont


def carregar_stl(caminho):
    tris = []
    with open(caminho, "rb") as f:
        f.read(80)
        n = struct.unpack("<I", f.read(4))[0]
        for _ in range(n):
            vals = struct.unpack("<12fH", f.read(50))
            v = vals[3:12]
            tris.append(((v[0], v[1], v[2]), (v[3], v[4], v[5]), (v[6], v[7], v[8])))
    return tris


def mat_rot(ax, ay, az):
    """Matriz de rotação (graus) na ordem X, Y, Z."""
    ax, ay, az = (math.radians(a) for a in (ax, ay, az))
    cx, sx, cy, sy, cz, sz = (math.cos(ax), math.sin(ax), math.cos(ay),
                              math.sin(ay), math.cos(az), math.sin(az))
    rx = ((1, 0, 0), (0, cx, -sx), (0, sx, cx))
    ry = ((cy, 0, sy), (0, 1, 0), (-sy, 0, cy))
    rz = ((cz, -sz, 0), (sz, cz, 0), (0, 0, 1))

    def mul(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                           for j in range(3)) for i in range(3))
    return mul(rz, mul(ry, rx))


def aplicar(m, v):
    return (m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2],
            m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2],
            m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2])


def subdividir(tris, aresta_max=5.0):
    """Divide triângulos grandes (algoritmo do pintor exige peças pequenas)."""
    def maior_aresta(t):
        d = []
        for a, b in ((0, 1), (1, 2), (2, 0)):
            d.append(sum((t[a][k] - t[b][k]) ** 2 for k in range(3)))
        return max(range(3), key=lambda i: d[i]), math.sqrt(max(d))

    fila = list(tris)
    prontos = []
    lim2 = aresta_max
    while fila:
        t = fila.pop()
        idx, comp = maior_aresta(t)
        if comp <= lim2:
            prontos.append(t)
            continue
        a, b = idx, (idx + 1) % 3
        c = 3 - a - b
        meio = tuple((t[a][k] + t[b][k]) / 2 for k in range(3))
        fila.append((t[a], meio, t[c]))
        fila.append((meio, t[b], t[c]))
    return prontos


def renderizar(tris, rot, tam, cor_base=(52, 54, 58), fundo=(245, 246, 248)):
    w, h = tam
    m = mat_rot(*rot)
    luz = (0.45, -0.35, 0.82)
    nl = math.sqrt(sum(c * c for c in luz))
    luz = tuple(c / nl for c in luz)

    # transforma e centraliza
    trans = []
    for t in tris:
        trans.append(tuple(aplicar(m, v) for v in t))
    xs = [v[0] for t in trans for v in t]
    ys = [v[1] for t in trans for v in t]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    escala = 0.85 * min(w / (max(xs) - min(xs)), h / (max(ys) - min(ys)))

    vis = []
    for t in trans:
        v0, v1, v2 = t
        ux = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
        vx = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])
        n = (ux[1] * vx[2] - ux[2] * vx[1],
             ux[2] * vx[0] - ux[0] * vx[2],
             ux[0] * vx[1] - ux[1] * vx[0])
        if n[2] <= 0:          # backface (câmera olha para -Z)
            continue
        nn = math.sqrt(sum(c * c for c in n)) or 1.0
        n = tuple(c / nn for c in n)
        dif = max(0.0, n[0] * luz[0] + n[1] * luz[1] + n[2] * luz[2])
        spec = max(0.0, n[2]) ** 24
        s = 0.22 + 0.72 * dif
        cor = tuple(min(255, int(c * s + 90 * spec)) for c in cor_base)
        prof = (v0[2] + v1[2] + v2[2]) / 3
        pts = [((v[0] - cx) * escala + w / 2, h / 2 - (v[1] - cy) * escala)
               for v in t]
        vis.append((prof, pts, cor))

    vis.sort(key=lambda x: x[0])   # pintor: de trás para frente
    img = Image.new("RGB", tam, fundo)
    dr = ImageDraw.Draw(img)
    for _, pts, cor in vis:
        dr.polygon(pts, fill=cor)
    return img


def main():
    stl = sys.argv[1] if len(sys.argv) > 1 else "stl/manopla_esquerda_neo2008.stl"
    saida = sys.argv[2] if len(sys.argv) > 2 else "docs/preview.png"
    tris = subdividir(carregar_stl(stl))

    vistas = [
        ("Vista 3/4", (-68, 0, -28)),
        ("Vista lateral", (-90, 0, 0)),
        ("Ponta (lado de fora)", (-25, 0, 0)),
        ("Boca (lado do manete)", (65, 0, 180)),
    ]
    tam = (560, 560)
    cols = 2
    linhas = (len(vistas) + cols - 1) // cols
    canvas = Image.new("RGB", (tam[0] * cols, tam[1] * linhas + 46), (245, 246, 248))
    dr = ImageDraw.Draw(canvas)
    try:
        fonte = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        fonte_tit = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except OSError:
        fonte = fonte_tit = ImageFont.load_default()

    dr.text((canvas.width / 2, 24),
            "Manopla esquerda — Yamaha Neo 115 (2008) — TPU",
            fill=(30, 40, 60), font=fonte_tit, anchor="mm")

    for i, (rotulo, rot) in enumerate(vistas):
        img = renderizar(tris, rot, tam)
        x, y = (i % cols) * tam[0], 46 + (i // cols) * tam[1]
        canvas.paste(img, (x, y))
        dr.text((x + tam[0] / 2, y + tam[1] - 26), rotulo,
                fill=(70, 80, 100), font=fonte, anchor="mm")

    canvas.save(saida)
    print(f"OK: {saida} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    main()
