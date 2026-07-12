#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera docs/perfil.svg — corte longitudinal da manopla para a documentação."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from gerar_stl import (  # noqa: E402
    raio_externo, COMP_TOTAL, RAIO_FURO, PROF_FURO, RAIO_ABA
)

ESCALA = 4.0
MARGEM = 30.0


def main():
    saida = sys.argv[1] if len(sys.argv) > 1 else "perfil.svg"

    zs = [i * 0.25 for i in range(int(COMP_TOTAL / 0.25) + 1)]
    perfil = [(z, raio_externo(z)) for z in zs]

    largura = COMP_TOTAL * ESCALA + 2 * MARGEM
    altura = 2 * RAIO_ABA * ESCALA + 2 * MARGEM
    cy = altura / 2.0

    def px(z):
        return MARGEM + z * ESCALA

    def py(r):
        return cy - r * ESCALA

    sup = " ".join(f"{px(z):.1f},{py(r):.1f}" for z, r in perfil)
    inf = " ".join(f"{px(z):.1f},{py(-r):.1f}" for z, r in reversed(perfil))
    contorno = f"{sup} {inf}"

    furo = (f"{px(0):.1f},{py(RAIO_FURO):.1f} {px(PROF_FURO):.1f},{py(RAIO_FURO):.1f} "
            f"{px(PROF_FURO):.1f},{py(-RAIO_FURO):.1f} {px(0):.1f},{py(-RAIO_FURO):.1f}")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura:.0f} {altura:.0f}"
     font-family="sans-serif" font-size="13">
  <rect width="100%" height="100%" fill="white"/>
  <polygon points="{contorno}" fill="#cfe3f7" stroke="#1f4e79" stroke-width="1.5"/>
  <polygon points="{furo}" fill="white" stroke="#c0504d" stroke-width="1" stroke-dasharray="5,3"/>
  <line x1="{px(0):.1f}" y1="{cy:.1f}" x2="{px(COMP_TOTAL):.1f}" y2="{cy:.1f}"
        stroke="#888" stroke-width="0.7" stroke-dasharray="8,4"/>
  <text x="{px(COMP_TOTAL/2):.1f}" y="{altura - 8:.1f}" text-anchor="middle" fill="#333">
    comprimento total {COMP_TOTAL:.0f} mm — furo Ø{2*RAIO_FURO:.1f} × {PROF_FURO:.0f} mm (tracejado) — aba Ø{2*RAIO_ABA:.0f} mm
  </text>
</svg>
"""
    with open(saida, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"OK: {saida}")


if __name__ == "__main__":
    main()
