// Manopla esquerda — Yamaha Neo 115 (2008)
// Guidão padrão 7/8" (22,2 mm). Fonte paramétrica em OpenSCAD.
//
// Mesma geometria do script scripts/gerar_stl.py — edite os parâmetros
// abaixo e renderize (F6) para exportar seu próprio STL.

// ---------------- Parâmetros (mm) ----------------
diam_guidao     = 22.2;   // diâmetro do tubo do guidão (7/8")
folga_diametral = -0.6;   // negativo = interferência (aperto) p/ TPU
prof_furo       = 114;    // profundidade do furo

comp_total  = 120;        // comprimento total
raio_corpo  = 14;         // raio externo base (Ø28)
raio_aba    = 19;         // raio da aba (Ø38)
comp_aba    = 4;          // trecho cilíndrico da aba
comp_filete = 3;          // transição aba -> corpo

dome_z0 = 110;            // início da ponta arredondada

num_nervuras = 8;         // anéis de pega
nerv_z_ini   = 14;
nerv_z_fim   = 104;
nerv_altura  = 1.5;
nerv_sigma   = 2.2;

swell_altura = 0.8;       // engrossamento ergonômico central
swell_centro = 60;
swell_sigma  = 30;

passo_z = 0.35;           // resolução axial do perfil
$fn = 128;                // resolução angular

// ---------------- Geometria ----------------
raio_furo = (diam_guidao + folga_diametral) / 2;
dome_len  = comp_total - dome_z0;

function smoothstep(t) = let (u = max(0, min(1, t))) u * u * (3 - 2 * u);

function r_nervuras(z) =
    num_nervuras <= 1 ? 0 :
    let (passo = (nerv_z_fim - nerv_z_ini) / (num_nervuras - 1))
    nerv_altura * max([for (k = [0 : num_nervuras - 1])
        exp(-pow((z - (nerv_z_ini + k * passo)) / nerv_sigma, 2))]);

function r_corpo(z) =
    raio_corpo
    + swell_altura * exp(-pow((z - swell_centro) / swell_sigma, 2))
    + r_nervuras(z);

function r_ext(z) =
    z <= comp_aba ? raio_aba :
    z <= comp_aba + comp_filete ?
        raio_aba + (r_corpo(z) - raio_aba) * smoothstep((z - comp_aba) / comp_filete) :
    z < dome_z0 ? r_corpo(z) :
    r_corpo(dome_z0) * sqrt(max(0, 1 - pow(min(1, (z - dome_z0) / dome_len), 2)));

module manopla() {
    difference() {
        rotate_extrude()
            polygon(concat(
                [[0, 0]],
                [for (z = [0 : passo_z : comp_total - passo_z]) [r_ext(z), z]],
                [[0, comp_total]]
            ));
        // furo do guidão
        translate([0, 0, -0.5])
            cylinder(h = prof_furo + 0.5, r = raio_furo);
    }
}

manopla();
