#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de STL — Manopla esquerda para Yamaha Neo 115 (2008)
Guidão padrão 7/8" (22,2 mm). Não requer bibliotecas externas.

Uso:
    python3 gerar_stl.py [saida.stl]

O modelo é gerado com o eixo Z ao longo da manopla, com a boca
(lado da aba/flange) em Z=0 — já na orientação ideal de impressão
(em pé, boca para baixo).
"""

import math
import struct
import sys

# ---------------------------------------------------------------------------
# Parâmetros (mm) — ajuste aqui se precisar de outra medida
# ---------------------------------------------------------------------------
DIAM_GUIDAO = 22.2          # diâmetro do tubo do guidão (7/8")
FOLGA_DIAMETRAL = -0.6      # negativo = interferência (aperto) para TPU
RAIO_FURO = (DIAM_GUIDAO + FOLGA_DIAMETRAL) / 2.0   # 10,8 mm
PROF_FURO = 114.0           # profundidade do furo do guidão

COMP_TOTAL = 120.0          # comprimento total da manopla
RAIO_CORPO = 14.0           # raio externo base do corpo (Ø28)
RAIO_ABA = 19.0             # raio da aba junto ao punho da embreagem (Ø38)
COMP_ABA = 4.0              # trecho cilíndrico da aba
COMP_FILETE = 3.0           # transição suave aba -> corpo

DOME_Z0 = 110.0             # início da ponta arredondada (domo)
DOME_LEN = COMP_TOTAL - DOME_Z0

# Anéis de pega (nervuras circunferenciais)
NUM_NERVURAS = 8
NERV_Z_INI = 14.0
NERV_Z_FIM = 104.0
NERV_ALTURA = 1.5           # altura da nervura acima do corpo
NERV_SIGMA = 2.2            # "largura" gaussiana da nervura

# Engrossamento ergonômico sutil no meio da pega
SWELL_ALTURA = 0.8
SWELL_CENTRO = 60.0
SWELL_SIGMA = 30.0

# Malha
N_THETA = 128               # segmentos ao redor do eixo
PASSO_Z = 0.35              # passo axial de amostragem


def smoothstep(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def raio_corpo(z: float) -> float:
    """Raio do corpo (sem aba/domo): base + swell + nervuras."""
    r = RAIO_CORPO
    r += SWELL_ALTURA * math.exp(-(((z - SWELL_CENTRO) / SWELL_SIGMA) ** 2))
    if NUM_NERVURAS > 1:
        passo = (NERV_Z_FIM - NERV_Z_INI) / (NUM_NERVURAS - 1)
        for k in range(NUM_NERVURAS):
            zc = NERV_Z_INI + k * passo
            r += NERV_ALTURA * math.exp(-(((z - zc) / NERV_SIGMA) ** 2))
    return r


def raio_externo(z: float) -> float:
    """Perfil externo completo em função de z (0 = boca, COMP_TOTAL = ponta)."""
    if z <= COMP_ABA:
        return RAIO_ABA
    if z <= COMP_ABA + COMP_FILETE:
        s = smoothstep((z - COMP_ABA) / COMP_FILETE)
        return RAIO_ABA + (raio_corpo(z) - RAIO_ABA) * s
    if z < DOME_Z0:
        return raio_corpo(z)
    # Domo elíptico na ponta
    r0 = raio_corpo(DOME_Z0)
    t = (z - DOME_Z0) / DOME_LEN
    t = min(t, 1.0)
    return r0 * math.sqrt(max(0.0, 1.0 - t * t))


def gerar_malha():
    """Constrói a lista de triângulos (cada um: 3 vértices (x, y, z))."""
    tris = []
    n = N_THETA
    cos_t = [math.cos(2 * math.pi * i / n) for i in range(n)]
    sin_t = [math.sin(2 * math.pi * i / n) for i in range(n)]

    def anel(r, z):
        return [(r * cos_t[i], r * sin_t[i], z) for i in range(n)]

    def parede(anel_a, anel_b, externa=True):
        """Liga dois anéis com quads; 'externa' controla a orientação."""
        for i in range(n):
            j = (i + 1) % n
            a0, a1 = anel_a[i], anel_a[j]
            b0, b1 = anel_b[i], anel_b[j]
            if externa:
                tris.append((a0, a1, b1))
                tris.append((a0, b1, b0))
            else:
                tris.append((a0, b1, a1))
                tris.append((a0, b0, b1))

    # ----- superfície externa: anéis de z=0 até perto da ponta -----
    zs = []
    z = 0.0
    while z < COMP_TOTAL:
        zs.append(z)
        z += PASSO_Z
    # última linha: onde o domo chega a raio pequeno (evita triângulos ruins)
    r_min_topo = 1.2
    z_topo = DOME_Z0 + DOME_LEN * math.sqrt(1.0 - (r_min_topo / raio_corpo(DOME_Z0)) ** 2)
    zs = [zv for zv in zs if zv < z_topo] + [z_topo]

    aneis_ext = [anel(raio_externo(zv), zv) for zv in zs]
    for a, b in zip(aneis_ext[:-1], aneis_ext[1:]):
        parede(a, b, externa=True)

    # tampa da ponta: leque do último anel até o ápice
    apice = (0.0, 0.0, COMP_TOTAL)
    topo = aneis_ext[-1]
    for i in range(n):
        j = (i + 1) % n
        tris.append((topo[i], topo[j], apice))

    # ----- furo interno -----
    boca_ext = aneis_ext[0]
    boca_int = anel(RAIO_FURO, 0.0)
    fundo_int = anel(RAIO_FURO, PROF_FURO)

    # anel plano da boca (normal -Z): liga raio externo ao raio do furo
    for i in range(n):
        j = (i + 1) % n
        tris.append((boca_ext[i], boca_int[i], boca_ext[j]))
        tris.append((boca_ext[j], boca_int[i], boca_int[j]))

    # parede interna do furo (normal aponta para o eixo)
    parede(boca_int, fundo_int, externa=False)

    # fundo do furo: leque com normal -Z (voltada para a boca)
    centro_fundo = (0.0, 0.0, PROF_FURO)
    for i in range(n):
        j = (i + 1) % n
        tris.append((centro_fundo, fundo_int[j], fundo_int[i]))

    return tris


def verificar_estanque(tris):
    """Toda aresta deve ser compartilhada por exatamente 2 triângulos."""
    def chave(v):
        return (round(v[0], 5), round(v[1], 5), round(v[2], 5))

    arestas = {}
    for t in tris:
        vs = [chave(v) for v in t]
        for a, b in ((vs[0], vs[1]), (vs[1], vs[2]), (vs[2], vs[0])):
            e = (a, b) if a <= b else (b, a)
            arestas[e] = arestas.get(e, 0) + 1
    ruins = [e for e, c in arestas.items() if c != 2]
    return ruins


def escrever_stl_binario(caminho, tris, nome=b"manopla_esquerda_neo2008"):
    with open(caminho, "wb") as f:
        f.write(nome.ljust(80, b"\0"))
        f.write(struct.pack("<I", len(tris)))
        for (v0, v1, v2) in tris:
            ux = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
            vx = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])
            nx = ux[1] * vx[2] - ux[2] * vx[1]
            ny = ux[2] * vx[0] - ux[0] * vx[2]
            nz = ux[0] * vx[1] - ux[1] * vx[0]
            norm = math.sqrt(nx * nx + ny * ny + nz * nz) or 1.0
            f.write(struct.pack("<3f", nx / norm, ny / norm, nz / norm))
            for v in (v0, v1, v2):
                f.write(struct.pack("<3f", *v))
            f.write(struct.pack("<H", 0))


def main():
    saida = sys.argv[1] if len(sys.argv) > 1 else "manopla_esquerda_neo2008.stl"
    tris = gerar_malha()
    ruins = verificar_estanque(tris)
    if ruins:
        print(f"AVISO: {len(ruins)} arestas não-manifold!", file=sys.stderr)
        sys.exit(1)
    escrever_stl_binario(saida, tris)
    print(f"OK: {saida}")
    print(f"  Triângulos: {len(tris)}")
    print(f"  Comprimento: {COMP_TOTAL} mm | Furo: Ø{2*RAIO_FURO:.1f} x {PROF_FURO} mm")
    print(f"  Aba: Ø{2*RAIO_ABA:.0f} mm | Corpo: Ø{2*RAIO_CORPO:.0f} mm (+nervuras)")
    print("  Malha estanque (todas as arestas compartilhadas por 2 triângulos).")


if __name__ == "__main__":
    main()
